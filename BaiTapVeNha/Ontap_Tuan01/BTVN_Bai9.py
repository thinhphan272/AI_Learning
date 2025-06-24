h = int(input("Nhập chiều cao: "))
cr = int(input('Nhập chiều rộng: '))

for i in range(h):
    for j in range(cr):
        print("* ",end="")

    print("")

print("\n")

for i in range(h):
    if i == 0 or i == h-1:
        print("*" * cr)
    else:
        print("*" + " " * (cr - 2) + "*")


for i in range(1, h + 1):
    print("*" * i)


height = int(input("Nhập chiều cao kim cương (số lẻ): "))

# Vẽ nửa trên của hình thoi
for i in range(1, height + 1, 2):
    print(" " * ((height - i) // 2) + "*" * i)

# Vẽ nửa dưới của hình thoi
for i in range(height - 2, 0, -2):
    print(" " * ((height - i) // 2) + "*" * i)