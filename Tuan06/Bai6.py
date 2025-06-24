import random



while True:
    try:
        print('Nhập danh sách ngẫu nhiên: ', end = '')
        l = list(map(int, input().split()))
        break
    except ValueError:
        pass

print('Dãy số ngẫu nhiên: ', l)

print('Số ngẫu nhiên được chọn từ dãy trên: ', random.choice(l))