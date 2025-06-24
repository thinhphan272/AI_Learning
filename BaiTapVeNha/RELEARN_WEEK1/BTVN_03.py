tich = 1
n = int(input('Nhập n: '))
for i in range(1, n+ 1, 2):
    tich *= i

print(f'Tích các số lẻ từ 1 tới {n}: {tich}')