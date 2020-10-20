from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('change/', views.change_view),
    path('forgot/', views.forgot_view),
]
