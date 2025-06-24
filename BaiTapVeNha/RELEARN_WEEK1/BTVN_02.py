tich = 1
n = int(input('Nhập n: '))

for i in range(2, n+ 1, 2):
    tich *= i

print(f"Tích các số chẵn từ 1 tới {n} = {tich}")