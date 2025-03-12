"""
URL configuration for mmn project.

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

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.urls import path
# from .views import home, get_data, create_data
from .views import trangchu_view
from django.contrib import admin
# from .views import api_get_ketqua
from .views import (
    trangchu_view, ketqua_view, monhoc_view, taikhoan_view, 
    thoikhoabieu_view, thongtinnguoidung_view, tinchi_view, vieccanlam_view, 
)
# TaiKhoanViewSet, QLMonHocViewSet, QLKetQuaHocViewSet, ViecCanLamViewSet, 
#     ThongTinNguoiDungViewSet, ThoiKhoaBieuViewSet, QLTinChiViewSet
# router = DefaultRouter()
# router.register(r'taikhoan', TaiKhoanViewSet)
# router.register(r'monhoc', QLMonHocViewSet)
# router.register(r'ketquahoc', QLKetQuaHocViewSet)
# router.register(r'vieccanlam', ViecCanLamViewSet)
# router.register(r'thongtinnguoidung', ThongTinNguoiDungViewSet)
# router.register(r'thoikhoabieu', ThoiKhoaBieuViewSet)
# router.register(r'tinchi', QLTinChiViewSet)

urlpatterns = [
    path('', trangchu_view, name='trangchu'),
    #  path('api/', include(router.urls)),
    path('ketqua/', ketqua_view, name='ketqua'),
    path('monhoc/', monhoc_view, name='monhoc'),
    path('taikhoan/', taikhoan_view, name='taikhoan'),
    path('thoikhoabieu/', thoikhoabieu_view, name='thoikhoabieu'),
    path('thongtinnguoidung/', thongtinnguoidung_view, name='thongtinnguoidung'),
    path('tinchi/', tinchi_view, name='tinchi'),
    path('vieccanlam/', vieccanlam_view, name='vieccanlam'),
    path('admin/', admin.site.urls),
    # path('api/<str:collection_name>/', get_data, name='get_data'),
    # path('api/<str:collection_name>/create/', create_data, name='create_data'),
    # path('api/ketqua/', api_get_ketqua, name='api_get_ketqua'),
   
]