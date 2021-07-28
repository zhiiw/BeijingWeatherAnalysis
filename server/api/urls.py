from . import views
from django.urls import include, path

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('forecast', views.forecast),
    path('everyday', views.everyday),
    path('send_comment', views.send_comment),
    path('load_comments', views.load_comments),
    path('lstm', views.lstm),
]