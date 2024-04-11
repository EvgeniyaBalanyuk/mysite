"""
URL configuration for mysite project.

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
from django.urls import path

from demo.views import demo, cur_time, index, summa, temp, pagi, new_car, list_car, create_person, list_person

urlpatterns = [
    path("admin/", admin.site.urls),
    path("site/", demo, name="site88"),
    path("time/", cur_time, name="cur_time"),
    path("", index, name="main"),
    path("summa/<int:a>/<int:b>", summa),
    path("temp/", temp, name="temp"),
    path("pagi/", pagi, name="pagi"),
    path("car/", new_car, name="car"),
    path("list_car/", list_car, name="list_car"),
    path("new_person/", create_person, name="create_person"),
    path("list_person/", list_person, name="list_person"),
]
