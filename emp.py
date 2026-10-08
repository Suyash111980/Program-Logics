class Employee:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def __str__(self):
          return self.show()+" "+self.get_age()

    def show(self):
            return self.__name
     
     
    def get_age(self):       
            return self.__age

emp1=Employee('Rahul','40')
# print('name is',emp1.show())
# print("age is ",emp1.get_age)

print(emp1)





