# x=[[1,2],[5,6]]

# print(x)
# print(x[1])
# print(x[1][1])

# #update
# x[0][1]=4

# print(x)


# #add elements 
# x.append([101,103])
# print(x)

# for i in x:
#     print(i)


# for i in x:
#     print(i[0],i[1])


# for i in x:
#     for j in i:
#         print(j)      


          

# x=[101,"hii",True,[10,20],[30,40]]
# print(x)

# for i in x:
#     print(i)


# for i in x:
#     if type(i)==list:
#         for j in i:
#             print(j)

#     else:
#         print(i)             


n=int(input("Enter sublist count :"))

main_list=[]

for i in range(n):
    sub_list=[]
    m=int(input("how many elements want in a list :"))

    for i in range(m):
        value=int(input(f"Enter {i+1} elements :"))
        sub_list.append(value)


    main_list.append(sub_list)
    print("Main List",main_list)        