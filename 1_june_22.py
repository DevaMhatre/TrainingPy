# FOR Loop...

# Cities=["Mumbai","Chennai","Delhi"]
# for x in Cities:
#     print(x)

# for x in range(5):              #Range(0,5,1)
#     print(x)

# for x in range(10,20):          #Range(10,20,1)
#     print(x)

# for x in range(10,20,2):      
#     print(x)

# for x in range(10,20,2):
#     print(x)
# else:
#     print("Done")


'''
     Display Fibonacci series up to 10 terms


'''



num1=0
num2=1

print("Fibonacci Series:")

for i in range(10):
    print(res, end =" ")

    res= num1+num2
    num1=num2
    num2=res

'''
0 1 1 2 3 5 8 13 21 34

num1 = 0  num2 =1

res= 0+1 = 1
-----------------------
num1= 1  num2=1

res= 1+1  =2
-----------------------
num1=1  num2=2

res = 1+2 = 3 
-----------------------

for 10 times it will be continued....
'''



# Cities=["Mumbai","Chennai","Delhi"]
# for x in Cities:
#     print(x)
#     if x== "Chennai":
#         break

# Cities=["Mumbai","Chennai","Delhi"]
# for x in Cities:
#     if x== "Chennai":
#         continue
#     print(x)



# a=0
# b=1

# for i in range(10):
#     print(c)
#     c= a+b


#     a=b
#     b=c