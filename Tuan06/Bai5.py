import random
n = int(input('Nhập số lượng phần tử: '))

l = []
for i in range(n):
    l.append(random.randint(1,5))

print('Dãy số ngẫu nhiên: ', l)

print('Dãy số xóa phần từ trùng ', set(l))