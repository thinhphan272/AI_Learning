sum = 0
n = int(input('Enter n: '))
for i in range(2, n+1):
    if i % 2 == 0:
        sum += i

print(f'Total all number is even number from 2 to {n}: {sum}')
