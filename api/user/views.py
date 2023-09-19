from django.shortcuts import render
import random
from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import login,logout
import re
from .models import CustomUser
from .serializers import UserSerializer
# Create your views here.

def genrate_session_token(length):
    return ''.join(
        random.SystemRandom().choice(chr(i)for i in range(97,123)+[str(i)for i in range(0,10)]) for _ in range(length)
        )

@csrf_exempt 
def sigin(request):
    if not request.method =='POST':
        
        return JsonResponse({'error':'send the post request with valid parameters'})
    
    username = request.POST['email']
    password = request.POST['password']

    if not re.match("[a-zA-Z0-9+_.-]+@[a-zA-Z0-9.-]+$",username):
        return JsonResponse({"enater a valid email address"})
    if len(password)<3:
        return JsonResponse({"enater a password 6 characters"})
    

    UserModel = get_user_model()

    try:
        user = UserModel.objects.get(email=username)
        if user.check_password(password):
            usr_dict = UserModel.object.filter(email = username).values().first()
            usr_dict.pop('password')

            if user.session_token != "0":
                user.session_token = "0"
                user.save()
                return JsonResponse({'error':'perivios session exsists'})
            
            token = genrate_session_token()
            user.session_token = token
            user.save()
            login(request, user)
            return JsonResponse({'token': token, 'user': usr_dict})
        else:
            return JsonResponse({'error': 'Invalid password'})
    except UserModel.DoesNotExist:
        JsonResponse({'error': 'User name in valid'})


@csrf_exempt 
def singnout(request,id):
    UserModel = get_user_model()
    logout(request,id)
     
    try:
        user = UserModel.objects.get(pk =id)
        user.session_token = "0"
        user.save()
    except UserModel.DoesNotExist:
        return JsonResponse({"error":'invliad user id'})
    
    return JsonResponse({"success":'logout user'})


class UserViewSet(viewsets.ModelViewSet):
    permission_classes_by_action = {'create': [AllowAny]}

    queryset = CustomUser.objects.all().order_by('id')
    serializer_class = UserSerializer

    def get_permissions(self):
        try:
            return [permission() for permission in self.permission_classes_by_action[self.action]]

        except KeyError:
            return [permission() for permission in self.permission_classes]