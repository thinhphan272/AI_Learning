import math
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

#Bai6 in ra dãy số chẵn chia hết cho 3 bé hơn 100
"""
i = 1
while i < 100:
    if i % 2 == 0 and i % 3 == 0:
        print(f'{i} ', end='')
    i += 1
"""

#Bai7 tính tổng từ 1 tới n
"""
n = int(input('Nhập n: '))
tong = 0
for i in range(1, n + 1):
    tong += i

print('Tổng {}'.format(tong))
"""
#Bai8 Đếm số ước của 1 số nhập từ bàn phím
"""
a = int(input('Nhập a: '))
dem = 0
i = 1
while i < a:
    if a % i == 0:
        dem += 1
        print(f'Ước = {i} ')
    i += 1

print(f'\nSo uoc cua {a} = {dem}')
"""

#Bai9 Nhập vào số nguyên dương a và b, in toàn bộ ước số chung của a và b
"""
a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

if a < b:
    so_nho = a
else:
    so_nho = b

i = 1
while i < so_nho + 1:
    if a % i == 0 and b % i == 0:
        print(f'Ước chung (a, b) = {i}')

    i += 1
"""

#Bài 10 Nhập vào số nguyên dương a, kiểm tra số nguyên tố
"""
def is_prime(a):
    if a <= 1:
        return False
    if a == 2:
        return True
    if a % 2 == 0:
        return False

    for i in range(3, int(a ** 0.5) + 1, 2):
        if a % i == 0:
            return False
    return True

a = int(input('Nhập a: '))

if is_prime(a):
    print(f'{a} là số nguyên tố!')
else:
    print(f'{a} không là số nguyên tố!')
"""

#Bai11 Nhập vào một dãy số, dừng khi người dùng nhập -1, in ra số lớn nhất và nhỏ nhất của dãy số vừa nhập
"""
solonnhat = -9999999999
sonhonhat = 9999999999

a = 0

while a != -1:
    a = int(input('Nhập a: '))
    if a != -1:
        if a > solonnhat:
            solonnhat = a

        if a < sonhonhat:
            sonhonhat = a

print(f'Số lơn nhất {solonnhat}\nSố nhỏ nhất {sonhonhat}')

"""

#Bai 12 Nhập vào số nguyên dương n tính tổng các chữ số của n
"""
n = int(input('Nhập n: '))

count = 0
while n > 0:
    n = n // 10
    count += 1

print(f'Số chữ số trong n là {count}')
"""

#Bai13 Nhập vào số nguyên dương n đếm xem n có bao nhiêu chữ số chẵn bao nhiêu chữ số lẻ
"""
n = input('Nhập n: ')

chuso_chan = 0
chuso_le = 0

for c in n:
    so = int(c)
    if so % 2 == 0:
        chuso_chan += 1
    else:
        chuso_le += 1

print(f'Tổng chữ số chẵn trong {n}: {chuso_chan}\nTổng chữ số lẻ trong {n}: {chuso_le}')
"""

#Bai14 Nhập vào số nguyên dương n tính tổng các chữ số của n
"""
n = int(input('Nhập n: '))

sum = 0
while n > 0:
    digit = n % 10
    sum += digit
    n //= 10

print(f'Tổng các chữ số trong số nguyên dương {n}: {sum}')
"""

#Bai15 Nhập vào 1 chuỗi in ra từ đầu tiên trong chuỗi:
""" Cách 1
string = input('Nhập chuỗi: ')

for c in string:
    print(f'{c}', end='')
    if c == ' ':
        break
"""

"""Cách 2
string = input('Nhập chuỗi: ')

for i in range(0, len(string)):
    if string[i] == ' ':
        first_word = string[0:i]
        print(f'Từ đầu tiên của chuỗi: {first_word}')
        break
"""

