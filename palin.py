num = int(input("enter a Number "))
temp=num


rev = 0

while num > 0:
    rem = num % 10
    rev = rev*10+rem
    num //= 10
 
print(rev)

if temp==rev:
    print("Number is palindrome ")

else:
    print("Number is not palindrome ")    