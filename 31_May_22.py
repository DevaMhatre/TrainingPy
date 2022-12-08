
# while loop
# while condition:
# if true execute this code

# i= 25
# while i<=30:
#     print(i)
#     i+=1    # i= i+1


# a="HELLO"
# b= len(a)

# i=0
# while i<=b:
#     print(a)
#     i+=1
#     # b+=1
# # print(b)


# BREAK and CONTInue

# # BREAK

# for BREAK   we write    increment statment AFTER  BREAK


# i= 25
# while i<=30:
#     print(i)

#     if i==28:
#         break
#     i+=1                       # i= i+1


# # CONTInue
# for CONTIUE   we write    increment statment BEFORE   Continue

# i= 25
# while i<30:

#     i+=1                        # i= i+1

#     if i==28:
#         continue

#     print(i)

# i= 1
# while i<10:              print(i)

#            i+=1                        # i= i+1

#            else:   print("i is now Greater than 10")


# WRITE a Program to print following using WHile LOOp

# First 10 EVEN ODD Natural Numbers


Num = int(input("Press 1 for EVEN  OR    Press 2 For ODD   OR Press 3 For Natural"))
a = 1
if Num == 1:

    while a <= 10:
        a += 1
        if a % 2 == 0:

            print(a)


elif Num == 2:

    while a <= 10:
        print(a)
        a += 2


elif Num == 3:

    while a <= 10:
        print(a)
        a += 1