#Bai16 Nhập vào 1 chuỗi 3 số nguyên cách nhau bởi dấu phẩy, tính tổng 3 số nguyên đó
"""Cách 1
chuoi = input('Nhập chuỗi 3 số (cách bởi dấu phẩy): ')

new = chuoi.strip()
new2 = new.split(',')
new3 = list(map(int, new2))
total = 0
for i in new3:
    total += i

print(f'Tổng của 3 số là {total}')
"""

#Bai17 Nhập vào 1 chuỗi, đếm xem trong chuỗi có bao nhiêu ký tự in hoa, bao nhiêu ký tự in thường, bao nhiêu ký tự số
"""
string = input('Nhập chuỗi: ')

tong_chuHoa = 0
tong_chuThuong = 0
tong_chuSo = 0
for c in string:
    if c.isupper():
        tong_chuHoa += 1
    elif c.islower():
        tong_chuThuong += 1
    elif c.isdigit():
        tong_chuSo += 1
    else:
        continue


print(f'Tổng chữ hoa {tong_chuHoa}')
print(f'Tổng chữ thường {tong_chuThuong}')
print(f'Tổng chữ số {tong_chuSo}')
"""

#Bai18 Nhập vào một chuỗi, tách toàn bộ kí tự số ra rồi tính tổng của chúng
"""Cách 1
string = input('Nhập vào một chuỗi: ')

for i in string:
    if not i.isdigit():
        string = string.replace(i, ' ')

new1 = string.split()
new2 = list(map(int, new1))
total = 0
for i in new2:
    total += i

print(f'Tổng của các chữ số trong chuỗi {total}')
"""

"""Cách 2
string = input('Nhập chuỗi: ')

tong = 0
for i in string:
    if i in '0123456789':
        tong += int(i)

print(f'Tổng chữ số trong chuỗi: {tong}')
"""

#Bai19 Nhập vào 1 chuỗi kiểm tra chuỗi đó có phải là một chuỗi mật khẩu mạnh hay không
#(một chuỗi mật khẩu mạnh cần có ít nhất 1 kí tự đặc biệt, 1 ký tự in hoa, 1 chữ thường và độ dài phải lớn hơn 6
"""Cách 1
while True:
    string = input("Nhập mật khẩu: ")

    while len(string) < 6:
        print('Mật khẩu phải có tối thiểu 6 ký tự! Vui lòng nhập lại!')
        string = input("Nhập mật khẩu: ")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in string:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in '!@#$%^&*()':
            has_special = True


    if has_special and has_digit and has_lower and has_upper:
        print('Tạo mật khẩu thành công')
        break
    elif has_special and has_digit and has_lower:
        print('Mật khẩu phải có ít nhất 1 kí tự in hoa!')
    elif has_digit and has_lower and has_upper:
        print('Mật khẩu phải có ít nhất 1 kí tự đặc biệt!')
    elif has_lower and has_upper and has_special:
        print('Mật khẩu phải có ít nhất 1 kí tự số!')
    elif has_special and has_digit and has_upper:
        print('Mật khẩu phải có ít nhất 1 kí tự in thường!')
    elif has_special and has_digit:
        print('Mật khẩu phải có ít nhất 1 kí tự in thường, 1 kí tự in hoa!')
    elif has_special and has_lower:
        print('Mật khẩu phải có ít nhất 1 kí tự số, 1 kí tự in hoa!')
    elif has_special and has_upper:
        print('Mật khẩu phải có ít nhất 1 kí tự số, 1 kí tự in thường!')
    elif has_digit and has_lower:
        print('Mật khẩu phải có ít nhất 1 kí đặc biệt, 1 kí tự in hoa!')
    elif has_digit and has_upper:
        print('Mật khẩu phải có ít nhất 1 kí đặc biệt, 1 kí tự in thường!')
    elif has_lower and has_upper:
        print('Mật khẩu phải có ít nhất 1 kí đặc biệt, 1 kí tự số!')
    elif has_special:
        print('Mật khẩu phải có ít nhất 1 kí số, 1 kí tự in thường, 1 kí tự in hoa!')
    elif has_digit:
        print('Mật khẩu phải có ít nhất 1 kí đặc biệt, 1 kí tự in thường, 1 kí tự in hoa!')
    elif has_lower:
        print('Mật khẩu phải có ít nhất 1 đặc biệt, 1 kí tự số, 1 kí tự in hoa!')
    elif has_upper:
        print('Mật khẩu phải có ít nhất 1 đặc biệt, 1 kí tự số, 1 kí tự in thường!')
    print('Vui lòng nhập lại!')
"""

