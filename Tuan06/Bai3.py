import random
import math
import statistics

n = int(input('Nhập số lượng phần tử'))

l = []
for i in range(n):
    l.append(random.randint(1, 100))

print('Dãy số ngẫu nhiên: ', l)


print("Trung bình cộng của dãy sô: ", round(statistics.mean(l),2))
