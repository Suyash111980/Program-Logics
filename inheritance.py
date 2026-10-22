class A:
    def hello(self): #parent class or super class 
        print("Hello a")

class B(A):
    def welcome(self):
        print("Welcome B")


b1=B()
b1.hello()
b1.welcome()                