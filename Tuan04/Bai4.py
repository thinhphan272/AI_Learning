class SanPham:
    def __init__(self, soluong, gia, tenSP, solgTon, giaThongthuong):
        self.soluong = soluong
        self.gia = gia
        self.tenSP = tenSP
        self.solgTon = solgTon
        self.giaThongthuong = giaThongthuong
        

    def get_price(self):
        if self.soluong < 10:
            return self.giaThongthuong * self.soluong
        elif self.soluong >= 10 and self.soluong <= 99:
            return self.giaThongthuong * self.soluong * 0.9
        elif self.soluong >= 100:
            return self.giaThongthuong * self.soluong * 1.2
        
    def make_purchase(self):
        if self.soluong > self.solgTon:
            print(f"Không đủ hàng trong kho. Chỉ còn {self.solgTon} sản phẩm.")
            return False
        self.solgTon -= self.soluong
        print(f"Đã mua {self.soluong} {self.tenSP}. Còn lại {self.solgTon} trong kho.")


product = SanPham(5, 1.5, "Sữa", 150, 1.5)

print(f"Tổng chi phí cho {product.soluong} sản phẩm: ${product.get_price():.2f}")

product.make_purchase()
    