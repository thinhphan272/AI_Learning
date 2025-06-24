import random

xuc1 = random.randint(1, 7)
xuc2 = random.randint(1, 7)

kq = xuc1 + xuc2

print('Kết quả xúc sắc 1: ', xuc1)
print('Kết quả xúc sắc 2: ', xuc2)
print('Tổng xúc sắc: ',kq )

if kq % 2 == 0:
    print('Tài, Nhà cái ăn tiền')
else:
    print('Xỉu, Nhà cái vẫn ăn tiền')