
def tinhTien(SoLuong):
    if SoLuong < 10:
        return 12
    elif SoLuong >= 10 and SoLuong <= 99:
        return 10
    else:
        return 7


n = int(input('Nhập số lượng sản phẩm: '))

sum = n * tinhTien(n)
print(f'Tổng tiền {sum}')