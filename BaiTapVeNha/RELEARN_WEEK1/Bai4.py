

def resolve_1st_degree_equation(a, b):
    if a == 0 and b == 0:
        print('The equation has a correct solution for all x!')
    elif a == 0 and b != 0:
        print('The equation has no solution!')
    else:
        print(f'The equation has only one solution x = -{b} / {a}\nx = {round((-b / a), 1)}')



if __name__ == '__main__':
    a = int(input('Enter a: '))
    b = int(input('Enter b: '))

    resolve_1st_degree_equation(a, b)

