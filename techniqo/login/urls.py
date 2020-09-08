from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('save', views.save),
    path('login', views.login),
    path('login_redirect', views.login_redirect),
    path('logout', views.logout),
    path('forgot_redirect', views.forgot_redirect),
    path('forgot', views.forgot),
    path('reset_redirect', views.reset_redirect),
    path('reset', views.reset),
]