#Xóa khoảng trắng trong chuỗi

string = "    Hello World    "

print(string.strip())

print("Chuỗi in hoa: ", end = "")
print(string.strip().upper())

print('Chuỗi in thường: ', end = "")
print(string.strip().lower())

print('Thay chữ H bằng chữ J: ', end = "")
print(string.strip().replace('H', "J", 1))