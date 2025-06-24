import math
from Bai4 import resolve_1st_degree_equation


def resolve_2nd_degree_equation(a, b, c):
    delta = pow(b, 2) - 4 * a * c
    if delta < 0:
        print('The equation has no solution!')
    elif delta == 0:
        print(f'The equation has double solution x = - {b} / 2 * {a}\nx = {-b / (2 * a)}')
    else:
        print(f'The equation has two distinguish solution\nx1 = -{b} + sqrt{delta} / (2 * {a})\nx2 = -{b} - sqrt{delta} / (2 * {a})\nx 1 = {-b + math.sqrt(delta) / (2 * a)}\nx2 = {-b - math.sqrt(delta) / (2 * a)}')

if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))
    c = int(input('Enter c: '))


    if a == 0:
        resolve_1st_degree_equation(b, c)
    else:
        resolve_2nd_degree_equation(a, b, c)