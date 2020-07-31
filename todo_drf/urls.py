"""todo_drf URL Configuration

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
from django.urls import path, include

from api.views import homeView, contact_page, profile, hashtagTwitter

urlpatterns = [
    path('', homeView, name="homeView"),
    path('add', contact_page, name="contact_page"),
    
    path('hashtag-twitter', hashtagTwitter, name="hashtag-twitter"),
    path('profile', profile, name="profile"),

    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
