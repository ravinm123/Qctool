from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
import os
import json





class UserManager(BaseUserManager):
    def create_user(self, email, username,password=None):
        """
        Creates and saves a User with the given email,  and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username,role,password=None):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            role,
            username,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


# def laod_Role():
#     current_dir=os .path.dirname(os.path.abspath(__file__))
#     file_name='role_choices.json'
#     file_path=os.path.json(current_dir,file_name)

#     with open(file_path,'r') as file:
#         role_choices=json.load(file)
#     return role_choices


class User(AbstractBaseUser):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length=250)
    email = models.EmailField(verbose_name="email address",max_length=255,unique=True,) 
    ROLE_CHOICES = [
    ('manager', 'Manager'),
    ('quality_checker', 'Quality Checker'),
    ('teamlead', 'Team Lead'),
]




    role=models.CharField(max_length=250,choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
