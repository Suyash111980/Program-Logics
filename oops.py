class demo:

    def accept(self):
        self.rno=int(input("Enter roll no : "))
        self.name=input("Enter Name    : ")

    def marks(self):
        self.tm=300
        self.eng=int(input("Enter ENGLISH marks : "))
        self.math=int(input("Enter MATHS marks   : "))
        self.sci=int(input("Enter SCIENCE marks : "))
        self.total=self.eng+self.math+self.sci 
        self.per=(self.total/self.tm)*100
        # self.avg=self.total/3

    def gradegiven(self):
        if self.per >= 90:
            self.grade = "A+"
        elif self.per >= 80:
            self.grade = "A"
        elif self.per >= 70:
            self.grade = "B"
        elif self.per >= 60:
            self.grade = "C"
        elif self.per >= 50:
            self.grade = "D"
        else:
            self.grade = "Fail"

    def show(self):
        print("============RESULT=============")
        print("   Name       : ",self.name)
        print("   Roll no    : ",self.rno)
        print("   Total      : ",self.total)
        print("   Percentage :", self.per,"%")
        print("   Grade      :", self.grade)
        print("===============================")


lststu=[]
while True:

    d1=demo()
    d1.accept()
    d1.marks()
    d1.gradegiven()

    lststu.append(d1)

    c=int(input("Do you want to continue press 1"))
    if c!=1:
        break

for s in lststu:
        s.show()