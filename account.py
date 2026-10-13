class Account:
    def __init__(self, accno, name, acctype, accbal):
        self.__accno = accno
        self.__name = name
        self.__acctype = acctype
        self.__accbal = accbal

    @property
    def accno(self):
        return self.__accno

    @property
    def name(self):
        return self.__name

    @property
    def acctype(self):
        return self.__acctype

    @property
    def accbal(self):
        return self.__accbal

    @accbal.setter
    def accbal(self, amount):
        self.__accbal = amount


lstaccount = []

while True:
    print("\n----- ACCOUNT MANAGEMENT SYSTEM -----")
    print("1. Create Account")
    print("2. Display Account")
    print("3. Search Account")
    print("4. Deposit")
    print("5. Withdrawal")
    print("6. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        ano = int(input("Enter account number: "))

        if any(acc.accno == ano for acc in lstaccount):
            print("Account already exists")
            continue

        name = input("Enter customer name: ")
        acctype = input("Enter account type: ")
        accbal = float(input("Enter initial balance: "))

        if accbal < 500:
            print("Minimum balance should be 500")
        else:
            acc = Account(ano, name, acctype, accbal)
            lstaccount.append(acc)
            print("Account created successfully")

    elif ch == 2:
        if not lstaccount:
            print("No accounts available")
        else:
            for acc in lstaccount:
                print("\nAccount Number:", acc.accno)
                print("Customer Name:", acc.name)
                print("Account Type:", acc.acctype)
                print("Account Balance:", acc.accbal)

    elif ch == 3:
        ano = int(input("Enter account number: "))
        found = False

        for acc in lstaccount:
            if acc.accno == ano:
                print("\nAccount Found")
                print("Account Number:", acc.accno)
                print("Customer Name:", acc.name)
                print("Account Type:", acc.acctype)
                print("Account Balance:", acc.accbal)
                found = True
                break

        if not found:
            print("Account not found")

    elif ch == 4:
        ano = int(input("Enter account number: "))
        found = False

        for acc in lstaccount:
            if acc.accno == ano:
                amount = float(input("Enter deposit amount: "))

                if amount > 0:
                    acc.accbal = acc.accbal + amount
                    print("Deposit successful")
                    print("Updated balance:", acc.accbal)
                else:
                    print("Enter a valid deposit amount")

                found = True
                break

        if not found:
            print("Account not found")

    elif ch == 5:
        ano = int(input("Enter account number: "))
        found = False

        for acc in lstaccount:
            if acc.accno == ano:
                amount = float(input("Enter withdrawal amount: "))

                if amount <= 0:
                    print("Enter a valid withdrawal amount")

                elif acc.accbal - amount >= 500:
                    acc.accbal = acc.accbal - amount
                    print("Withdrawal successful")
                    print("Remaining balance:", acc.accbal)

                else:
                    print("Insufficient balance!")
                    print("Minimum balance is 500 ")

                found = True
                break

        if not found:
            print("Account not found")

    elif ch == 6:
        print("Thank you for using Account Management System")
        break

    else:
        print("Invalid choice")