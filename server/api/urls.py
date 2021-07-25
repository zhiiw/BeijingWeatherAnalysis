from . import views
from django.urls import include, path

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('trial', views.trial),
    path('gettemp', views.get_temp),
    path('forecast_Beijing', views.forecast_Beijing),
    path('Beijing_everyday', views.Beijing_everyday),
    path('send', views.send),
]