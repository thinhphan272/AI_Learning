#25 BÀI CODE PYTHON CƠ BẢN
#Bai1
"""
toan = float(input('Nhập điểm toán: '))
while toan < 0 or toan > 10:
    toan = float(input('Nhập điểm toán: '))

van = float(input('Nhập điểm văn: '))
while van < 0 or van > 10:
    van = float(input('Nhập điểm văn: '))

anh = float(input('Nhập điểm anh: '))
while anh < 0 or anh > 10:
    anh = float(input('Nhập điểm anh: '))

dtbinh = (toan + van + anh) / 3

if dtbinh >= 8:
    if (toan >= 8 or van >= 8) and (toan >= 6.5 and van >= 6.5 and anh >= 6.5):
        print('Học sinh giỏi!')
elif dtbinh  >= 6.5:
    if (toan >= 6.5 or van >= 6.5) and (toan >= 5 and van >= 5 and anh >= 5):
        print('Học sinh khá!')
elif dtbinh  >= 5:
    if (toan >= 5 or van >= 5) and (toan >= 3.5 and van >= 3.5 and anh >= 3.5):
        print('Học sinh trung bình!')
elif dtbinh  >= 3.5:
    if (toan >= 3.5 or van >= 3.5) and (toan >= 2 and van >= 2 and anh >= 2):
        print('Học sinh yếu!')
else:
    print('Học sinh kém!')

"""
import math

#Bai2
"""
thang = int(input('Nhập tháng: '))
nam = int(input('Nhập năm: '))

if (nam % 4 == 0 and nam % 100 != 0) or (nam % 400 == 0):
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print('Tháng {} có 31 ngày'.format(thang))
    elif thang == 2:
        print('Tháng {} có 29 ngày'.format(thang))
    else:
        print('Tháng {} có 30 ngày'.format(thang))

    print('Năm {} là năm nhuận'.format(nam))
else:
    if thang == 1 or thang == 3 or thang == 5 or thang == 7 or thang == 8 or thang == 10 or thang == 12:
        print('Tháng {} có 31 ngày'.format(thang))
    elif thang == 2:
        print('Tháng {} có 28 ngày'.format(thang))
    else:
        print('Tháng {} có 30 ngày'.format(thang))

    print('Năm {} không là năm nhuận'.format(nam))
"""

#Bai3
"""
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))

if a == 0:
    if b == 0 and c != 0:
        print('Phương trình vô nghiệm!')
    elif b == 0 and c == 0:
        print('Phương trình có vô số nghiệm!')
    else:
        print('Phương trình có nghiệm duy nhất x = {}'.format(-c / b))
else:
    delta = b**2 - 4*a*c
    if delta < 0:
        print("Phương trinh vô nghiệm!")
    elif delta == 0:
        print('Phương trình có 1 nghiệm kép x = (-b / 2a)\nx = {}'.format(-b / 2*a))
    else:
        print('Phương trình có 2 nghiệm phân biệt\nx1 = {}, x2 = {}'.format((-b + math.sqrt(delta)) / 2*a, (-b - math.sqrt(delta)) / 2*a))
"""

#Bai4
"""
a = float(input('Nhập a: '))
b = float(input('Nhập b: '))
c = float(input('Nhập c: '))

if a + b > c and a + c > b and b + c > a:
    print('3 cạnh a, b, c có thể cấu thành độ dài của 1 tam giác!')
else:
    print('3 cạnh a, b, c không thể cấu thành độ dài của 1 tam giác!')
"""

#Bai5
"""
i = 1
while i < 100:
    if i % 2 != 0:
        print(f'{i} ', end='')
    i += 1
"""

#Bai6
"""
i = 1
while i < 100:
    if i % 2 == 0 and i % 3 == 0:
        print(f'{i} ', end='')
    i += 1
"""

#Bai7
"""

"""
n = int(input('Nhập n: '))
tong = 0
for i in range(1, n + 1):
    tong += i

print('Tổng {}'.format(tong))






