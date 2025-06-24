import random
n = int(input('Nhập số lượng phần tử: '))

l = []
for i in range(n):
    l.append(random.randint(1,1000))

print('Dãy số ngẫu nhiên: ', l)

print('Số lớn nhất ', max(l))
print('Số nhỏ nhất ', min(l))