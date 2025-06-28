
from toanhoc import tamgiacvuong
from vatly import tinh_vantoc

print('1. Nhập 3 cạnh kiểm tra tam giác vuông.')
print('2. Nhập quãng đường (s), thời gian (t) tính vận tốc (v)')
print('0. Thoát chương trình')
choice = int(input('Nhập lựa chọn: '))

if choice == 1:
    a = float(input("Nhập cạnh a: "))
    b = float(input('Nhập cạnh b: '))
    c = float(input('Nhập cạnh c: '))
    check = tamgiacvuong(a, b, c)
    if check == True:
        print(f'Đây là tam giác vuông!')
    else:
        print(f'Đây không phải tam giác vuông')
else:
    s = float(input('Nhâp quãng đường '))
    t = float(input('Nhập thời gian: '))

    v = tinh_vantoc(s, t)
    print('Vận tốc = {}'.format(v))