"""Recommendationsystem URL Configuration

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
from . import index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('admindashboard',index.admindashboard),
    path('page1',index.page1),
    path('aboutus',index.aboutus),
    path('register',index.register),
    path('ourteam',index.ourteam), 
    path('contact',index.contact),
    path('addquestion',index.addquestion),
    path('',index.login),
    path('doregister',index.doregister),
    path('calculate',index.calculate),
    path('recommend',index.recommend),
    path('unanswer',index.unanswer),
    path('subanswer',index.subanswer),
    path('subanswer1',index.subanswer1  ),
    
    path('dologin',index.dologin),
    path('viewuser',index.viewuser),
    path('logout',index.logout),
    #path('prevpred',index.prevpred),
    path('temp',index.temp),
    path('index',index.index),
    path('analyze',index.analyze),
    path('userhome',index.userhome,name="userhome"),
    path('adminhome',index.adminhome),
    path('doremove',index.doremove),
    path('viewpredicadmin',index.viewpredicadmin),
    path('chat', index.chat),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

