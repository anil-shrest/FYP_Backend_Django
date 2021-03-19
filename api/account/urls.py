from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from account import views
from rest_framework import permissions, status, generics, request, viewsets
from .views import(
    register_view,
    HelloView,
    account_property_update,
    account_property_view,
    ChangePasswordView,
    verify_number,
    verify_otp,
    PasswordTokenCheck,
    RequestPasswordResetEmail,
    SetNewPassword,
#     UserList,
)
from rest_framework.authtoken.views import obtain_auth_token
# from rest_framework.authtoken import views

# app_name = "accounts"

urlpatterns = [
    path('register/', register_view, name="register"),
    path('login/', obtain_auth_token, name="login"),
#     path('users/', views.UserList.as_view(), name="list"),

    # path('image/', ImageViewSet.as_view, name='image'),
    # path('log/', LoginView, name='log'),
    # path('token/', views.obtain_auth_token),
    path('hello/', views.HelloView.as_view(), name="hello"),
    path('properties/', account_property_view, name="property"),
    path('properties/update/', account_property_update, name="update"),

    path('change_password/<int:pk>/', ChangePasswordView.as_view(),
         name='change-password'),
    path('reset_email/', RequestPasswordResetEmail.as_view(), name="reset_email"),
    path('password_reset/<uidb64>/<token>/',
         PasswordTokenCheck.as_view(), name="password_reset_confirm"),
    path('password_reset_compelete/', SetNewPassword.as_view(),
         name="password_reset_compelete"),
    # path('reset_password/', auth_views.PasswordResetView.as_view(), name="reset_password"),
    # path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(), name="password_reset_done"),
    # path('reset_password/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    # path('reset_password_complete/', auth_views.PasswordResetConfirmView.as_view(), name="password_reset_complete"),

    path('verification/', verify_number, name="phone_verification"),
    path('verification/token/', verify_otp, name="token_validation"),
    # path('app/password_reset/',
    #      include('django_rest_passwordreset.urls', namespace='password_reset')),
]
