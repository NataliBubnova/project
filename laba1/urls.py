"""
URL configuration for laba1 project.

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
from django.contrib.auth.views import LogoutView
from django.urls import path, reverse_lazy

from my_project import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_index, name="home"),
    path('info/', views.show_info, name="info"),
    path('showcar/<int:id_car>/', views.show_car, name='car'),
    path('showcar/<int:id_car>/updatechar/', views.update_character, name='update_characteristic'),

    path('user_logout', views.logout_user, name='logout_user'),
    path('employeeView/<str:name_department>/', views.show_brands_odDepartment, name='cars_brand'),
    path('employeeViews/<str:name_department>/<str:name_of_brand>/', views.show_carsFromBrands, name='cars_fromBrands'),
]
