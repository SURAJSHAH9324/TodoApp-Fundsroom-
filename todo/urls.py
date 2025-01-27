"""
URL configuration for todo project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
# from django.contrib import admin
# from django.urls import path
# from todoapp.views import home,add,deleteItem
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', home),
#     path('add/', add,name="add"),
#     path('delete/<int:todo_id>/', deleteItem,name="delete"),
# ]
from django.contrib import admin
from django.urls import path
from todoapp.views import home, add, deleteItem, register, user_login, user_logout

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('add/', add, name='add'),
    path('delete/<int:id>/', deleteItem, name='delete'),
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
