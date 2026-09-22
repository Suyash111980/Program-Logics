x=[90,25,34,56]

key=int(input("enter element to serach"))
flag=0


for i in x:
    if(i==key):
     print("key found")
     flag=1
     break
    
if(flag==0):
    print("key not found ")
        
sq=0 
listofsq=[]   
for i in range(len(x)):
   if i %2 != 0:
      sq=x[i]*x[i]
      listofsq+=[sq]

print(listofsq)

num=0
for i in listofsq:
   if i%5==0:
      num+=i

print(num)


sum=0

while num>0:
   rem=num%10
   sum+=rem
   num//=10

print(sum)
      
      
   
   
   


   