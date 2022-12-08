#Min>> Sec

# def MinSEC(Min):
#    return Min*60
# MinSEC(2)
# ---------------------------------------------------------------
# #remainder

# def remm(Numb1,Numb2):
#     print(Numb1%Numb2)

# remm(12,5)

# #list
# lstt=[1,2,3,4,5]

# def list_less_than_100(lstt):
#          print(sum(lstt))

# list_less_than_100(lstt)

# -----------------------------------------------------------------
# #2string 

# def comp(str1,str2):
#     if len(str1)==len(str2):
#         print("True")
#     else:
#         print("False")

# # str1="ABS"
# # str2="CFFF"
# comp("ABS","CFF")
# -----------------------------------------------------------------------
# #is Upper or lower

# def string_cal(strr):
#     cout=0
#     cou1=0

#     for x in strr:
#         if x.islower():
#                cout+=1
#         elif x.isupper():
#               cou1+=1
#     print("The No of lower case words is ",cout)
#     print("The No of upper case words is ",cou1)
    
# # strr="abcDEF"
# string_cal("The quick Brown Fox")

# ------------------------------------------------------------
# # list1=[1,2,3,3,3,3,4,5]

# unique_list=[]

# def search(list1):
#     for x in list1:
#         if x not in unique_list:
#             unique_list.append(x)

#     print(unique_list)

# search(list1=[1,2,3,3,3,3,4,5])
# -----------------------------------------------------------------------------

# even=[]
# odd=[]

# def sort_even_odd(list1):
#     for x in list1:
#         if x%2==0:
#             even.append(x)
#         else:
#             odd.append(x)
#     print("The even List is ",even)
#     print("The odd List is ",odd)

# sort_even_odd(list1=[1,2,3,4,5,6,7,8,9])


# --------------------------------------------------

fruits=["mangoo","apple","banana"]

newlist=[i for i in fruits if "a" in i]  # print i ,  for i in fruits , if there is "a" in i!

# ---------------------------------------------
