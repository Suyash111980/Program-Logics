stud=[
    [1,"ram",23],
    [3,"shyam",25],
     [2,"raman",24]
]

#CRUD
#view stud 

for i in stud:
    print(i[0],i[1],i[2])

#only ages
sum=0
for i in stud:
    print(i[2])
    sum+=i[2]
print("Total of age ",sum)





max=stud[0][2]
name=""
for i in stud:
    if(i[2]>max):
        max=i[2]
        name=i[1]
print("Older Age =",max,name)


min=stud[0][2]
name=stud[0][1]
for i in stud:
    if(i[2]<min):
        min=i[2]
        name=i[1]


print("Younger age= ",min,name)  
