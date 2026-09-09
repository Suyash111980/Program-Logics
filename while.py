i=1 
n=20
evensum=0
oddsum=0
tot=0


while i<=n:
    if i%2==0:
        evensum=evensum+i
    
    else :
        oddsum=oddsum+i
        

    i+=1
tot=evensum+oddsum


print(evensum)
print(oddsum)
print(tot)