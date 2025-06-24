from CSinhVien import SinhVien

mssv = input('Nhập mã số sinh viên: ')
tenSV = input('Nhập họ và tên sinh viên: ')


sv1 = SinhVien(mssv, tenSV)

print("Sinh viên 1: ", sv1.getName())
sv1.get()
sv1.put()