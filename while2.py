        
# i=1
# n=20

# tot=0
# sqr=0

# while i<=n:
#     if(i%5==0):
#         sqr=i*i
#         tot=sqr+tot
        
#     i+=1
    
# print(tot)  
# 
# 
# 
#   

# i=1
# n=10
# sq=0
# cube=0
# tot=0

# while i<=n:
#     print(f"\n",(i),(i*i),(i*i*i))
    
#     i+=1   

num = 123

sum = 0

rev = 0

while num > 0:
    rem = num % 10
    sum += rem
    num //= 10

print(sum)  