from rest_framework import serializers
from .models import CustomUser

class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only = True)

    class Meta:
        model  = CustomUser
        fields = ['email', 'password','first_name', 'last_name']


    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data.get('first_name',''),
            last_name = validated_data.get('last_name','')
        )
        return user