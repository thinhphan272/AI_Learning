import tkinter as tk
from tkinter import messagebox, ttk
import json
import os
import random
from datetime import datetime
import re


class StudentManagementApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quản lý Sinh viên")

        # Tạo file students.json nếu chưa tồn tại
        self.filename = "students.json"
        if not os.path.exists(self.filename):
            with open(self.filename, 'w') as f:
                json.dump([], f)

        # Load dữ liệu từ file
        self.students = self.load_students()

        # Tạo giao diện
        self.create_widgets()

        # Hiển thị danh sách sinh viên ban đầu
        self.display_students()

    def load_students(self):
        try:
            with open(self.filename, 'r') as f:
                return json.load(f)
        except (json.JSONDecodeError, FileNotFoundError):
            return []

    def save_students(self):
        with open(self.filename, 'w') as f:
            json.dump(self.students, f, indent=4)

    def generate_student_id(self):
        # Chữ số đầu là 2
        first_digit = '2'

        # 3 chữ số tiếp theo: 001 hoặc 033
        middle_part = random.choice(['001', '033'])

        # 3 chữ số tiếp theo là 3 số cuối năm hiện tại
        current_year_last3 = str(datetime.now().year)[-3:]

        # 3 chữ số cuối ngẫu nhiên từ 000 đến 999
        last_part = f"{random.randint(0, 999):03d}"

        return first_digit + middle_part + current_year_last3 + last_part

    def validate_email(self, email):
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    def create_widgets(self):
        # Frame chính
        main_frame = ttk.Frame(self.root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Nhãn tiêu đề
        ttk.Label(main_frame, text="Quản lý Sinh viên", font=('Arial', 14, 'bold')).grid(row=0, column=0, columnspan=2,
                                                                                         pady=10)

        # Phần nhập thông tin sinh viên
        ttk.Label(main_frame, text="Tên sinh viên:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.name_entry = ttk.Entry(main_frame, width=40)
        self.name_entry.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5)

        ttk.Label(main_frame, text="Email sinh viên:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.email_entry = ttk.Entry(main_frame, width=40)
        self.email_entry.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5)

        # Nút thêm sinh viên
        self.add_button = ttk.Button(main_frame, text="Thêm sinh viên", command=self.add_student)
        self.add_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Ô tìm kiếm
        ttk.Label(main_frame, text="Tìm kiếm:").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.search_entry = ttk.Entry(main_frame, width=40)
        self.search_entry.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5)
        self.search_entry.bind('<KeyRelease>', self.search_students)

        # Danh sách sinh viên
        ttk.Label(main_frame, text="Danh sách sinh viên:").grid(row=5, column=0, sticky=tk.W, pady=5)

        self.student_listbox = tk.Listbox(main_frame, width=60, height=10)
        self.student_listbox.grid(row=6, column=0, columnspan=2, pady=5)

        # Thanh cuộn
        scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=self.student_listbox.yview)
        scrollbar.grid(row=6, column=2, sticky=(tk.N, tk.S))
        self.student_listbox.config(yscrollcommand=scrollbar.set)

        # Nút xóa
        self.delete_button = ttk.Button(main_frame, text="Xóa", command=self.delete_student)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10)

        # Kết quả tìm kiếm
        ttk.Label(main_frame, text="Kết quả tìm kiếm:").grid(row=8, column=0, sticky=tk.W, pady=5)
        self.search_result_listbox = tk.Listbox(main_frame, width=60, height=5)
        self.search_result_listbox.grid(row=9, column=0, columnspan=2, pady=5)

        # Cấu hình resize
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(1, weight=1)

    def display_students(self):
        self.student_listbox.delete(0, tk.END)
        for student in self.students:
            self.student_listbox.insert(tk.END, f"{student['id']} - {student['name']} - {student['email']}")

    def add_student(self):
        name = self.name_entry.get().strip()
        email = self.email_entry.get().strip()

        if not name:
            messagebox.showerror("Lỗi", "Vui lòng nhập tên sinh viên")
            return

        if not email:
            messagebox.showerror("Lỗi", "Vui lòng nhập email")
            return

        if not self.validate_email(email):
            messagebox.showerror("Lỗi", "Email không hợp lệ")
            return

        # Tạo MSSV
        student_id = self.generate_student_id()

        # Thêm sinh viên mới
        new_student = {
            'id': student_id,
            'name': name,
            'email': email
        }

        self.students.append(new_student)
        self.save_students()
        self.display_students()

        # Xóa nội dung nhập
        self.name_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)

        messagebox.showinfo("Thành công", "Thêm sinh viên thành công")

    def delete_student(self):
        selected_index = self.student_listbox.curselection()
        if not selected_index:
            messagebox.showerror("Lỗi", "Vui lòng chọn sinh viên cần xóa")
            return

        confirm = messagebox.askyesno("Xác nhận", "Bạn có chắc chắn muốn xóa sinh viên này?")
        if confirm:
            index = selected_index[0]
            del self.students[index]
            self.save_students()
            self.display_students()
            self.search_result_listbox.delete(0, tk.END)
            messagebox.showinfo("Thành công", "Xóa sinh viên thành công")

    def search_students(self, event=None):
        keyword = self.search_entry.get().strip().lower()
        self.search_result_listbox.delete(0, tk.END)

        if not keyword:
            return

        results = []
        for student in self.students:
            if (keyword in student['name'].lower()) or (keyword in student['email'].lower()):
                results.append(f"{student['id']} - {student['name']} - {student['email']}")

        for result in results:
            self.search_result_listbox.insert(tk.END, result)


if __name__ == "__main__":
    root = tk.Tk()
    app = StudentManagementApp(root)
    root.mainloop()