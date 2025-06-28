#Vidu1
"""
def upper(string):
    string = string.upper()
    return string


string = input('Nhập tên: ')
string = upper(string)
print(string)
"""

#Vidu2
"""
def noi_chuoi(chuoi1, chuoi2, chuoi3 = "_"): 
    newstring = chuoi1 + chuoi2 + chuoi3
    return newstring


string = noi_chuoi(chuoi1='abc',chuoi2='xyz',chuoi3='*') #Mặc định là _ nhưng nếu truyền vào * thì sẽ thành *
print(string)
"""
#HÀM Lambda
#có thể nhập vào nhiều tham số nhưng chỉ có một biểu thức tính toán
#Vidu3
"""
x = lambda a: a + 10

ket_qua = x(5)
print(ket_qua)
"""

"""
x = lambda a,b: a + b

ket_qua = x(5, 1)
print(ket_qua)
"""

#Handson
#Bai1
"""
def binh_phuong_float(a):
    new = a**2
    return new

q = float(input('Nhập vào 1 số tính bình phương: '))

print(f'{binh_phuong_float(q)}')
"""

#Bai2
"""
def thuong_nhanvien(capbac, luong, sex='F'):
    if sex == 'F':
        if capbac == 'CV3':
            return 4 * luong
        else:
            return 3 * luong
    else:
        if capbac == 'CV3':
            return 3.5 * luong
        else:
            return 2 * luong


sex = input('Nhập giới tính (F/M): ')

#while sex != 'F' or sex != 'M':
    #print('Sai cú pháp! Vui lòng nhập lại!')
   # sex = input('Nhập giới tính (F/M): ')


capbac = input('Nhập cấp bậc (CV1/CV2/CV3): ')
while capbac != 'CV1' and capbac != 'CV2' and capbac != 'CV3':
    print('Sai cú pháp! Vui lòng nhập lại!')
    capbac = input('Nhập cấp bậc (CV1/CV2/CV3): ')

luong_thang = float(input('Nhập lương tháng: '))

print(f'Giới tính: {sex}')
print(f'Cấp bậc: {capbac}')
print(f'Lương tháng: {luong_thang}')
if sex != '':
    tienthuong = thuong_nhanvien(capbac, luong_thang, sex)
else:
    tienthuong = thuong_nhanvien(capbac, luong_thang)
print(f'Lương thưởng: {tienthuong}')
"""

#Bai3 Nhập vào một chuỗi 'adfasd1sdfdf9fasd8fsd8' in ra kí tự số trong chuỗi '1998'
"""
def take_digit(string):
    newoutput = ''
    for i in string:
        if i.isdigit() == True:
            newoutput += i

    return newoutput


string = input('Nhập vào chuỗi: ')
string = take_digit(string)
print(string)
"""
#SCOPE
"""
x = 'Global scope'

def local():
    local_variable = 'Local scope'
    print(local_variable)

print(x)
"""
