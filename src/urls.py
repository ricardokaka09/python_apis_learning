from django.urls import path
from . import views
from rest_framework.authtoken import views as drf_views
from rest_framework import routers
route = routers.SimpleRouter()



urlpatterns = [
    path('hi/', views.say_hello),
    path('auth', drf_views.obtain_auth_token, name='auth')
]
