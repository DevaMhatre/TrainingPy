'''
Q1.   Calculate Electricity Bill

accespt number of Unit from user 

First 100 Units     No charge
Next 100 Units      Rs. 5 per Unit
Next 200 Units      Rs. 10 per Unit


for 
Unit 215   >>    0 + 500 + 15 = 650


'''


# Unit = int(input("Enter your Bill Units: "))


# if Unit<=100:
#     print("No Charge")


# elif Unit >= 100 and Unit <= 200:
#     b= Unit- 100
#     print (b* 5)

# elif Unit>200:
#     a= Unit -200

#     print(a*10 + 500)


'''
Q.2 Check wheather Last DIgit of No. is  Divisible by 5
'''

# Num= int(input("Enter a Num"))

# a = Num%10

# if a%7 == 0:
#     print(Num," It is Divisible By 7")

# else:
#     print(Num," Not Divisible")




'''
Q.3 Accept %  and Display Grades Accordingly

Marks                    Grade
>90                         A
>80 and <90                 B
>= 60 and <= 80             C
below 60                    D
'''

# Per= int(input("Enter Your Percentage:"))

# if Per> 90:
#    print("A Grade")

# elif Per>80 and Per<=90:
#     print("B Grade")

# elif Per >=60 and Per <= 80:
#     print("C Grade")

# elif Per< 60:
#     print("D Grade")


'''
Q.4 Accept Cost Price & Display Tax to be paid 

Cost Price                              TAX

> 100000                                15%
> 50000 and <= 100000                   10%
<= 50000                                5%
'''

# CP= int(input("ENter thr Cost Price of Your Bike:"))

# if CP >100000:
#     print("You have to pay 15% TAX of Your Cost Price of Bike ", )
#     print (CP*(15/100))
# elif CP >50000 and CP<= 100000:
#     print("You have to pay 10% TAX of Your Cost Price of Bike ", )
#     print (CP*(10/100))
# elif CP <=50000:
#     print("You have to pay 5% TAX of Your Cost Price of Bike ", )
#     print (CP*(5/100))

'''
Q5. Accept Num , from 1-7 , for 1 Sunday.... and so on
'''
# WEEK={  1:"Sunday",
#         2:"Monday",
#         3:"Tuesday",
#         4 : "Wednesday",
#         5: "Thursday",
#         6:"Friday",
#         7:"Saturday"


# }

# Num= int(input("Enter a Num from 1-7 :"))
# if Num<= 7:
# print(WEEK[Num])

'''
Q.6 Check wheater i/p num is divisible by 2 and 3
'''

Num= int(input("Enter Number:"))


