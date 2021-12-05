"""ApplicationServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # The default path is the home page
    path('', views.home, name="home"),

    # Link the html page rendering functions to the correct paths
    path('linearChoice', views.linearChoice, name="linearChoice"),
    path('linregress', views.linregress, name="linregress"),
    path('linearResults', views.linearResults, name="linearResults"),
    path('multiregress', views.multiregress, name="multiregress"),
    path('multiResults', views.multiResults, name="multiResults"),
    path('polyregress', views.polyregress, name="polyregress"),
    path('polyResults', views.polyResults, name="polyResults"),
    path('neuraln', views.neuraln, name="neuraln"),
    path('neuralResults', views.neuralResults, name="neuralResults")
]
