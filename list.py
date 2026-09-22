# x=[]
# print(x,type(x))

# x=[10,20,30]
# print(x,x[1])


# #update 
# x[2]=300

# print(x)


# for i in x:
#     print(i)


# #inbuilt function 
# # lenght,minimum,sum,maximum,sorted=[ascending],sorted[x,reverse]=desending 

# x=[3,2,4,1]
# print(len(x),min(x),max(x),sum(x))
# print(sorted(x),sorted(x,reverse=True))


# #methods

# x=[20,30]

# #add elements into the list
# x.append(10)#add elements at the last position
# x.insert(0,40)#insert element at specific position
# print(x)

# #removing elements from the list

# x.pop()#removes last elements 
# x.remove(20)#removes the specific elements 
# x.clear()#delete entire list


# print(x)

# x=[102,304,45,78,8]

# x.sort()#sorts the list
# print(x)

# y=x.copy()
# print(y)

# x.extend([20,30])#extends the list and add the elements
# print(x)

# print(x.index(304))

# x.reverse()#reverses the list
# print(x)


x=[]
ip=int(input("\nEnter the no of elements :"))
for i in range(ip):
    no=int(input("\nEnter the numbers :"))
    x+=[no]


print("\n",x)    
