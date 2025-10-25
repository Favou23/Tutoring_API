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
    
    
    
class ResetPasswordRequestSerializer(serializers.Serializer):
    email = serializers.EmailField()


class SetNewPasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only= True,validators=[validate_password])
    password2= serializers.CharField(write_only= True)
    
    def validate(self,attributes):
        if attributes['password'] != attributes['password2']:
            raise serializers.ValidationError({"password":"password must match"})
        return attributes


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]