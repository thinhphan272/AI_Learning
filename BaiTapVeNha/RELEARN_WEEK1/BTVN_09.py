def veHCN(cr, cd):
    for i in range(cr):
        print('* ' * cd)
    print('')


def veHCN_Rong(cr, cd):
    for i in range(cr):
        for j in range (cd):
            if i == 0 or i == cr - 1 or j == 0 or j == cd-1:
                print('* ', end="")
            else:
                print('  ', end='')
        print()

def veTamGiaCVuong_trai(h):
    for i in range(1, h + 1):
        print('* '* i)
    print('')

def veTamGiacVuong_phai(h):
    for i in range(1, h + 1):
        print("  " * (h - i) + ' *' * i)
    print("")

def hinhThoi(height):
    for i in range(height // 2 + 1):
        print(" " * (height // 2 - i) + "*" * (2 * i + 1))

    # Phần dưới (tam giác cân đỉnh dưới)
    for i in range(height // 2 - 1, -1, -1):
        print(" " * (height // 2 - i) + "*" * (2 * i + 1))

if __name__ == '__main__':
    cd = int(input("Nhập chiều dài: "))
    cr = int(input('Nhập chiều rộng: '))
    print('Hình chữ nhật đặc:')
    veHCN(cr, cd)

    print('Hình chữ nhật rỗng: ')
    veHCN_Rong(cr, cd)

    h = int(input('Nhập chiều cao tam giác: '))
    print("Tam giác vuông trái: ")
    veTamGiaCVuong_trai(h)

    print('Tam giác vuông phải: ')
    veTamGiacVuong_phai(h)

    height = int(input('Nhập chiều cao hình thoi: '))

    hinhThoi(height)


