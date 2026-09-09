n= int (input("enter a number "))
i=1
sum=0

while i<n:
    if n%i==0:
        sum=sum+i
        print(i)


    i+=1

        

if sum==n:
    print("Number is perfect")


else:
    print("Numbeer is not perfect")    

