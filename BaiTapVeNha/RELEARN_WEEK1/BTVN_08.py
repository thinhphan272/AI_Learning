def tinhNamNhuan(nam):
    if nam % 4 == 0 and nam % 100 != 0:
        print(f"{nam} là năm nhuận!")
    else:
        print(f'{nam} không phải năm nhuận!')


if __name__ == '__main__':
    nam = int(input("Nhập năm: "))
    tinhNamNhuan(nam)
