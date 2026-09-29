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








starter = ['a', 'b', 'c']
starterprice = [150, 200, 120]

maincourse = ['a', 'b', 'c']
mainprice = [250, 220, 180]

dessert = ['a', 'b', 'c']
dessertprice = [100, 80, 150]


order = []

b = 1

while b == 1:

    print("")
    
    print("             HOTEL MENU")
    print("======================================")
    print("1. Starter")
    print("2. Main Course")
    print("3. Dessert")
    print("======================================")

    choice = int(input("What do you want to order : "))


  
    if choice == 1:

        print("")
        print("----------- STARTER -----------")

        j = 0
        o = 0

        for i in starter:

            print((o+1), " ", i, " ", starterprice[j])

            j += 1
            o += 1

        on = int(input("Enter order number : "))

        if on >= 1 and on <= len(starter):

            order.append(["Starter", on])

            print("One order placed")

        else:
            print("Invalid order number")


    elif choice == 2:

        print("")
        print("--------- MAIN COURSE ---------")

        j = 0
        o = 0

        for i in maincourse:

            print((o+1), " ", i, " ", mainprice[j])

            j += 1
            o += 1

        on = int(input("Enter order number : "))

        if on >= 1 and on <= len(maincourse):

            order.append(["Main", on])

            print("One order placed")

        else:
            print("Invalid order number")


    
    elif choice == 3:

        print("")
        print("----------- DESSERT -----------")

        j = 0
        o = 0

        for i in dessert:

            print((o+1), " ", i, " ", dessertprice[j])

            j += 1
            o += 1

        on = int(input("Enter order number : "))

        if on >= 1 and on <= len(dessert):

            order.append(["Dessert", on])

            print("One order placed")

        else:
            print("Invalid order number")


    else:

        print("Invalid choice")


    print("")
    b = int(input("Do you want to order again? Press 1 for Yes : "))




print("")
print("======================================")
print("              YOUR BILL")
print("======================================")

total = 0

for k in order:

    category = k[0]
    number = k[1]


    if category == "Starter":

        print(starter[number-1], " Rs.", starterprice[number-1])

        total += starterprice[number-1]


    elif category == "Main":

        print(maincourse[number-1], " Rs.", mainprice[number-1])

        total += mainprice[number-1]


    elif category == "Dessert":

        print(dessert[number-1], " Rs.", dessertprice[number-1])

        total += dessertprice[number-1]


print("--------------------------------------")

print("Total Bill Amount = Rs.", total)


print("          THANK YOU VISIT AGAIN")















