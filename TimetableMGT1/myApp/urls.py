from django.urls import path
from myApp import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.index,name='index'),
    path('home/', views.home, name="home"),
    path('register/', views.register, name="register"),
    path('profile/', views.profile, name="profile"),
    path('logout/',views.logout,name="logout"),
    path('about/', views.about, name="about"),
    path('managetimetable/', views.managetimetable, name="managetimetable"),
    path('viewtimetable/', views.viewtimetable, name="viewtimetable"),
    path('login/',views.login,name='login'),
    
]