from django.urls import path, include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from rest_framework import permissions, status, generics, request, viewsets
from account import views
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
)
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('login/', obtain_auth_token, name="login"),
    path('register/', register_view, name="register"),

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

    path('verification/', verify_number, name="phone_verification"),
    path('verification/token/', verify_otp, name="token_validation"),
]
