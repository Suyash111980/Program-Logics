def factor(n):
    print("Factors are : ")
    for i in range(1, n + 1):
        if n % i == 0:
            print(i) 


def factorial(n):
    fact=1

    for i in range(1,n+1):
        fact=fact*i

    print("Factorial are : ",fact)


def primenumber(n):
    count=0
    for i in range(1,n+1):
        if n%i==0:
            count=count+1
    if count==2:
        print("n,is a prime number");
    else:
        print("n,is not a prime number");


def sum_digits(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    print("Sum of digits:", total)


def fibonacci(n):
    a = 0
    b = 1

    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c
    print()



def table(n):
    for i in range(1, 11):
        print(n, "x", i, "=", n * i)