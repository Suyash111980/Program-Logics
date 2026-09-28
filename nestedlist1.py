# # list1=[[10,20,30],
# # [40,50,60],
# # [70,80,90]
# # ]

# # n=int(input("Enter any  number :"))
# # flag=0
# # for i in list1:
# #     for j in i:
# #         if(j==n):
           
# #             flag=1
# #             break
        
# # if(flag==1):
# #     print("Number found",n)

# # if(flag==0):
# #     print("Number not found")


   

# o=0
# listmenu=['a','b','c']
# listprice=[100,200,300]
# j=0


# for i in listmenu:
#     print((o+1),i, " " ,listprice[j])
#     j+=1
#     o+=1

# ord=[]
# od=int(input("Enter Order :"))

# for i in listmenu:


o=0
listmenu=['a','b','c']
listprice=[100,200,300]


b=1
order=[]
while b==1:
    j=0
    o=0
    for i in listmenu:
        print((o+1),"   ",i,"   ",listprice[j])
        j+=1
        o+=1
    print("================================================")
    print("")
    on=int(input("Enter order number :"))
    order.append(on)
    print("One order placed ")

    b=int(input("Do you want to order again pree 1 "))

print("your order is ")
sum=0
for k in order:
    print(listmenu[k-1]," ",listprice[k-1])

    sum+=listprice[k-1]
print("Total Bill Amount =",sum)


