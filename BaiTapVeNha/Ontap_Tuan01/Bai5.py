import math
from Bai4 import ptBac1
def ptBac2(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    if delta < 0:
        print("Phương trình vô nghiệm")
    elif delta == 0:
        tmp = -b / (2 * a)
        print(f"Phương trình có nghiệm kép x1 = x2 = -b / 2a\nx1 = x2 = {tmp}")
    else:
        x1 = (-b + math.sqrt(delta)) / (2 * a)
        x2 = (-b - math.sqrt(delta)) / (2 * a)
        print(f"x1 = {x1}, x2 = {x2}")


a = int(input('Nhập a: '))
b = int(input("Nhập b: "))
c = int(input('Nhập c: '))

if a == 0:
    ptBac1(b, c)
else:
    ptBac2(a, b, c)