"""
URL configuration for Nova_post_mashin project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

import user.views
from Nova_post_mashin import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', user.views.user_page),
    path('login/', user.views.Login_View.as_view()),
    path('logout/', user.views.logout_view),
    path('register/', user.views.Register_View.as_view()),

    path('parcel/', include('parcel.urls')),
    path('post_machines/', include('post_machin.urls')),
    path('', views.home, name='home'),
    path('user/login/', user.views.Login_View.as_view()),

]
