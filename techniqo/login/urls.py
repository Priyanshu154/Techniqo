from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('save', views.save),
    path('login', views.login),
    path('login_redirect', views.login_redirect),
    path('logout', views.logout),
]