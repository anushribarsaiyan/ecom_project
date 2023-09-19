from rest_framework import routers
from django.urls import path ,include
from .import views

router = routers.DefaultRouter()
router.register(r'',views.UserViewSet)

urlpatterns = [
    path('login/',views.sigin, name = 'sigin'),
    path('logout/<int:id>/', views.singnout, name='signout'),
    path('',include(router.urls))
   
]