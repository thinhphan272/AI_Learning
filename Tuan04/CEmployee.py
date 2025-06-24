class Employee:
    def __init__(self, emp_id, salary):
        

        self.emp_id = emp_id
        self.salary = salary

    def display_employee_info(self):
        
        print(f"Employee ID: {self.emp_id}")
        print(f"Salary: {self.salary}")
