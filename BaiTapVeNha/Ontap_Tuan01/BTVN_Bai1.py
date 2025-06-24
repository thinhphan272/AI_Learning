sum = 0
n = int(input("Nhập n: "))
for i in range(1, n + 1):
    if i % 2 != 0:
        sum += i

print(f"Tổng các số lẻ S = 1 + 3 + 5 + ... + {n} = {sum}")