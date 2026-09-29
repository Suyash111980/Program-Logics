# # t=(10,20,5,10,5,3,5)
# # print(t.count(5))
# # print(t.index(5))

# # l1=[]
# # t2=(l1,10,20,30)
# # l1.append(1)
# # l1.append(2)
# # l1.append(3)
# # print(t2)
# # print(" -----------------Tuple with list ---------------------")
# # for i in t2:
    
# #     print(i,end=" ")

# student=(
#     ("amit",70,80,90),
#     ("ajay",67,77,99),
#     ("mahesh",100,100,99)
# )
# sum=0
# for i in student:
   
#     sum=i[1]+i[2]+i[3]
#     nam=i[0]
#     print(nam," : ",sum)




name=input("Enter Name :")
marks=[]

for i in range(3):
    marks.append(int(input("enter marks ")))


student=(name,marks)
print(student)    







