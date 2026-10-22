class Employee:

    def accept(self):
        self.empid = int(input("Enter employee ID: "))
        self.ename = input("Enter employee name: ")
        self.salary = float(input("Enter employee salary: "))

    def display(self):
        print("Employee ID:", self.empid)
        print("Employee Name:", self.ename)
        print("Employee Salary:", self.salary)


class Manager(Employee):

    def getdata(self):
        self.accept()
        self.bonus = int(input("Enter bonus amount: "))

    def putdata(self):
        self.display()
        print("Employee Bonus:", self.bonus)


class Developer(Employee):

    def inputdata(self):
        self.accept()
        self.noofhr = int(input("Enter number of hours: "))

    def displaydata(self):
        self.display()
        print("Number of Hours:", self.noofhr)


# Main program
print("\n--- Manager Details ---")
m = Manager()
m.getdata()
m.putdata()

print("\n--- Developer Details ---")
d = Developer()
d.inputdata()
d.displaydata()