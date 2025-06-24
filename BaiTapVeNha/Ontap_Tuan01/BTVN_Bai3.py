tich = 1

n = int(input('Nhập n: '))
for i in range(1, n+1, 2):
    tich *= i

print(f"Tích các số lẻ 1 x 3 x 5 x...x{n} = {tich} ")