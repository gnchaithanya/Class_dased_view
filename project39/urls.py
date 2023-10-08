"""
URL configuration for project39 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    path('Fbv_view/',Fbv_view,name='Fbv_view'),
    path('Cbv_view/',Cbv_view.as_view(),name='Cbv_view'),



    path('fbv_render/',fbv_render,name='fbv_render'),
    path('cbv_render/',cbv_render.as_view(),name='cbv_render'),



    path('insert_fbv/',insert_fbv,name='insert_fbv'),
    path('insert_cbv/',insert_cbv.as_view(),name='insert_cbv'),


    path('cbv_temp/',cbv_temp.as_view(),name='cbv_temp')



















]
