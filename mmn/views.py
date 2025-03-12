from django.shortcuts import render
from .models import TaiKhoan, QLMonHoc,QLKetQuaHoc, ViecCanLam, ThoiKhoaBieu, ThongTinNguoiDung, QLTinChi
from rest_framework import viewsets

from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.decorators import api_view
from pymongo import MongoClient
from .serializers import *
from django.http import JsonResponse
# Kết nối đến MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['QLHT']  # Tên database trong MongoDB
QLKetQuaHoc = db['QLKetQuaHoc']  # Tên collection
TaiKhoan = db['TaiKhoan']
QLMonHoc = db['QLMonHoc']

ViecCanLam = db['ViecCanLam']
ThongTinNguoiDung = db['ThongTinNguoiDung']
ThoiKhoaBieu = db['ThoiKhoaBieu']
QLTinChi = db['QLTinChi']

def trangchu_view(request):
    return render(request, 'qlht/trangchu.html')  # Hiển thị trang chủ


def taikhoan_view(request):
    taikhoans = list(TaiKhoan.find({}, {"_id": 0}))
    return render(request, 'qlht/taikhoan.html', {'taikhoan': taikhoans})

def monhoc_view(request):
    monhocs = list(QLMonHoc.find({}, {"_id": 0}))
    return render(request, 'qlht/monhoc.html', {'monhoc': monhocs})

def ketqua_view(request):
    ketquas = list(QLKetQuaHoc.find({}, {"_id": 0}))  # Lấy tất cả dữ liệu, bỏ _id để tránh lỗi hiển thị
    return render(request, 'qlht/ketqua.html', {'ketqua': ketquas})

def vieccanlam_view(request):
    vieccanlam_list = list(ViecCanLam.find({}, {"_id": 0}))
    return render(request, 'qlht/vieccanlam.html', {'vieccanlam': vieccanlam_list})

def thongtinnguoidung_view(request):
    nguoidung_list = list(ThongTinNguoiDung.find({}, {"_id": 0}))
    return render(request, 'qlht/thongtinnguoidung.html', {'nguoidung': nguoidung_list})

def thoikhoabieu_view(request):
    tkb_list = list(ThoiKhoaBieu.find({}, {"_id": 0}))
    return render(request, 'qlht/thoikhoabieu.html', {'thoikhoabieu': tkb_list})

def tinchi_view(request):
    tinchi_list = list(QLTinChi.find({}, {"_id": 0}))
    return render(request, 'qlht/tinchi.html', {'tinchi': tinchi_list})


# ##API
# collections = {
#     "taikhoan": db['TaiKhoan'],
#     "monhoc": db['QLMonHoc'],
#     "ketqua": db['QLKetQuaHoc'],
#     "vieccanlam": db['ViecCanLam'],
#     "thongtinnguoidung": db['ThongTinNguoiDung'],
#     "thoikhoabieu": db['ThoiKhoaBieu'],
#     "tinchi": db['QLTinChi']
# }

# serializers_map = {
#     "taikhoan": TaiKhoanSerializer,
#     "monhoc": QLMonHocSerializer,
#     "ketqua": QLKetQuaHocSerializer,
#     "vieccanlam": ViecCanLamSerializer,
#     "thongtinnguoidung": ThongTinNguoiDungSerializer,
#     "thoikhoabieu": ThoiKhoaBieuSerializer,
#     "tinchi": QLTinChiSerializer
# }

# @api_view(['GET'])
# def get_data(request, collection_name):
#     if collection_name in collections:
#         data = list(collections[collection_name].find({}, {"_id": 0}))
#         serializer_class = serializers_map.get(collection_name)
#         serializer = serializer_class(data, many=True)
#         return Response(serializer.data)
#     return Response({"error": "Collection not found"}, status=404)

# @api_view(['POST'])
# def create_data(request, collection_name):
#     if collection_name in collections:
#         collections[collection_name].insert_one(request.data)
#         return Response({"message": f"{collection_name} record created successfully"}, status=201)
#     return Response({"error": "Collection not found"}, status=404)


# def home(request):
#     return JsonResponse({"message": "Welcome to the MongoDB Django API!"})

# def api_get_ketqua(request):
#     ketqua_list = list(QLKetQuaHoc.find({}, {"_id": 0}))  # Lấy tất cả dữ liệu, bỏ ObjectId
#     return JsonResponse({"data": ketqua_list}, safe=False)


# from rest_framework import viewsets

# from .serializers import (
#     TaiKhoanSerializer, QLMonHocSerializer, QLKetQuaHocSerializer,
#     ViecCanLamSerializer, ThongTinNguoiDungSerializer, ThoiKhoaBieuSerializer, QLTinChiSerializer
# )


# # Các ViewSet sử dụng MongoDB
# class TaiKhoanViewSet(viewsets.ViewSet):
#     def list(self, request):
#         taikhoans = list(db['TaiKhoan'].find({}, {"_id": 0}))
#         serializer = TaiKhoanSerializer(taikhoans, many=True)
#         return Response(serializer.data)

# class QLMonHocViewSet(viewsets.ViewSet):
#     def list(self, request):
#         monhocs = list(db['QLMonHoc'].find({}, {"_id": 0}))
#         serializer = QLMonHocSerializer(monhocs, many=True)
#         return Response(serializer.data)

# class QLKetQuaHocViewSet(viewsets.ViewSet):
#     def list(self, request):
#         ketquas = list(db['QLKetQuaHoc'].find({}, {"_id": 0}))
#         serializer = QLKetQuaHocSerializer(ketquas, many=True)
#         return Response(serializer.data)

# class ViecCanLamViewSet(viewsets.ViewSet):
#     def list(self, request):
#         vieccanlam_list = list(db['ViecCanLam'].find({}, {"_id": 0}))
#         serializer = ViecCanLamSerializer(vieccanlam_list, many=True)
#         return Response(serializer.data)

# class ThongTinNguoiDungViewSet(viewsets.ViewSet):
#     def list(self, request):
#         nguoidung_list = list(db['ThongTinNguoiDung'].find({}, {"_id": 0}))
#         serializer = ThongTinNguoiDungSerializer(nguoidung_list, many=True)
#         return Response(serializer.data)

# class ThoiKhoaBieuViewSet(viewsets.ViewSet):
#     def list(self, request):
#         tkb_list = list(db['ThoiKhoaBieu'].find({}, {"_id": 0}))
#         serializer = ThoiKhoaBieuSerializer(tkb_list, many=True)
#         return Response(serializer.data)

# class QLTinChiViewSet(viewsets.ViewSet):
#     def list(self, request):
#         tinchi_list = list(db['QLTinChi'].find({}, {"_id": 0}))
#         serializer = QLTinChiSerializer(tinchi_list, many=True)
#         return Response(serializer.data)