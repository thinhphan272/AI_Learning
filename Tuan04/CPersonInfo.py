from CPerson import Person
from CStudent import Student
from CEmployee import Employee

class PersonInfo(Person, Employee, Student):
    def __init__(self, name, age, emp_id, salary, student_id, grade):
        Person.__init__(self, name, age)
        Employee.__init__(self, emp_id, salary)
        Student.__init__(self, student_id, grade)

    def display_person_info(self):
  
        Person.display_person_info(self)
        Employee.display_employee_info(self)
        Student.display_student_info(self)