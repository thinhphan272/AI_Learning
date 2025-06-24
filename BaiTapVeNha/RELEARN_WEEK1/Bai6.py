sum = 0

for i in range(0, 1000):
    if i % 3 == 0 and i % 5 == 0:
        sum += i

print(f'Total all number is multiples of 3 and 5 from 0 to 999: {sum}')