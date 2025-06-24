n = int(input('Nhập n: '))
sum = 0
for i in range(1, n + 1, 2):
    sum += i

print(f"Tổng số lẻ từ 1 tới {n}: {sum}")