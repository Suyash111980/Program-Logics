x=[23,56,78,2,1]
count=0
sum=0


for i in x:
    count+=1
    sum+=i

print("Lenght of the list=",count)
print("Sum of List=",sum)

max=0
for i in x:
    if(i>max):
        max=i
print("Maximum Number=",max)

min=x[0]
for i in x:
    if(i<min):
        min=i

print("Minimum Number=",min)    



even=[]
odd=[]
evensum=0
oddsum=0
for i in x:
    if(i%2==0):
        even+=[i]
        evensum+=i
    else:
        odd+=[i] 
        oddsum+=i 
print("Even NUmber")
print(even)
print(" Odd Numbers")
print(odd)
print(" Even Sum")
print(evensum)
print(" Odd sum")
print(oddsum)




    

      


