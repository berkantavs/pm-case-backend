"""
URL configuration for djangobackend project.

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
from user.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', register_user, name='register_user'),
    path('login', login_user, name='login_user'),
    path('units', get_units, name='get_units'),
    path('units/<int:birim_id>/', get_unit_by_id, name='get_unit_by_id'),
    path('add_unit', create_unit, name='create_unit'),
    path('delete_unit/<int:pk>/', delete_unit, name='delete_unit'),
    path('update_unit/<int:birim_id>/', update_unit, name='update_unit'),
    path('users', get_users, name='get_users'),
    path('users/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    path('add_user', create_user, name='create_user'),
    path('delete_user/<int:user_id>/', delete_user, name='delete_user'),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
    path('employees', get_personels, name='get_personels'),
    path('add_employee', create_personel, name='create_personel'),
    path('delete_employee/<int:personel_id>/', delete_personel, name='delete_personel'),
    path('employees/<int:personel_id>/', get_employee_by_id, name='get_employee_by_id'),
    path('update_employee/<int:personel_id>/', update_employee, name='update_employee'),
]
