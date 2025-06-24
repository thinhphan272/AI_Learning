import random

#Vidu1
"""
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if a > b:
    print(a)


if b > a:
    print(b)
"""

#Vidu2
"""
tenNV = input('Nhập họ tên nhân viên: ')
xepLoai = input('Nhập xếp loại (A1, A2, A3): ')
luong = 10000000
thuong = 3

if xepLoai == 'A1':
    thuong = thuong + 1


print(f'Nhân viên {tenNV} xếp loại {xepLoai} nên được thưởng 4 tháng lương là {luong * thuong} đồng.')
"""

#Vidu3 if elif else
"""
tenNV = input('Nhập họ tên nhân viên: ')
xepLoai = input('Nhập xếp loại (A1, A2, A3): ')
luong = 10000000

if xepLoai == 'A1':
    thuong = 4
elif xepLoai == 'A2':
    thuong = 3
else:
    thuong = 2

print(f'Nhân viên {tenNV} xếp loại {xepLoai} nên được thưởng 4 tháng lương là {luong * thuong} đồng.')
"""

#Vidu4
"""
maNV = input('Nhập mã nhân viên: ')
chucVu = input('Nhập chức vụ (CV1, CV2, CV3): ')
xepLoai = input('Nhập xếp loại (A1, A2, A3): ')

if chucVu == 'CV3':
    if xepLoai == 'A1':
        thuong = 2
    else:
        thuong = 1
else:
    if xepLoai == 'A1':
        thuong = 3
    elif xepLoai == 'A2':
        thuong = 2.5
    else:
        thuong = 2

print(f'{thuong} tháng')
"""

#Vidu5 Vòng lập While
"""
i = 1
while i < 6:
    print(f'i = {i}')
    if i == 3:
        break
    i += 1
"""

#Vidu6 Vòng lập while, Nhập vào xếp loại nhân viên
#Nếu không phải là A1, A2, A3 yêu cầu nhập lại
"""
ten = input('Nhập họ tên nhân viên: ')

xepLoai = input('Nhập xếp loại (A1, A2, A3): ')

while xepLoai != 'A1' and xepLoai != 'A2' and xepLoai != 'A3':
    xepLoai = input('Nhập xếp loại (A1, A2, A3): ')

print('Họ tên: {}\nXếp loại: {}'.format(ten, xepLoai))

"""

#Vidu7 Vòng lập For
"""
for i in range(1, 6):
    print('i =', i)

for x in 'I LOVE PYTHON':
    print('x =', x)

for x in ['A1', 'A2', 'A3']:
    print('x =', x)
"""

#Vidu8
"""
a = int(input('Nhập a: '))

while a >= 10:
    a = int(input('Nhập a: '))

for i in range(1, 11):
    print('{} x {} = {}'.format(a, i, a*i))
"""

#HAND-ONS
#Bai1
"""
a = int(input('Nhập số a: '))

if a % 2 == 0:
    print('{} là số chẵn'.format(a))
else:
    print('{} là số lẻ'.format(a))
"""

#Bai2
"""
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if a > b:
    print('{} lớn hơn {}'.format(a, b))
elif a < b:
    print('{} nhỏ hơn {}'.format(a, b))
else:
    print('{} bằng {}', format(a, b))
"""

#Bai3
"""
ten = input('Họ tên học sinh: ')
monhoc = input('Nhập tên môn học: ')

while monhoc != 'toán' and monhoc != 'văn' and monhoc != 'anh':
    print('Môn học chỉ có thể là (toán, văn, anh). Vui lòng nhập lại! ')
    monhoc = input('Nhập tên môn học: ')

diem = float(input('Nhập điểm: '))

if monhoc == 'toán':
    heso = 3
elif monhoc == 'văn':
    heso = 2
else:
    heso = 1

print('Họ tên: {}\nMôn học: {}\nĐiểm: {}\nĐiểm đã nhân hệ số: {}'.format(ten, monhoc, diem, diem*heso))
"""


#Trò chơi oẳn tù tì

def game():
    nguoi_choi = input('Chọn (Kéo, Búa, Bao): ')
    while nguoi_choi != 'Kéo' and nguoi_choi != 'Bao' and nguoi_choi != 'Búa':
        nguoi_choi = input('Chọn (Kéo, Búa, Bao): ')

    may_chon = random.choice(['Kéo', 'Búa', 'Bao'])

    if nguoi_choi == 'Kéo':
        if may_chon == 'Kéo':
            print('Kết quả: Hòa!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        elif may_chon == 'Búa':
            print('Kết quả: Bạn đã thua!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        else:
            print('Kết quả: Bạn đã thắng!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
    elif nguoi_choi == 'Búa':
        if may_chon == 'Kéo':
            print('Kết quả: Bạn đã thắng!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        elif may_chon == 'Búa':
            print('Kết quả: Hòa!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        else:
            print('Kết quả: Bạn đã thua!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
    else:
        if may_chon == 'Kéo':
            print('Kết quả: Bạn đã thua!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        elif may_chon == 'Búa':
            print('Kết quả: Bạn đã thắng!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')
        else:
            print('Kết quả: Hòa!')
            print(f'Bạn chọn: {nguoi_choi}\nMáy chọn: {may_chon}')

game()
ask = input('Bạn có muốn chơi tiếp không ?\nNhập <Có> để tiếp tục.\nNhấn Enter để dừng trò chơi\n')

while ask == 'Có':
    game()
    ask = input('Bạn có muốn chơi tiếp không ?\nNhập <Có> để tiếp tục.\nNhấn Enter để dừng trò chơi\n')
