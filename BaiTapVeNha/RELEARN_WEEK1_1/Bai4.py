def ptBac1(a, b):
    if a == 0 and b != 0:
        print('Phương trình vô nghiệm!')
    elif a == 0 and b == 0:
        print('Phương trình có vô số nghiệm')
    else:
        print(f'Phương trình có nghiệm x = {-b / a}')


a = int(input('Nhập a: '))
b = int(input('Nhập b: '))

ptBac1(a, b)