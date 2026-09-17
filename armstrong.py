no = int (input("enter a number "))

sum = 0
temp = no
c = 0

while no > 0:
    c += 1
    no //= 10

no = temp

while no > 0:
    rem = no % 10
    sum += rem ** c
    no //= 10

if temp == sum:
    print("Number is Armstrong")
else:
    print("Number is not Armstrong")
