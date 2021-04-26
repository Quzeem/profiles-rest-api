from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
  """Manages users"""

  def create_user(self, name, email, password=None):
    """Create a new user"""
    if not email:
      raise ValueError('User must have an email address')

    email = self.normalize_email(email) # Make email lowercase
    user = self.model(email=email, name=name)
    user.set_password(password)
    user.save(using=self._db)

    return user

  def create_superuser(self, name, email, password):
    """Create a new superuser"""
    user = self.create_user(name, email, password)
    user.is_superuser = True,
    user.is_staff = True
    user.save(using=self._db)

    return user


class User(AbstractBaseUser, PermissionsMixin):
  """Databse model for users"""
  email = models.EmailField(max_length=255, unique=True)
  name = models.CharField(max_length=255)
  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  # UserManager tells Django how to interact with our custom user model in order to create a user
  objects = UserManager()

  USERNAME_FIELD = 'email' # Override the default username field which is required by default to email
  REQUIRED_FIELDS = ['name'] # Additional required fields

  # methods to interact with our custom user model
  def get_full_name(self):
    """Retriever user full name"""
    return self.name

  def get_short_name(self):
    """Retrieve short name of user"""
    return self.name

  def __str__(self):
    """Return string representation of a user"""
    return self.email