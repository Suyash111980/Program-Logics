car={
    "maruti":10000,
    "Toyota":20000,
    "bmw":500000
};
sum=0
for i in car:
    # print(i," \t",car.get(i))
    sum+=car.get(i)
print(sum)    


#functions
#1.lenght (len) 
#2.Minimum (min)
#3.Maximum (max)#ut returns the value based on the ascii value of the keys first word  
#4.Sorting (sorted)

#methods 
#1. Update --- add-->update if the key is present--->updates the existing value 
#                    if the key is not presnt --->inserts the new value 

# car.update({"bmw":100})
# print(car)
# car.update({"xuv":200})
# print(car)


# # 2.remove methods -- 1.pop() 2.popitem() 3.clear()
# car.pop("maruti") #removes specific key value pair
# print(car)
# car.popitem() #removes last key value pair
# print(car)
# car.clear()  #removes the entire dictionary
# print(car)

# all keys 
print(car.keys())
print(car.values())
print(car.items())

for keys in car:
    print(keys)

for v in car.values():
    print(v)

for kv in car.items():
    print(kv)

for k,v in car.items():
    print(k,v)



max=0
for i in car.items():
    if i[1]>max:
        max=i[1]
        maxcar=i[0]


print(max,"\t",maxcar)   



    


