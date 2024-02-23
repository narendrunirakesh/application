from django.db import models

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, role, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        user.roles.add(*role)  # Add roles to the user
        return user

    def create_superuser(self, email, username, role, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self.create_user(email, username, role, password, **extra_fields)

# class Role(models.Model):
#     DEPARTMENT_MANAGER = 'Department Manager'
#     STORE_MANAGER = 'Store Manager'

    # ROLE_CHOICES = (
    #     ('DEPARTMENT_MANAGER', 'Department Manager'),
    #     ('STORE_MANAGER', 'Store Manager'),

    # )
        
    

    # name = models.CharField(max_length=50, choices=ROLE_CHOICES, unique=True)

    # def __str__(self):
    #     return self.name
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=150, unique=True)
    DEPARTMENT_MANAGER = 'Department Manager'
    STORE_MANAGER = 'Store Manager'
    ROLE_CHOICES = [
        (DEPARTMENT_MANAGER, 'Department Manager'),
        (STORE_MANAGER, 'Store Manager'),
    ]

    # Use the choices in the roles field
    role = models.CharField(max_length=50, choices=ROLE_CHOICES)
    roles = models.CharField(max_length=50, choices=ROLE_CHOICES, default = STORE_MANAGER)  # Many-to-many relationship with Role
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'roles']

    def __str__(self):
        return self.email


    # class Meta:
    #     # Add related_name attributes to avoid clashes with auth.User
    #     # Set related_name to 'customuser_groups' and 'customuser_user_permissions'
    #     # This will change the reverse accessor names
    #     # For example, instead of 'user.groups', it will be 'user.customuser_groups'
    #     # Similarly, instead of 'user.user_permissions', it will be 'user.customuser_user_permissions'
    #     # You can choose any custom related_name you prefer
    #     # Ensure that they are unique and descriptive
    #     # You need to run makemigrations and migrate after making these changes
    #     # to apply the changes to your database schema
    #     related_name = 'customuser_%(class)s'
