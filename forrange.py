# for i in range (1,6):
#     print(i)

# print("\n Odd Numbers")
# for i in range (1,11,2):
#     print(i)

# print("\n Even  Numbers")
# for i in range (2,11,1):
#     print(i)    


# sum=0
# for i in range (11,36,1):
#     if(i%5==0):
#         sum=sum+i



# rem=0
# sum=0

# num = int (input("Enter a number "))
# temp=num

# while num > 0:
#         rem = num % 10
#         sum += rem
#         num //= 10

# print(sum)   

# if(temp%sum==0):
#         print("Number is Harshad")
# else :
#         print("Number is not Harshad")        


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
        


        






