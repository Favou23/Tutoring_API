from django.db import models
from django.contrib.auth.models import AbstractUser 


class User(AbstractUser):
    email = models.EmailField(max_length=200,unique=True)
    
    
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]
    
    def __str__(self):
        return self.email
    


# from django.db import models
# Imports Django’s ORM base classes — used to declare model fields and meta options.
# from django.contrib.auth.models import AbstractUser
# Imports AbstractUser, which is a full User class implementation (username, first_name, last_name, email, password, is_staff, is_active, is_superuser, groups, user_permissions, last_login, date_joined, etc.) but meant to be extended. It already includes authentication helpers and default manager.
# class User(AbstractUser):
# Creates a new model User that inherits from AbstractUser. You get all the built-in fields and methods of Django’s default user, but you can override or add fields/behaviors.
# email = models.EmailField(unique=True)
# Declares an email field (overrides the email from AbstractUser), and sets a unique constraint in the database.
# EmailField applies Django’s email validation and stores it as a text column (max length normally 254).
# unique=True creates a unique index/constraint — two rows cannot have the same email.
# USERNAME_FIELD = "email"
# Tells Django: use the email field as the unique identifier for authentication instead of username.
# This affects authenticate(), createsuperuser, get_by_natural_key, and other auth internals.
# REQUIRED_FIELDS = ["username"]
# Used by createsuperuser management command (and by some other utilities) to know which fields to prompt for in addition to USERNAME_FIELD and password.
# Because USERNAME_FIELD is email, Django will prompt for password and any fields in REQUIRED_FIELDS (here username) when you run python manage.py createsuperuser.
# def __str__(self): return self.email
# When you print(user) or Django displays the user in admin/choices, it will show the email. This is helpful and conventional when email is the identifier.