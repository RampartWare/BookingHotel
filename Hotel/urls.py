from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('mybooking',views.mybooking),
    path('recorded',views.recorded),
    path('about', views.about),
    path('hotelcoco', views.hotelcoco),
    path('hotelamphwa', views.hotelamphwa),
    path('hotelarong', views.hotelarong),
    path('hotelthegret', views.hotelthegret),
    path('hotelroyal', views.hotelroyal)
]