from djongo import models

class TaiKhoan(models.Model):
    id = models.CharField(max_length=50, primary_key=True, db_column="Id")  # Trùng với trường "Id" trong MongoDB
    tai_khoan = models.CharField(max_length=100, db_column="TaiKhoan")  # Tên tài khoản
    mat_khau = models.CharField(max_length=255, db_column="MatKhau")  # Mật khẩu (có thể hash nếu cần)
    quyen = models.BooleanField(db_column="Quyen")  # True/False cho quyền
    ma_nguoi_dung = models.CharField(max_length=50, db_column="MaNguoiDung")  # Liên kết với người dùng

    def __str__(self):
        return self.tai_khoan

    class Meta:
        db_table = "TaiKhoan"  # Trùng với tên collection trong MongoDB


class QLMonHoc(models.Model):
    
    MaNguoiDung = models.CharField(max_length=50)
    IDMonHoc = models.CharField(max_length=50, unique=True)
    MaMon = models.CharField(max_length=50)
    TenMon = models.CharField(max_length=255)
    ThoiGianBatDau = models.DateTimeField()
    ThoiGianKetThuc = models.DateTimeField()
    GiangVien = models.CharField(max_length=255)

    def __str__(self):
        return self.TenMon

    class Meta:
        db_table = "QLMonHoc"
        

class QLKetQuaHoc(models.Model):
   
    MaNguoiDung = models.CharField(max_length=20)
    MaKetQuaHoc = models.CharField(max_length=20, unique=True)
    MaMon = models.CharField(max_length=20)
    TenMon = models.CharField(max_length=100)
    DiemHe10 = models.FloatField()
    DiemHe4 = models.FloatField()

    def __str__(self):
        return f"{self.MaNguoiDung} - {self.MaMon} - {self.DiemHe10}"
    
    class Meta:
        db_table = "QLKetQuaHoc"
        
        


class ViecCanLam(models.Model):
    MaNguoiDung = models.CharField(max_length=50, db_column="MaNguoiDung")
    MaVCL = models.CharField(max_length=50, unique=True, db_column="MaVCL")
    NhacNho = models.TextField(db_column="NhacNho")
    GhiChu = models.TextField(db_column="GhiChu", null=True, blank=True)
    ThoiHan = models.DateTimeField(db_column="ThoiHan")
    TenMon = models.CharField(max_length=255, db_column="TenMon")

    def __str__(self):
        return self.NhacNho

    class Meta:
        db_table = "ViecCanLam"


class ThongTinNguoiDung(models.Model):
    MaNguoiDung = models.CharField(max_length=50, unique=True, db_column="MaNguoiDung")
    TaiKhoan = models.CharField(max_length=100, db_column="TaiKhoan")
    MatKhau = models.CharField(max_length=255, db_column="MatKhau")
    Ten = models.CharField(max_length=255, db_column="Ten")
    Email = models.EmailField(db_column="Email")
    SDT = models.CharField(max_length=15, db_column="SDT")

    def __str__(self):
        return self.Ten

    class Meta:
        db_table = "ThongTinNguoiDung"


class ThoiKhoaBieu(models.Model):
    MaNguoiDung = models.CharField(max_length=50, db_column="MaNguoiDung")
    MaTKB = models.CharField(max_length=50, unique=True, db_column="MaTKB")
    MonHoc = models.CharField(max_length=255, db_column="MonHoc")
    Thu = models.CharField(max_length=50, db_column="Thu")
    ThoiGianHoc = models.CharField(max_length=50, db_column="ThoiGianHoc")

    def __str__(self):
        return f"{self.MonHoc} - {self.Thu}"

    class Meta:
        db_table = "ThoiKhoaBieu"


class QLTinChi(models.Model):
    MaNguoiDung = models.CharField(max_length=50, db_column="MaNguoiDung")
    IDTinChi = models.CharField(max_length=50, unique=True, db_column="IDTinChi")
    MaMon = models.CharField(max_length=50, db_column="MaMon")
    SoChiDaDat = models.IntegerField(db_column="SoChiDaDat")
    SoChiNo = models.IntegerField(db_column="SoChiNo")
    TongTinChi = models.IntegerField(db_column="TongTinChi")

    def __str__(self):
        return f"{self.MaNguoiDung} - {self.MaMon} ({self.SoChiDaDat}/{self.TongTinChi} tín chỉ)"

    class Meta:
        db_table = "QLTinChi"
