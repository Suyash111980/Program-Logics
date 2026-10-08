class Employee:

    def accept(self):
        self.emp = int(input("Enter Employee ID: "))
        self.name = input("Enter Employee Name: ")
        self.salary = float(input("Enter Salary: "))

    def calculate(self):
        self.hra = self.salary * 9 / 100
        self.ta = self.salary * 8 / 100
        self.ma = self.salary * 7 / 100
        self.final_salary = self.salary + self.hra + self.ta + self.ma

    def display(self):
        print("\n----- SALARY SLIP -----")
        print("Employee ID :", self.emp)
        print("Employee Name :", self.name)
        print("Salary :", self.salary)
        print("HRA :", self.hra)
        print("TA :", self.ta)
        print("MA :", self.ma)
        print("Final Salary :", self.final_salary)


emp_dict = {}

e = Employee()
e.accept()
e.calculate()

emp_dict[e.emp] = e

e.display()