"""ProyekSPK URL Configuration

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
from django.urls import path
from AHPSPK.views import *

urlpatterns = [
    path('', SHOWLaptop),
    path('admin/', admin.site.urls),
    path('index/', SHOWLaptop,name='index'),
    path('tambah/',TambahLaptop),
    path('index/ubah_data/<int:id_laptop>',ubah_data,name='ubah'),
    path('index/hapus_data/<int:id_laptop>',hapus_data,name='hapus'),
    path('hasil/',coba,name='hasil'),
    path('kriteria/',testing,name='test')
]