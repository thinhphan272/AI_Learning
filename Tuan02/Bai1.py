import random

def create_array(n):
    a = [random.randint(1, 100) for _ in range(n)]
    
    b = [x for x in a if x % 2 == 0]
    
    return a, b

n = int(input('Nhập vào số phần tử dãy a: '))
a, b = create_array(n)
print('Dãy a: ', a)
print('Dãy b: ', b)