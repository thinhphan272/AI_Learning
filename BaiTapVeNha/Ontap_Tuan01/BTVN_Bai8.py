def tinhNamNhuan(nam):
    if nam % 4 == 0 and nam % 100 != 0:
        print(f"{nam} là năm nhuận!")
    else:
        print(f"{nam} không phải năm nhuận!")

nam = int(input('Nhập vào năm: '))
tinhNamNhuan(nam)