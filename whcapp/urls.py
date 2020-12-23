from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('allpostcommunity', views.allpostcommunity),
    path('login', views.login),
    path('register', views.register),
    # path('logout', views.logout),
    path('profile_edit', views.profile_edit),
    path('profile_view', views.profile_view),
    
    
]
