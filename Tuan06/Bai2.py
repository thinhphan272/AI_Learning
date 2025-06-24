import random

l = []
n = int(input('Nhập số lượng phần tử: '))
for i in range(n):
    l.append(random.randint(1,100))

print('Dãy số ngẫu nhiên')
print(l)

print('Dãy số sau khi tăng dần')
l.sort()
print(l)

