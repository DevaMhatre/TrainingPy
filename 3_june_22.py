# FUNCTIONAL Programming
'''
def FuncName(Parameters)
    logic 
    return/print
FuncName(Argument)
'''


def add(a, b):
    # return a+b

    print(a+b)

# result= add(20,25)
# print(result)


'''
if condition (true):
    print(if)
else:
    print(else)

basics(if-else,for-while loops)
functions
oops
'''
'''

Q1:-
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
             Unit                                                     Price  
First 100 units   0-100                                            no charge
Next 100 units    101-200                                           Rs 5 per unit
After 200 units      >200                                       Rs 10 per unit

215    0 + 500 + 150
amount = 500+150 = 650

'''
# unit = int(input("Enter the number of units consumed for a month\n"))
# print(unit)
# if unit <= 100 :
#     elec_bill = 0
#     print("electricity bill :",elec_bill)
# elif 100 < unit <= 200:
#     x1 = unit - 100
#     elec_bill = x1 * 5
#     print("electricity bill :",elec_bill)
# else :
#     x1 = unit - 200
#     elec_bill = 500 + x1 * 10
#     print("electricity bill :",elec_bill)


# def Bill(Unit):
#     if Unit <= 100:
#         print("electricity bill : No Charge")

#     elif 100 < Unit <= 200:
#         x1 = Unit - 100
#         EleBill = x1 * 5
#     print("electricity bill :", EleBill)

#     else:
#     x1 = Unit - 200
#     EleBill = 500 + x1 * 10
#     print("electricity bill :", EleBill)


# '''
# Q2:-
# Write a program to check whether the last digit of a number( entered by user ) is
# divisible by 7 or not.
'''
def check(Num):
    Last_Digit= Num%10
    Result= Last_Digit%7

    if Result==0:
        print("Divisible By 7")
    else:
        print("Not Divisible by 7")

'''

# Q3:-
#  Write a program to accept percentage from the user and display the grade according to the following criteria:

#          Marks                                    Grade
#          > 90                                         A
#          > 80 and <= 90                               B
#          >= 60 and <= 80                              C
#          below 60                                     D

'''
def Marks(Per):
    if Per> 90:
     print("A Grade")

    elif Per>80 and Per<=90:
     print("B Grade")

    elif Per >=60 and Per <= 80:
     print("C Grade")

    elif Per< 60:
     print("D Grade")

'''

# Q4:-
# Write a program to accept the cost price of a bike and display the road tax to be paid according to the following criteria :

#         Cost price (in Rs)                                       Tax
#         > 100000                                                  15 %
#         > 50000 and <= 100000                                     10%
#         <= 50000                                                  5%



# print("ENter thr Cost Price of Your Bike:")
# def CP(Num):
#     if CP >100000:
#      print("You have to pay 15% TAX of Your Cost Price of Bike ", )
#      print (CP*(15/100))
#     elif CP >50000 and CP<= 100000:
#      print("You have to pay 10% TAX of Your Cost Price of Bike ", )
#      print (CP*(10/100))
#     elif CP <=50000:
#      print("You have to pay 5% TAX of Your Cost Price of Bike ", )
#      print (CP*(5/100))


# Q5:-
# Write a program to accept a number from 1 to 7 and display the name of the day like 1 for Sunday , 2 for Monday and so on.


# Q6:-
# Write a program to whether a number (accepted from user) is divisible by 2 and 3 both.

# Q7:
#  Write a program to check a character is vowel or not.

# #Q6:-
# num = int(input("Enter a number"))
# if(num%2==0 and num%3==0):
#     print("The number is divisible by both 2 and 3")
# else:
#     print("Number is not divisible by 2 and 3")

# #Q7:-
# # word = input("Enter a character:")
# # ch = word.lower()
# # if( ch=='a'or  ch=='e'  or ch=='i' or ch=='o' or  ch=='u'):
# #     print(ch,"Is a vowel")
# # else:
# #     print(ch,"Is not a vowel")


# # vowel = ['a','e','i','o','u']
# # char = input("Enter the Character\n")
# # if char.lower() in vowel :
# #     print("Input character is Vowel")
# # else :
# #     print("character is not vowel")

# # word = input("enter a random string:-")
# # word = word.lower()
# # for i in word:
# #     if i in "aeiou":
# #         print("its vowel")
# #     else:
# #         print("its not a vowel")

# #Q5. Accept Num , from 1-7 , for 1 Sunday.... and so on

# WEEK={  1:"Sunday",
#         2:"Monday",
#         3:"Tuesday",
#         4 : "Wednesday",
#         5: "Thursday",
#         6:"Friday",
#         7:"Saturday"
# }

# Num= int(input("Enter a Num from 1-7 :"))
# if Num <= 7:
#     print(WEEK[Num])
# else:
#     print("Hey you have enter the wrong number pls verify!")


# CP = int(input("Enter the cost price of the bike:"))
# if(CP>100000):
#     print("Tax on your bike is 15%")
# elif(CP>50000 and CP<=100000):
#     print("Tax on your bike is 10%")
# elif(CP<=50000):
#     print("Tax on your bike is 5%")

# # 1000 pay 10% ==   1000+100 = 1100


# CP= int(input("ENter thr Cost Price of Your Bike:"))

# if CP >100000:
#     print("You have to pay 15% TAX of Your Cost Price of Bike ", )
#     print (CP * (15/100))
# elif CP >50000 and CP<= 100000:
#     print("You have to pay 10% TAX of Your Cost Price of Bike ", )
#     print (CP* (10/100))
# elif CP <=50000:
#     print("You have to pay 5% TAX of Your Cost Price of Bike ", )
#     print (CP * (5/100))


# percentage = int(input("Enter your percentage: "))

# if percentage > 90:
#   print("Grade : A")
# elif percentage > 80 and percentage <=90:
#     print("Grade : B")
# elif percentage >= 60 and percentage <= 80:
#     print("Grade : C")
# else:
#     print("Grade : D")


# unit = int(input("Enter the number of units consumed for a month\n"))
# print(unit)
# if unit <= 100 :
#     elec_bill = 0
#     print("electricity bill :",elec_bill)
# elif 100 < unit <= 200:
#     x1 = unit - 100
#     elec_bill = x1 * 5
#     print("electricity bill :",elec_bill)
# else :
#     x1 = unit - 200
#     elec_bill = 500 + x1 * 10
#     print("electricity bill :",elec_bill)
# '''