"""Cách 2
while True:
    string = input('Nhập mật khẩu: ')

    while len(string) < 6:
        print('Độ dài phải trên 6 kí tự! Vui lòng nhập lại!')
        string = input('Nhập mật khẩu:')

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for char in string:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif char in '!@#$%^&*()':
            has_special = True

    if has_upper and has_digit and has_lower and has_special:
        print("Tạo mật khẩu thành công!")
        break

    print('Mật khẩu yếu:')
    if not has_special:
        print('Mật khẩu phải có ít nhất 1 kí tự đặc biệt!')
    if not has_digit:
        print('Mật khẩu phải có ít nhất 1 kí tự số!')
    if not has_lower:
        print('Mật khẩu phải có ít nhất 1 kí tự in thường!')
    if not has_upper:
        print('Mật khẩu phải có ít nhất 1 kí tự in hoa!')
    print('Vui lòng nhập lại')
"""

#Bai20   Chuyển độ C sang độ F
"""
doC = int(input('Nhập độ C: '))
doF = (doC * 1.8) + 32
print(f'{doC}ºC = {doF}ºF')
"""

#Bai21 Kiểm tra n có phải là số chính phương hay không
"""
def check_cp(n):
    tmp = math.sqrt(n)
    if tmp * tmp == n:
        print(f'{n} là số chính phương!')
    else:
        print(f'{n} không là số chính phương!')


n = int(input('Nhập n: '))
check_cp(n)
"""

#Bai22 Tìm trong dãy số Fibonacci lớn nhất nhưng không vượt quá n
"""
def fibonacci(n):
    if n <= 1:
        return None
    fib1 = 0
    fib2 = 1
    while fib2 < n:
        fib_next = fib1 + fib2  # Tính số tiếp theo trước khi gán
        fib1 = fib2  # Dịch chuyển fib1
        fib2 = fib_next  # Dịch chuyển fib2

    return fib1


n = int(input('Nhập n: '))
result = fibonacci(n)

if result is not None:
    print(f'Số {result} là số fibonacci lớn nhất trong dãy từ 1 tới {n}')
else:
    print(f'Không có số fibonacci nào nhỏ hơn {n}')
"""

#Bai23 Nhập vào số nguyên dương n kiểm tra xem số đó có phải dạng 2 mũ k hay không
"""
n = int(input('Nhập n: '))
tmp = n
while n != 1:
    if n % 2 != 0:
        break
    n = n // 2

if n == 1:
    print(f'{tmp} là số thỏa 2^k')
else:
    print(f'{tmp} là số không thỏa 2^k')
"""

#Bai24 Nhập n vào tìm k sao cho S(k) lớn nhất nhưng nhỏ hơn n
#S(k) = 1 + 2 + 3 + ... + k
"""
n = int(input('Nhập n: '))
S = 0
k = 0

while S + (k + 1) < n:
    k += 1
    S += k

print(f'Số k lớn nhất thỏa mãn S(k) < n là {k}')
"""

#Bai25 Nhập vào một chuỗi. hãy đếm xem trong chuỗi có bao nhiêu từ
#(quy định là chuỗi không có ký tự đặc biệt, không có số, không có dấu câu, chỉ có kí tự chữ và khoảng trắng

"""
string = input('Nhập chuỗi: ')

new = string.strip()
new2 = new.split()

dem = 0

for word in new2:
    if word.isalpha():
        dem += 1

print(f'Số từ trong câu là: {dem}')

"""





