from django.urls import path
from . import views


urlpatterns = [
    path('signup/', views.SignupApiView.as_view(), name='signup'),
    path('login/', views.loginApiView.as_view(), name='login'),
    
]
