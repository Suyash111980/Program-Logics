num = int (input("Enter a Number "))

sum = 0
pro = 1



while num > 0:
    rem = num % 10
    pro = pro * rem
    sum += rem
    num //= 10

print(sum)  
print(pro)

if pro==sum:
    print("Number is spy")

else:
    print("Number is not spy")    