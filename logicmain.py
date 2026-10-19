from logic import *

while True:
    print("\n1. Factor")
    print("2. Factorial")
    print("3. Prime number")
    print("4. Even-Odd")
    print("5. Sum of digits")
    print("6. Fibonacci")
    print("7. Table")
    print("8. Exit")

    ch = int(input("Enter your choice: "))

    if ch == 1:
        n = int(input("Enter number to find factors: "))
        factor(n)

    elif ch == 2:
        n = int(input("Enter number to find factorial: "))
        factorial(n)

    elif ch == 3:
        n = int(input("Enter number to check prime: "))
        primenumber(n)

    elif ch == 4:
        n = int(input("Enter number: "))
        even_odd(n)

    elif ch == 5:
        n = int(input("Enter number: "))
        sum_digits(n)

    elif ch == 6:
        n = int(input("Enter number of terms: "))
        fibonacci(n)

    elif ch == 7:
        n = int(input("Enter number for table: "))
        table(n)

    elif ch == 8:
        print("Program ended")
        break

    else:
        print("Invalid choice")