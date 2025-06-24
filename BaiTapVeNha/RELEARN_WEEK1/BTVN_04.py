n = int(input('Nhập n: '))
tich = 1
for i in range(1, n+ 1):
    tich *= i

print(f'{n}! = {tich}')