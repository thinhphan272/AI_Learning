import random
import re

class SinhVienHuit:
    
    def __init__(self):
       self.year = "14"  # Khóa học (luôn là 14)
       self.department = "DH"  # Mã ngành (luôn là DH)
       self.major_codes = ["TH", "BM", "DS"]  # Các chuyên ngành có thể chọn
       self.class_number_range = range(1, 100)  # Số lớp từ 01 đến 99
       
    
    
    def createNew(self):
       
        self.Mssv = ''.join(random.choices('0123456789', k = 10))
        self.Dtb = round(random.randint(0, 10) + random.random(),2)
        self.Tuoi = random.randint(18, 70)
        
        major_code = random.choice(self.major_codes)
       # Chọn ngẫu nhiên số lớp từ 01 đến 99
        class_number = random.choice(self.class_number_range)
        
        self.Lop = f"{self.year}{self.department}{major_code}{class_number:02d}"
        
    def inputInfo(self):
        
        while True:
            self.Mssv = input("Nhập mã số sinh viên(10 ký tự): ")
            if len(self.Mssv) < 10:
                print('Nhập lại ! (Phải đủ 10 ký tự).')
            elif len(self.Mssv) > 10:
                print('Nhập lại ! (Không được quá 10 ký tự)')
            else:
                break
                
        while True:
            self.Dtb = input('Nhập điểm trung bình: ')
            if len(self.Dtb) < 0:
                print('Nhập lại ! (Điểm phải lớn hơn 0).')
            elif len(self.Dtb) > 10:
                print('Nhập lại ! (Điểm không được quá 10)')
            else:    
                break
        
        self.Tuoi = int(input('Nhập tuổi: '))
        
        pattern = r"^14DH(TH|BM|DS)\d{2}$"
        
        while True:
            self.Lop = input('Nhập mã lớp theo định dạng 14DH<mã nganh(TH, BM, DS)><Số lớp(từ 01 - 99)>')
            if re.match(pattern, self.Lop):
                break
            else:
                print("Không đúng cú pháp ! Nhập Lại !")
           
        
    def showInfo(self):
        print(f'{self.Mssv} - {self.Dtb} - {self.Tuoi} - {self.Lop}')
        