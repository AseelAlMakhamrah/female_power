from django.urls import path 
from . import views

urlpatterns = [
    path('',views.index),
    path('allpostcommunity', views.allpostcommunity),
    path('login', views.login),
    path('logout', views.logout),
    path('register',views.register),
    path('show', views.show),
    path('profile_edit', views.profile_edit),
    path('profile_view', views.profile_view),
    path('save_profile_changes', views.save_profile_changes),
    
    

]