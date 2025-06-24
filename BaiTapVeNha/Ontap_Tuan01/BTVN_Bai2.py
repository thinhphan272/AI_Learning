tich = 1

n = int(input("Nhập n: "))
for i in range(2, n+1, 2):
    tich *= i

print(f"Tích các số từ 2 x 4 x 6 x ... x {n} = {tich}")