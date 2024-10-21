from rest_framework import serializers
from .models import User


class Userserirializer(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)
    class Meta:
        model=User
        fields=fields = ["id", "email", "username", "password", "password2",'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }


    def validate(self,data):
        password=data.get('password')
        password2=data.get('password2')

        if password !=password2:
            raise serializers.ValidationError
        return data
            
        
    def create(self, validated_data):
        password = validated_data.pop('password')
        validated_data.pop('password2')  # Remove password2 as it's not needed
        user = User(**validated_data)  # Create user instance without saving
        user.set_password(password)  # Hash the password
        user.save()  # Save the user
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    email=serializers.EmailField(max_length=50)
    class Meta:
        model=User
        fields=['email','password']


class UserprofileSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['email','username']