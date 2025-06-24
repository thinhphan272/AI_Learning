

def tinhDiem(diem):
    if diem >= 0 and diem <= 3.9:
        print("F = 0 trên thang 4. KHÔNG ĐẠT!")
    elif diem >= 4.0 and diem <= 5.4:
        print('D = 1 trên thang 4. ĐẠT!')
    elif diem >= 5.5 and diem <= 6.9:
        print('C = 2 trên thang 4. ĐẠT!')
    elif diem >= 7.0 and diem <= 8.4:
        print('B = 3 trên thang 4. ĐẠT!')
    elif diem >= 8.5 and diem <= 10:
        print('A = 4 trên thang 4. ĐẠT!')


if __name__ == '__main__':
    diem = float(input('Nhập điểm của sinh viên: '))
    tinhDiem(diem)
