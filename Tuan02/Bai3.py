import random

m = int(input('Nhập số dòng: '))
n = int(input('Nhập số cột: '))

a = [[random.randint(0, 50) for j in range(n)] for i in range(m)]

def xuat_maTran(a):
    for m in a:
        print(m)
    
def xuat_phantu_dongK(a, k):
    if 0 <= k < len(a):
        print(f'Các phần tử của dòng {k}: {a[k]}')
    else:
        print("Chỉ số dòng không hợp lệ!")

def xuat_phantu_cotK(a, k):
    if 0 <= k < len(a[0]):
        print(f'Các phần tử của cột {k}: ')
        for i in range(len(a)):
            print(a[i][k])
    else:
        print("Chỉ số cột không hợp lệ!")
        
def tim_dong_TonglonNhat(a):
    max_sum = 0
    max_col = -1
    
    for row in a: 
        row_sum = sum(row)
        
        if row_sum > max_sum:
            max_sum = row_sum
            max_row = row
            
    return max_row

def tim_cot_TichLonNhat(a):
    
    if not a or not a[0]:
        return -1
    
    max_product = float('-inf')
    max_col = -1
    
    for j in range(len(a[0])):
        col_product = 1
        for i in range(len(a[0])):
            col_product *= a[i][j]
            
        if col_product > max_product:
            max_product = col_product
            max_col = j
            
    return max_col

def tich_pTu_Cot(a, col_index):
    product = 1
    for m in a:
        product *= m[col_index]
        
    return product

def pTu_dongChan_cotLe(a):
    for i in range(len(a)):
        if i % 2 == 0:
            for j in range(len(a[0])):
                if j % 2 != 0:
                    print(f'Phần tử tại dòng {i}, cột {j}: {a[i][j]}')

def tinh_TBC_pTuChan_dongLe(a):
    tong = 0
    dem = 0
    
    for i in range(len(a)):
        if i % 2 != 0:
            for j in range(len(a[0])):
                if a[i][j] % 2 == 0:
                    tong += a[i][j]
                    dem += 1
    
    if dem == 0:
        return 0
    else:
        return tong / dem
    
def tinh_TBC_pTuBien(a):
    if not a or not a[0]:
        return 0
    
    tong = 0 
    dem = 0
    
    m = len(a)
    n = len(a[0])
    
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                tong += a[i][j]
                dem += 1
                
    if dem == 0:
        return 0
    else:
        return tong / dem
    
    
def tinh_TBTich_pTuBien(a):
    
    if not a or not a[0]:
        return 0
    
    tich = 1
    dem = 0
    
    m = len(a)
    n = len(a[0])
    
    for i in range(m):
        for j in range(n):
            if 0 < i < m - 1 and 0 < j < n - 1:
                tich *= a[i][j]
                dem += 1
                
    if dem == 0:
        return 0
    else:
        return tich ** (1 / dem)
#CÂU A

xuat_maTran(a)
'''
CÂU B

k = int(input('Nhập vị trí dòng cần xem: '))

xuat_phantu_dongK(a, k)

CÂU C

k = int(input('Nhập vị trí cột cần xem: '))

xuat_phantu_cotK(a, k)

CÂU D

dong_coTong_LonNhat = tim_dong_TonglonNhat(a)

if dong_coTong_LonNhat:
    print(f'Dòng có tổng lớn nhất: {dong_coTong_LonNhat} (tổng = {sum(dong_coTong_LonNhat)})')
else:
   print('Ma trận rỗng')
    
CÂU E

col_index = tim_cot_TichLonNhat(a)

if col_index != -1:
    print(f'Cột có tích lớn nhất là cột {col_index} (tích = {tich_pTu_Cot(a, col_index)})')
else:
    print("Ma trận rỗng.")
 

#CÂU F
pTu_dongChan_cotLe(a)

#CÂU G

tbc = tinh_TBC_pTuChan_dongLe(a)

print(f'Trung bình cộng các phần tử chẵn thuộc dòng lẻ: {tbc}')
'''

#CÂU H

tbc = tinh_TBC_pTuBien(a)
print(f'Trung bình cộng các phần tử thuộc biên: {tbc}')

#CÂU I

tbtich = tinh_TBTich_pTuBien(a)
print(f'Trung bình tích các phần từ không thuộc biên: {tbtich}')