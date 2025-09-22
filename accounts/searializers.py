from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password




User = get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only= True, required =True, validators=[validate_password])
    password2 = serializers.CharField(write_only= True, required= True)
    
    
    class Meta:
        model=User
        fields = ('username', "email", "password", "password2")
        
        
        
    def validate(self, attributes):
        if attributes ["password"] != attributes ["password2"]:
            raise serializers.ValidationError({"password": "Passwords must match"})
        return attributes
    
    def create(self, validated_data):
        user = User.objects.create(username= validated_data ["username"], email = validated_data["email"])
        user.set_password(validated_data["password"])
        user.save()
        return user


class LogoutSerializers(serializers.Serializer):
    refresh = serializers.CharField()
    


# from rest_framework import serializers
# Brings in DRF serializers, which convert between JSON ↔ Django models/objects, and also handle validation.
# from django.contrib.auth import get_user_model
# Ensures you always reference the custom user model set in AUTH_USER_MODEL (instead of hardcoding User).
# from django.contrib.auth.password_validation import validate_password
# Uses Django’s built-in password validators (like minimum length, common password, numeric-only, etc.) to enforce strong passwords.
# class RegisterSerializer(serializers.ModelSerializer):
# Inherits from ModelSerializer, which auto-generates serializer fields based on the model fields (User).
# Password fields
# password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
# password2 = serializers.CharField(write_only=True, required=True)
# password field
# CharField → expects a string from input JSON.
# write_only=True → will be used for input, but never returned in API responses (prevents leaking password in JSON output).
# validators=[validate_password] → runs Django’s configured password validators. If the password is too short, too common, all-numeric, etc., it raises a ValidationError.
# password2 field
# Just another input field for confirmation.
# It’s not part of the User model, but adding it here ensures the API requires the client to submit it.
# 👉 So your registration JSON input looks like:
# json
# Copy code
# {
#   "username": "favour",
#   "email": "favour@example.com",
#   "password": "StrongPass123",
#   "password2": "StrongPass123"
# }
# Meta class
# class Meta:
#     model = User
#     fields = ('username', "email", "password", "password2")

# Meta is a special inner class that configures the serializer.
# Tells DRF to:

# Use the User model for mapping fields.

# Expose these four fields in API input/output.

# Normally, ModelSerializer would generate fields automatically from the model, but here you explicitly specify which fields you want. This prevents leaking fields like is_staff, last_login, etc.

# Validation method
# def validate(self, attrs):
#     if attrs["password"] != attrs["password2"]:
#         raise serializers.ValidationError({"password": "Passwords must match"})
#     return attrs

# Runs after field-level validation.

# attrs is a dict of validated data so far (username, email, password, password2).

# Compares password and password2.

# If they don’t match → raises ValidationError. This stops the request and returns a 400 Bad Request response to the client:

# {"password": ["Passwords must match"]}


# If they match → returns attrs unchanged, so serialization continues.

# Create method
# def create(self, validated_data):
#     user = User.objects.create(
#         username=validated_data["username"], 
#         email=validated_data["email"]
#     )
#     user.set_password(validated_data["password"])
#     user.save()
#     return user


# create() is called by DRF when .save() is executed on the serializer.

# It receives validated_data, which is guaranteed clean from validation step.

# Step by step:

# User.objects.create(...) → inserts a new row in the User table with username + email.
# ⚠️ Bug alert: in your code, you had an extra , after the line — that actually makes user a tuple not a User instance. Fix is: remove the comma.

# user = User.objects.create(
#     username=validated_data["username"], 
#     email=validated_data["email"]
# )


# user.set_password(...) → hashes the raw password into a secure salted hash using Django’s PBKDF2 (or configured algorithm). Never store raw passwords!

# user.save() → saves the password hash into the DB (updates the password field).

# return user → returns the newly created user instance so DRF can serialize it back in response (minus write-only fields).

# Runtime behavior in API

# When a client sends POST /api/register/ with valid JSON:

# DRF parses the JSON.

# RegisterSerializer validates:

# Checks required fields.

# Validates password with Django’s password validators.

# Confirms password == password2.

# If validation passes → create() is called, which:

# Creates user with username and email.

# Hashes and stores password.

# Saves user in DB.

# Response → typically returns the new user’s username and email, but not the password.

# Example

# Request:

# POST /api/register/
# Content-Type: application/json

# {
#   "username": "favour",
#   "email": "favour@example.com",
#   "password": "Secretpass123!",
#   "password2": "Secretpass123!"
# }


# Response:

# {
#   "username": "favour",
#   "email": "favour@example.com"
# }