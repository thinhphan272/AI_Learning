

class Student:
    def __init__(self, student_id, grade):
       
        self.student_id = student_id
        self.grade = grade

    def display_student_info(self):
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
