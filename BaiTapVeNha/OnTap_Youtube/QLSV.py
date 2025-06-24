import json
import random
class Student:

    def __init__(self, name, age, gender, lop, diem):

        self.name = name
        self.age = age
        self.gender = gender
        self.lop = lop
        self.diem = diem

    def to_dict(self):
        return{"name": self.name, "age": self.age, "gender": self.gender, "lop": self.lop, "diem": self.diem}

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["age"], data["gender"], data["lop"], data["diem"])


def load_data(file_name):
    try:
        with open(file_name, 'r') as file:
            data =  json.load(file)
            students = [Student.from_dict(item) for item in data]
    except FileNotFoundError:
        students = []
    return students

def save_data(students, file_name):
    data = [student.to_dict() for student in students]
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)

def create_student_random(students):
    ho = ["Nguyễn", "Lý", "Phan", "Trần", "Hồ", "Lê", "Đinh"]
    ho_dem = ["Thanh", "Yến", "Thành", "Gia", "Minh", "Mạnh"]
    ten = ["Quân", "Tài", "Quang", "Như", "Nga", "Hương", "Ly"]
    name = f'{random.choice(ho)} {random.choice(ho_dem)} {random.choice(ten)}'
    age = random.randint(18,50)
    gender = random.choice(['Nam', 'Nữ'])
    lop = f'{random.randint(11,14)}DH{random.choice(["TH","BM","KHDL"])}{random.randint(1, 10):02d}'
    diem = random.randint(0, 10) + round(random.random(),1)
    student = Student(name, age, gender, lop, diem)
    students.append(student)
    save_data(students, "QLHS.json")
    print('Học sinh được thêm thành công')

def read_student(students):
    if not students:
        print('Danh sách học sinh trống!!')
    else:
        for i, student in enumerate(students, 1):
            print(f"{i}. {student.name} - {student.age} - {student.gender} - {student.lop} - {student.diem}")


def update_student(students):
    read_student(students)
    try:
        index = int(input("Nhập số thứ tự của sinh viên muốn cập nhật: ")) - 1
        if 0 <= index < len(students):
            students[index].name = input("Nhập tên mới: ") or students[index].name
            students[index].age = int(input("Nhập tuổi mới: ") or students[index].age)
            students[index].gender = input("Nhập giới tính mới: ") or students[index].gender
            students[index].lop = input("Nhập lớp mới: ") or students[index].lop
            students[index].diem = float(input("Nhập điểm mới: ") or students[index].diem)
            save_data(students, "QLHS.json")
            print("Cập nhật thành công!")
        else:
            print("Số thứ tự không hợp lệ!")
    except ValueError:
        print('Vui lòng nhập đúng định dạng!')

def delete_student(students):
    read_student(students)
    try:
        index = int(input('Nhập số thứ tự của sinh viên muốn xóa: ')) -1
        if 0 <= index < len(students):
            del students[index]
            save_data(students, "QLHS.json")
            print('Xóa thành công!')
        else:
            print('Số thứ tự không hợp lệ!')
    except ValueError:
        print('Vui lòng nhập đúng định dạng!')

def main():
    students = load_data("QLHS.json")
    while True:
        print('\n---------------Quản lý sinh viên---------------')
        print('1. Hiển thị danh sách sinh viên')
        print('2. Thêm sinh viên mới')
        print('3. Cập nhật sinh viên')
        print('4. Xóa sinh viên')
        print('0. Thoát chương trình')

        choice = input('Chọn chức năng: ')

        if choice == '1':
            read_student(students)
        elif choice == '2':
            create_student_random(students)
        elif choice == '3':
            update_student(students)
        elif choice == '4':
            delete_student(students)
        elif choice == '0':
            print("Kết thúc chương trình!!")
            break
        else:
            print('Lựa chọn không hợp lệ. Vui lòng nhập lại!')

if __name__ == '__main__':
    main()
