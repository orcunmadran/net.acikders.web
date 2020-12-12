"""website URL Configuration

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
from django.urls import path
#pages app
from pages import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('test/', views.test_view, name='test'),
    path('schema/', views.sema_view, name='schema'),
    path('metaform/', views.form_view, name='metaform'),
    path('metadata/', views.metadata_view, name='metadata'),
    path('basic/', views.basic_view, name='basic'),
    path('admin/', admin.site.urls),
]

# Admin Page Setup
admin.site.site_header = 'Açık Ders Yönetim Paneli'
admin.site.site_title = 'Açık Ders Yönetim Paneli'
admin.site.index_title = 'Yönetim Paneli Uygulamaları'
