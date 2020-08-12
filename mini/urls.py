"""mini URL Configuration

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
import mini.views as views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', views.main),
<<<<<<< HEAD
    path('board/', views.board),
    path('list/', views.list),
=======

    path('board/', views.board),
    path('list/', views.list),
<<<<<<< HEAD

=======
=======
<<<<<<< HEAD
    path('board/', views.board),
    path('list/', views.list),
=======
>>>>>>> ed86002b9fb9519619df34a38a96e484454a41da
>>>>>>> 76fdf9f7b992771c8939a2c633142f358b3761ae
>>>>>>> 0ec69d05943c5cb93a7b8f76b74d4526e06c7879
    path('phone_data/', views.phone_data),

]
