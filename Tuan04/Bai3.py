class ShoppingCart:
    def __init__(self):
        self.gio = {}
        
    def them_sanPham(self, sanPham, donGia):
        self.gio[sanPham] = donGia
        
    def xoa_sanPham(self, sanPham):
        self.gio.pop(sanPham)
        
    def xuat(self):
        for i, k in self.gio.items():
            print(i, "-" , k)
            
    def tong(self):
        s = 0
        for i in self.gio.values():
            s+=i
        return s
    
    
gio = ShoppingCart()
i = int(input('Nhập số lượng mặt hàng:'))

while(i > 0):
    gio.them_sanPham(input("Nhập mặt hàng: "), int(input("Nhập giá: ")))
    i-=1;
    
print("Mặt hàng hiện tại có trong giỏ")
gio.xuat();
print(f'Tổng tiền: {gio.tong()}')

xoa = input('Nhập măt hàng muốn xóa: ')
gio.xoa_sanPham(xoa)

print(f"Giỏ sau khi xóa {xoa}")
gio.xuat()

print(f'Tổng tiền: {gio.tong()}')