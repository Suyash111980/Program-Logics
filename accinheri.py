class Account:

    def accept(self):
        self.accno = int(input("Enter account number: "))
        self.cname = input("Enter customer name: ")
        self.accbal = float(input("Enter account balance: "))

    def display(self):
        print("Account Number:", self.accno)
        print("Customer Name:", self.cname)
        print("Account Balance:", self.accbal)


class SavingAccount(Account):

    def inputdata(self):
        self.accept()
        self.interestrate = float(input("Enter interest rate: "))

    def displaydata(self):
        self.display()
        print("Interest Rate:", self.interestrate)


class CurrentAccount(Account):

    def getdata(self):
        self.accept()
        self.companyname = input("Enter company name: ")

    def putdata(self):
        self.display()
        print("Company Name:", self.companyname)


# Main program
print("\n--- Saving Account Details ---")
s = SavingAccount()
s.inputdata()
s.displaydata()

print("\n--- Current Account Details ---")
c = CurrentAccount()
c.getdata()
c.putdata()