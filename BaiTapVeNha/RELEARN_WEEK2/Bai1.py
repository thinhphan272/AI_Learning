import numpy as np

a = np.array([1,2,3,4,5,6,7,8,9,10])

filter_a = a % 2 == 0

b = a[filter_a]

print(f'Dãy a: {a}')

print(f'Dãy b: {b}')


