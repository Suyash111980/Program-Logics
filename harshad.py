rem=0
sum=0

num = int (input("Enter a number "))
temp=num

while num > 0:
        rem = num % 10
        sum += rem
        num //= 10

print(sum)   

if(temp%sum==0):
        print("Number is Harshad")
else :
        print("Number is not Harshad")        
