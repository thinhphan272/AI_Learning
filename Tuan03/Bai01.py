
from CCircle import Circle

n = float(input('Nhập bán kính: '))

P = Circle(n)

print('Bán kính hình tròn: ', P.r)
print('Chu vi hình tròn: ', P.getP())
print('Diện tích hình tròn: ', P.getS())
