from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import NewUser
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password
# from versatileimagefield.serializers import VersatileImageFieldSerializer
# from rest_flex_fields import FlexFieldsModelSerializer
# from .image_conversion import Base64ImageField
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_bytes, smart_str, force_str, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from rest_framework.exceptions import AuthenticationFailed


# User Serializer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = NewUser
        fields = ('id', 'username', 'email')


# User Serializer
class RegisterSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(
        style={'input_type': 'password'}, write_only=True)

    profile_image = serializers.ImageField(max_length=None, use_url=True)

    # profile_image = Base64ImageField(required=False)
    class Meta:
        model = NewUser
        fields = (
            'first_name', 'last_name', 'mobile', 'email', 'username', 'address', 'profile_image', 'password', 'password2')
        extra_kwargs = {
            'password': {'write_only': True}
        }

    # Saving user and thier required fields
    def save(self):
        user = NewUser(
            first_name=self.validated_data['first_name'],
            last_name=self.validated_data['last_name'],
            mobile=self.validated_data['mobile'],
            email=self.validated_data['email'],
            username=self.validated_data['username'],
            address=self.validated_data['address'],
            profile_image=self.validated_data['profile_image'],
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']

        # Password double checking
        if password != password2:
            raise serializers.ValidationError(
                {'password': 'Password does not match'})
        user.set_password(password)
        user.save()
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        user = authenticate(**data)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")


# Account Property Serializer
class AccountPropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = NewUser
        # fields = ['pk', 'email', 'username',
        #           'first_name', 'last_name', 'mobile', 'address', 'profile_image']
        fields = ('__all__')


# Password change serializer
class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = NewUser
        fields = ('old_password', 'password', 'password2')

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."})

        return attrs

    def validate_old_password(self, value):
        user = self.context['request'].user
        if not user.check_password(value):
            raise serializers.ValidationError(
                {"old_password": "Old password is not correct"})
        return value

    def update(self, instance, validated_data):

        instance.set_password(validated_data['password'])
        instance.save()

        return instance


# Password reset serializers
class ResetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=5)

    class Meta:
        fields = ['email']


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(
        min_length=6, max_length=30, write_only=True)
    token = serializers.CharField(min_length=1, write_only=True)
    uidb64 = serializers.CharField(min_length=1, write_only=True)

    class Meta:
        fields = ['password', 'token', 'uidb64']

    def validate(self, attrs):
        try:
            password = attrs.get('password')
            token = attrs.get('token')
            uidb64 = attrs.get('uidb64')

            id = force_str(urlsafe_base64_decode(uidb64))
            user = NewUser.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('The reset link is not valid!', 401)

            user.set_password(password)
            user.save()

        except Exception as e:
            raise AuthenticationFailed('The reset link is not valid!', 401)

        return super().validate(attrs)


# Mobile number serializer for OTP
class MobileSerializer(serializers.Serializer):
    mobile = serializers.CharField()
    # print(mobile);


# OTP serializer
class OtpSerializer(serializers.Serializer):
    otp = serializers.CharField()
    # mobile_no = serializers.CharField()
    # print(otp);
