import random
import string


def generate_password(length):
    if length < 1:
        return "Độ dài mật khẩu phải lớn hơn 0."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


# Yêu cầu người dùng nhập độ dài mật khẩu
try:
    length = int(input("Nhập độ dài mật khẩu: "))
    print("Mật khẩu ngẫu nhiên: ", generate_password(length))
except ValueError:
    print("Vui lòng nhập một số nguyên hợp lệ.")
