
def tinhTien(a):
    if a < 10:
        return a * 12
    elif a >= 10 and a <= 99:
        return a * 10
    else:
        return a * 7

if __name__ == '__main__':
    soluong = int(input('Nhập số lượng mặt hàng: '))
    print(f"Tổng tiền phải trả cho {soluong} mặt hàng là: {tinhTien(soluong)}")