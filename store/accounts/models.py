from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from random import randint
from django.conf import settings
# Create your models here.


class User(AbstractUser):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=100, blank=False)
    is_active = models.BooleanField(default=False)
    activation_code = models.CharField(max_length=6, blank=True)

    def __str__(self):
        return self.username

    def generate_activation_code(self):
        activation_code = str(randint(100000, 999999))
        self.activation_code = activation_code
        self.save()

    def create_superuser(self):
        self.is_superuser = True
        self.is_admin = True
        self.is_active = True
        self.save()



class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users_photo', blank=True)

    def __str__(self):
        return f'Profile for user {self.user.username}'



