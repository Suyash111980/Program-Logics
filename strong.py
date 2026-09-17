num= int (input("enter a number "))
rem=0
sum=0

tot=0
temp=num
while num > 0:
        rem = num % 10
        num //= 10
        fact=1
        for i in range (rem,0,-1):
                fact=fact*rem
                rem-=1
                

        tot+=fact
       

if (temp==tot)  :
        print("Number is strong")
else:
        print("Number is not strong")                    
        