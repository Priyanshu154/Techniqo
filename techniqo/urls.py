"""techniqo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('candlepattern/',include('candlepattern.urls')),
    path('intrinsic/',include('intrinsic.urls')),
    path('news/', include('news.urls')),
    path('peers/', include('peers.urls')),
    path('technicals/', include('technicals.urls')),
    path('market/', include('market.urls')),
    path('stock/',include('stock.urls')),
    path('backtest/',include('backtest.urls')),
    path('scanner/',include('scanner.urls')),
    path('suggestion/', views.suggest),
    path('channel/',include('channel.urls')),
    path('opinion/',include('opinion.urls')),
    path('accounts/',include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)