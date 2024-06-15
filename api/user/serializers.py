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

# from django.contrib.auth.handlers import make_password
from rest_framework.decorators import authentication_classes, permission_classes
from .models import CustomUser




class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            instance.set_password(instance,attr, value)
        instance.save()
        return instance
    
    class Meta:
        model = CustomUser
        extra_kwargs = {'password':{'write_only':True}}
        fields =('name', 'email', 'password', 'phone', 'gender','is_staff', 'is_superuser')

