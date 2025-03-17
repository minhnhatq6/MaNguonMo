from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    trangchu_view, ketqua_view, monhoc_view, taikhoan_view, 
    thoikhoabieu_view, thongtinnguoidung_view, tinchi_view, vieccanlam_view, 
    home, get_data, create_data, api_get_ketqua,
    TaiKhoanViewSet, QLMonHocViewSet, QLKetQuaHocViewSet, ViecCanLamViewSet, 
    ThongTinNguoiDungViewSet, ThoiKhoaBieuViewSet, QLTinChiViewSet
)

# Khai báo router cho ViewSet API
router = DefaultRouter()
router.register(r'taikhoan', TaiKhoanViewSet, basename='taikhoan')
router.register(r'monhoc', QLMonHocViewSet, basename='monhoc')
router.register(r'ketquahoc', QLKetQuaHocViewSet, basename='ketquahoc')
router.register(r'vieccanlam', ViecCanLamViewSet, basename='vieccanlam')
router.register(r'thongtinnguoidung', ThongTinNguoiDungViewSet, basename='thongtinnguoidung')
router.register(r'thoikhoabieu', ThoiKhoaBieuViewSet, basename='thoikhoabieu')
router.register(r'tinchi', QLTinChiViewSet, basename='tinchi')

# Khai báo URL patterns
urlpatterns = [
    # Trang giao diện
    path('', trangchu_view, name='trangchu'),
    path('ketqua/', ketqua_view, name='ketqua'),
    path('monhoc/', monhoc_view, name='monhoc'),
    path('taikhoan/', taikhoan_view, name='taikhoan'),
    path('thoikhoabieu/', thoikhoabieu_view, name='thoikhoabieu'),
    path('thongtinnguoidung/', thongtinnguoidung_view, name='thongtinnguoidung'),
    path('tinchi/', tinchi_view, name='tinchi'),
    path('vieccanlam/', vieccanlam_view, name='vieccanlam'),

    # Django Admin
    path('admin/', admin.site.urls),

    # API
    path('api/', include(router.urls)),  # API dùng ViewSet
    path('api/<str:collection_name>/', get_data, name='get_data'),
    path('api/<str:collection_name>/create/', create_data, name='create_data'),
    path('api/ketqua/', api_get_ketqua, name='api_get_ketqua'),
]
