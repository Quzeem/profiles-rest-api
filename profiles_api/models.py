from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings  # settings module of the root project


class UserManager(BaseUserManager):
    """Manages users"""

    def create_user(self, name, email, password=None):
        """Create a new user"""
        if not email:
            raise ValueError('User must have an email address')

        email = self.normalize_email(email)  # Make email lowercase
        user = self.model(email=email, name=name)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, name, email, password):
        """Create a new superuser"""
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Databse model for users"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # UserManager tells Django how to interact with our custom user model
    objects = UserManager()

    # Override the default username field which is required by default to email
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']  # Additional required fields

    # methods to interact with our custom user model
    def get_full_name(self):
        """Retrieve user full name"""
        return self.name

    def get_short_name(self):
        """Retrieve user short name"""
        return self.name

    def __str__(self):
        """Return string representation of users"""
        return self.email


class UserProfileFeed(models.Model):
    """Database model for user profile feed"""
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    status_text = models.CharField(max_length=255)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return string representation of a model instance"""
        return self.status_text
