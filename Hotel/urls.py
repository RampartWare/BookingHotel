from django.urls import path
from Hotel import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('login',views.login),
    path('register',views.register),
    path('mybooking',views.mybooking),
    path('recorded',views.recorded)
]