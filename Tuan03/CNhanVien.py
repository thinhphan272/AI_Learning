class NhanVien:
    
       
        
    def inputInfo(self):
        self.TenNV = input('Nhập họ tên nhân viên: ')
        self.Tuoi = int(input('Nhập tuổi: '))
        self.DiaChi = input('Nhập địa chỉ: ')
        self.TienLg = float(input('Nhập tiền lương: '))
        self.TongHLam = float(input('Nhập tổng giờ làm: '))
        
    def printInfo(self):
        print(f"Nhân viên {self.TenNV} - {self.Tuoi} tuổi\n")
        print(f"Địa chỉ: {self.DiaChi}\n")
        print(f"Tiền lương: {self.TienLg} - Tổng giờ làm: {self.TongHLam}")
        
    def tinhLuong(self):
        if self.TongHLam >= 200:
            return self.TienLg + (self.TienLg * 0.2)
        elif  self.TongHLam < 200 and self.TongHLam >= 100:
            return self.TienLg + (self.TienLg * 0,1)
        else:
            return self.TienLg