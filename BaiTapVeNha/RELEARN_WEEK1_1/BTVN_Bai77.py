soluong = int(input('Nhập số lương mặt hàng: '))

if soluong < 10:
    print(f'Tổng chi phí: {soluong * 12}$')
elif soluong >= 10 and soluong <= 99:
    print(f'Tổng chi phí: {soluong * 10}$')
else:
    print(f'Tổng chi phí: {soluong * 7}$')