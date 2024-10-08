"""firstdjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include

from first import views

urlpatterns = [
    #관리 용이하게 하기 위해 루트 디렉토리의 urls.py에는 한줄만 추가하도록
    path('first/', include('first.urls')),
    path('second/', include('second.urls')),
    path('third/', include('third.urls')),
    path('admin/', admin.site.urls),
]
