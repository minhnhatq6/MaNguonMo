from django.shortcuts import render
from .models import TaiKhoan, QLMonHoc,QLKetQuaHoc, ViecCanLam, ThoiKhoaBieu, ThongTinNguoiDung, QLTinChi
from rest_framework import viewsets

from pymongo import MongoClient
from rest_framework.response import Response
from rest_framework.decorators import api_view
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


##API
collections = {
    "taikhoan": db['TaiKhoan'],
    "monhoc": db['QLMonHoc'],
    "ketqua": db['QLKetQuaHoc'],
    "vieccanlam": db['ViecCanLam'],
    "thongtinnguoidung": db['ThongTinNguoiDung'],
    "thoikhoabieu": db['ThoiKhoaBieu'],
    "tinchi": db['QLTinChi']
}

serializers_map = {
    "taikhoan": TaiKhoanSerializer,
    "monhoc": QLMonHocSerializer,
    "ketqua": QLKetQuaHocSerializer,
    "vieccanlam": ViecCanLamSerializer,
    "thongtinnguoidung": ThongTinNguoiDungSerializer,
    "thoikhoabieu": ThoiKhoaBieuSerializer,
    "tinchi": QLTinChiSerializer
}

# 🔹 Hiển thị dữ liệu từ MongoDB trên giao diện
def get_data_view(request, collection_name):
    if collection_name in collections:
        data = list(collections[collection_name].find({}, {"_id": 0}))
        return render(request, f'qlht/{collection_name}.html', {collection_name: data})
    return JsonResponse({"error": "Collection not found"}, status=404)

# 🔹 API lấy dữ liệu
@api_view(['GET'])
def get_data(request, collection_name):
    if collection_name in collections:
        data = list(collections[collection_name].find({}, {"_id": 0}))
        return Response(data)
    return Response({"error": "Collection not found"}, status=404)

# 🔹 API tạo dữ liệu
@api_view(['POST'])
def create_data(request, collection_name):
    if collection_name in collections:
        collections[collection_name].insert_one(request.data)
        return Response({"message": f"{collection_name} record created successfully"}, status=201)
    return Response({"error": "Collection not found"}, status=404)

# 🔹 API lấy dữ liệu từ collection "ketqua"
def api_get_ketqua(request):
    ketqua_list = list(collections["ketqua"].find({}, {"_id": 0}))
    return JsonResponse({"data": ketqua_list}, safe=False)

# 🔹 API mặc định
def home(request):
    return JsonResponse({"message": "Welcome to the MongoDB Django API!"})

# 🔹 ViewSet cho các bảng (MongoDB không hỗ trợ ModelViewSet nên phải dùng custom ViewSet)
class GenericMongoViewSet(viewsets.ViewSet):
    collection_name = None  # Collection tương ứng với mỗi ViewSet

    def list(self, request):
        if self.collection_name in collections:
            data = list(collections[self.collection_name].find({}, {"_id": 0}))
            return Response(data)
        return Response({"error": "Collection not found"}, status=404)

    def create(self, request):
        if self.collection_name in collections:
            collections[self.collection_name].insert_one(request.data)
            return Response({"message": "Record created successfully"}, status=201)
        return Response({"error": "Collection not found"}, status=404)

# 🔹 Các ViewSet cho từng bảng
class TaiKhoanViewSet(GenericMongoViewSet):
    collection_name = "taikhoan"

class QLMonHocViewSet(GenericMongoViewSet):
    collection_name = "monhoc"

class QLKetQuaHocViewSet(GenericMongoViewSet):
    collection_name = "ketqua"

class ViecCanLamViewSet(GenericMongoViewSet):
    collection_name = "vieccanlam"

class ThongTinNguoiDungViewSet(GenericMongoViewSet):
    collection_name = "thongtinnguoidung"

class ThoiKhoaBieuViewSet(GenericMongoViewSet):
    collection_name = "thoikhoabieu"

class QLTinChiViewSet(GenericMongoViewSet):
    collection_name = "tinchi"