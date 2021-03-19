from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
# from versatileimagefield.fields import PPOIField
# Custome user class with necessary fields


class CustomAccountManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, password=None, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_admin', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError('Superuser must be assigned to is_staff=True')

        if other_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must be assigned to is_superuser=True')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, password=None, **extra_fields):

        if not email:
            raise ValueError('You must provide an email address')
        if not username:
            raise ValueError('You must provide a username')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user


class NewUser(AbstractBaseUser):

    first_name = models.CharField(max_length=150, blank=False)
    last_name = models.CharField(max_length=150, blank=True)
    mobile = models.CharField(max_length=150, blank=False)
    email = models.EmailField(verbose_name="email", unique=True)
    username = models.CharField(max_length=150, unique=True)
    address = models.CharField(max_length=150, blank=True)
    # image = models.ForeignKey('accounts.ProfileImage', related_name='users', on_delete=models.CASCADE)
    profile_image = models.ImageField('profile_image', blank=True)
    # profile_image = VersatileImageField('Profile Image', upload_to='profile_image', ppoi_field='image_ppoi')
    # image_ppoi = PPOIField()
    start_date = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomAccountManager()

    # Required fields
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name', 'last_name', 'mobile', 'email']

    def __str__(self):
        return self.username

    # For checking permissions
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # Does this user have permission to view the app
    def has_module_perms(self, app_label):
        return True


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
