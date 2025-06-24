import math



def ptBac2(a, b, c):
    delta = b**2 - 4*a*c
    if a == 0:
        if b== 0 and c != 0:
            print('Phương trình vô nghiệm!')
        elif b == 0 and c == 0:
            print('Phương trình có vô số nghiệm')
        else:
            print(f'Phương trình có nghiệm x = {-c / b}')
    else:
        if delta < 0:
            print('Phương trình vô nghiệm')
        elif delta == 0:
            print(f'Phường trình có 1 nghiệm kép x = {-b / (2*a)}')
        else:
            print(f'x1 = {(-b + math.sqrt(delta)) / (2*a)}')
            print(f'x2 = {(-b - math.sqrt(delta)) / (2*a)}')



a = int(input('Nhập a: '))
b = int(input('Nhập b: '))
c = int(input('Nhập c: '))


ptBac2(a, b, c)

