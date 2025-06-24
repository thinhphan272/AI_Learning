a = [3, 9, 1, 4]
b = [2, 7, 4, 3, 8, 2]
min = len(b) if len(a) > len(b) else len(a)
c = a if len(a)>len(b) else b
for i in range(min):
    c[i] = a[i] + b [i]
print(c)