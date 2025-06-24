import json
import random

from colorama import Fore,Back, init

class HocSinh:
    ho = ["Nguyễn", "Lý", "Phan", "Trần", "Hồ", "Lê", "Đinh"]
    ho_dem = ["Thanh", "Yến", "Thành", "Gia", "Minh", "Mạnh"]
    ten = ["Quân", "Tài", "Quang", "Như", "Nga", "Hương", "Ly"]
    def __init__(self,name, age, sex, lop, diem):
        self.name = name
        self.age = age
        self.sex = sex
        self.lop = lop
        self.diem = diem



    def to_dict(self):
        return {"name": self.name, "age": self.age, "sex": self.sex, "lop": self.lop, "diem": self.diem}

    @classmethod
    def from_dict(cls,data):
        return cls(data["name"], data["age"], data["sex"], data["lop"], data["diem"])

def load_data(file_name):
    try:
        with open(file_name) as file:
            data = json.load(file)
            hocsinhs = [HocSinh.from_dict(item) for item in data]
    except FileNotFoundError:
        hocsinhs = []
    return hocsinhs

def save_data(hocsinhs, file_name):
    data = [hocsinh.to_dict() for hocsinh in hocsinhs]
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


def create_hocsinh_random(hocsinhs):
    name = f'{random.choice(HocSinh.ho)} {random.choice(HocSinh.ho_dem)} {random.choice(HocSinh.ten)}'
    age = random.randint(1, 100)
    sex = random.choice(["Nam", 'Nữ'])
    lop = f"{random.randint(11, 15)}DH{random.choice(['TH', 'BM', 'KHDL'])}{random.randint(1, 10):02d}"
    diem = random.randint(1, 11) + round(random.random(), 1)
    hocsinh = HocSinh(name, age, sex, lop, diem)
    hocsinhs.append(hocsinh)
    save_data(hocsinhs, "hocsinhs.json")
    print(Fore.GREEN + Back.BLACK + 'Học sinh được thêm thành công')
def create_hocsinh(hocsinhs):
    name = input('Nhập tên học sinh: ')
    age = int(input('Nhập tuổi: '))
    sex = input('Nhập giới tính: ')
    lop = input('Nhập lớp: ')
    diem = float(input('Nhập điểm: '))
    hocsinh = HocSinh(name, age, sex, lop, diem)
    hocsinhs.append(hocsinh)
    save_data(hocsinhs, "hocsinhs.json")
    print(Fore.GREEN + Back.BLACK + 'Học sinh được thêm thành công')

def read_hocsinhs(hocsinhs):
    if not hocsinhs:
        print(Fore.RED + Back.BLACK + 'Chưa có học sinh trong danh sách')
    else:
        for i, hocsinh in enumerate(hocsinhs, 1):
            print(f'{i}. {hocsinhs.name} - {hocsinhs.age} - {hocsinhs.sex} - {hocsinhs.lop} - {hocsinhs.diem}')
def main():
    init(autoreset=False)
    hocsinhs = load_data("hocsinhs.json")
    while True:
        print(Fore.YELLOW + Back.BLACK + '---------------Quản Lý Học Sinh---------------')
        print('1. Hiển thị danh sách học sinh: ')
        print('2. Thêm học sinh mới: ')
        print('3. Cập nhật học sinh')
        print('4. Xóa một học sinh')
        print('5. Thêm ngẫu nhiên 1 học sinh')
        print('0. Thoát')
        print(Fore.GREEN + Back.BLACK + '')
        choice = input('Chọn chức năng: ')

        if choice == '1':
            read_hocsinhs(hocsinhs)
        elif choice == '2':
            create_hocsinh(hocsinhs)
        elif choice == '5':
            create_hocsinh_random(hocsinhs)
        elif choice == '4':
            pass
        elif choice == '0':
            print(Fore.BLUE + Back.BLACK + 'Kết thúc chương trình !!')
            break
        else:
            print(Fore.RED + Back.BLACK + 'Lựa chọn không hợp lệ. Vui lòng nhập lại !')

if __name__ == '__main__':
    main()
