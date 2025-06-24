n = int(input('Nhập n: '))

result = []
for i in range(1, n+ 1):
    result.append(f'{i} : {i*i}')
print(', '.join(result))