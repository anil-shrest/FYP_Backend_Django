from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, parser_classes
from .serializers import RegisterSerializer, LoginSerializer, AccountPropertySerializer, ChangePasswordSerializer, ResetPasswordSerializer, MobileSerializer, OtpSerializer, SetNewPasswordSerializer, AccountUpdateSerializer
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework import permissions, status, generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.parsers import FileUploadParser, JSONParser, MultiPartParser
from django.contrib.auth import authenticate
from django.http import JsonResponse
from .models import NewUser
from rest_framework.authtoken import views
from .sms_verification import verification_checks, verifications
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from .utils import Util
from .models import NewUser


# class UserList(generics.ListAPIView):
#     serializer_class = AccountPropertySerializer
#     queryset = NewUser.objects.all()

# View for OTP setup
@api_view(['POST'])
@permission_classes([])
def verify_number(request):
    if request.method == 'POST':
        serializer = MobileSerializer(data=request.data)
        if serializer.is_valid():
            request.session['mobile'] = serializer.data['mobile']
            verify = verifications(request.session['mobile'], 'sms')
            print(request.session['mobile'])
        return Response({'mobile_no': request.session['mobile']})


# View for OTP verification
@api_view(['POST'])
@permission_classes([])
def verify_otp(request):
    if request.method == 'POST':
        serializer = OtpSerializer(data=request.data)
        # serializer2 = MobileSerializer(data=request.data)
        if serializer.is_valid():
            # print(serializer.data['mobile'])
            print(serializer.data['otp'])
            # request.session['mobile'] = serializer.data['otp']
            verify = verification_checks(
                request.session['mobile'], serializer.data['otp'])
            if verify.status == 'approved':
                # print(serializer.data['mobile'])
                print(serializer.data['otp'])
                return Response({'status': verify.status})
        return Response({'otp': serializer.data['otp']})


# View for registering a new user

@api_view(['POST', ])
@parser_classes((MultiPartParser, ))
def register_view(request):
    if request.method == 'POST':
        serializer = RegisterSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            user = serializer.save()
            data['response'] = "Successfully regsitered new user"
            data['first_name'] = user.first_name
            data['last_name'] = user.last_name
            data['mobile'] = user.mobile
            data['email'] = user.email
            data['username'] = user.username
            data['address'] = user.address
            # data['profile_image'] = user.profile_image
            token = Token.objects.get(user=user).key
            data['token'] = token
        else:
            data = serializer.errors
        return Response(data)


# class LoginView(views.APIView):
#     serializer_class = LoginSerializer

#     def post(self, request, **kwargs):
#         serializer = self.serializer_class(data=request.data)
#         if serializer.is_valid():
#             user = NewUser.objects.get(username=serializer.data['username'])
#             token = Token.objects.create(user=user)

#             response = {}
#             response['user'] = serializer.data
#             response['token'] = token.key

#             return Response(response, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


# View for accounts properties
@api_view(['GET', ])
# @permission_classes((IsAuthenticated,))
def account_property_view(request):
    # user = NewUser.objects.get(username='bing')
    try:
        user = request.user
    except user.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        print('THE USER IS', user)
        serializer = AccountPropertySerializer(user)
        return Response(serializer.data)


# View for accounts properties update
@api_view(['PUT', ])
@permission_classes((IsAuthenticated,))
def account_property_update(request):
    try:
        user = request.user
    except user.DoesNotExists:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == "PUT":
        serializer = AccountUpdateSerializer(user, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['response'] = "Account update successful"
            return Response(data=data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views for password change
class ChangePasswordView(generics.UpdateAPIView):

    queryset = NewUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = ChangePasswordSerializer


# views for password reset
class RequestPasswordResetEmail(generics.GenericAPIView):
    serializer_class = ResetPasswordSerializer

    def post(self, request):
        data = {'request': request, 'data': request.data}
        serializer = self.serializer_class(data=data)

        email = request.data['email']

        if NewUser.objects.filter(email=email).exists():
            user = NewUser.objects.get(email=email)
            uidb64 = urlsafe_base64_encode(smart_bytes(user.id))
            token = PasswordResetTokenGenerator().make_token(user)
            current_site = get_current_site(
                request=request).domain
            relativeLink = reverse('password_reset_confirm', kwargs={
                                   'uidb64': uidb64, 'token': token})
            absurl = 'http://'+current_site + relativeLink
            email_body = 'Hello, \n Use the given below link to reset your password \n' + absurl
            data = {'email_body': email_body, 'to_email': user.email,
                    'email_subject': 'Password Reset'}

            Util.send_email(data)
        return Response({'success': 'Link for password reset mail has been sent'}, status=status.HTTP_200_OK)


# To check the values after opening reset email
class PasswordTokenCheck(generics.GenericAPIView):

    def get(self, request, uidb64, token):

        try:
            id = smart_str(urlsafe_base64_decode(uidb64))
            user = NewUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'Token is invalid, please request a new one'})

            return Response({'success': True, 'message': 'Credentilas Valid', 'uidb64': uidb64, 'token': token}, status=status.HTTP_200_OK)

        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error': 'Token is invalid, please request a new one'})


# To reset old password and save new one
class SetNewPassword(generics.GenericAPIView):
    serializer_class = SetNewPasswordSerializer

    def patch(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'success': True, 'message': 'Password reset successful'}, status=status.HTTP_200_OK)
