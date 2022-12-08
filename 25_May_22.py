#BOOLEAN PART__________________________________________________________________________


# print(5>10)
# print(5<10)
# print(5==10)


# print(bool("Hello BOSS"))  #Gives TRUE 
# print(bool())              #Gives FALSE... STRING is EMpty


# x= 5
# y= 10

# if x>y:
#     print("x is GREATER")

# else:
#     print("Y is GREATER")



#OPERATORS__________________________________

# 1. ARITHMATIC  (+-*/)
# 2. Assignment 
# 3. Comparision
# 4. LOGICAL     (AND OR NOT)
# 5. Indentity
# 6. MemberShip
# 7. BitWise 

# ___________________________________________


# Arithmstic [+-*/]

# a= 10
# b= 5

# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a%b) # MOodulus  ..... gives Remender 
# print (a**b) # Exponential a^b


# #Let,
# a= 2
# b= 4
# print(a**b) #  (a)^4 

# # 2*2*2*2 = 2^4

#-----------------------------------------

# # AssignMent 

# a= 10
# b= 5

# print(a+=b)
# print(a-=b)
# print(a*=b)
# print(a/=b)
# print(a%=b) # MOodulus  ..... gives Remender 

#------------------------------------------

# # Comparison
# x= 10 
# y= 5

# print(x==y,"    Equal TO" )  #Equal TO
# print(x!=y,"    NOT Equal TO")  #NOT Equal TO

# print(x>y,"     Greater Than...")              #Greater Than...
# print(x<y,"     Less Than...")                 #Less Than...
# print(x>=y,"    Greater Than OR Equal To...") #Greater Than OR Equal To...
# print(x<=y,"    LESS Than  OR Equal To...")    #LESS Than  OR Equal To...

# -------------------------------------------

# # LOGICAL.......
# x=10 

# print(x>5 and x>15)
# print(x>5 or x>15  )
# print(not x )




#----------------------------------------------

#identity......

# x=("HELLO")
# y=("HELLO")
# z=("HELLO")

# print(x is y)
# print( x is not y)
# print(x is z)

# ----------------------------------------------

# # MEMBERship......

# sent="Python is a high - level, interpeted, general-purpose programming language."
# print("level" in sent)

# print("CLASSES" not in sent)


# -----------------------------------------------


# _______________________________________________________________________________________


# List ......................



#Store Collection of DATA

#ordered = data is added to to list in ordered fashion ....
# changable= can be modified....
# allows duplication = 
#index = no. is given to location of data...

# 1. list         []       = ordered , changable , allows to duplicate , indexed (Store multiple data/ collection of data, in single variable)
# 2. Tuple        ()       = ordered , unchangable , allows to duplicate ,       (NEGATIVE Indexing)  "indexed"

# 3. Set          {}       = unordered, unchangable, can't duplicate, unchangable , unidexed 
# 4. Dictionary  {Key:Value}    = ordered , changable , can't duplicate ,                     "keyvalue"
 


## List ()..........................


# Cities= ["Mumbai", "Chennai", "Delhi"]   
# print(Cities)

# Cities = list(("Mumabai", "Chennai", "Delhi", 50, 50.56, True , False))  #COnstructor  use (())
# print(Cities)

# print(len(Cities))     # Length Starts from "1" .....  and Index Starts from "0"

# print(type(Cities))

# "Mumabi" , "Chennai" , "Delhi", 50 , 50.56 , True , False
# # 0             1           2      3    4       5       6

# print(Cities[1])

# Cities[2]= "Punjab"                #just replaces the data
# print(Cities)

# Cities.insert(1,"MP")              # New value is added and original value is shifted.....
# print(Cities)

# Cities.append("Rajsthan")            # by default add new value at the END!
# print(Cities)

# Countries= ["India", "US", "UK"]
# Cities.extend(Countries)
# print(Cities)

# Cities.remove("Mumbai")    #Removes the value .... When we have to dlt particular data

# print(Cities)
# Cities.pop(1)             #Pop th value at th Index....but Index is still there

# Cities.pop()

# del Cities[1]             #  totally delete that particular INDEX

# del Cities 

# Cities.clear()

# print(Cities)









Cities= ["Mumbai", "Chennai", "Delhi"]
for x in Cities :                        #Data in the list is PRINTED Numerically...
    print(x)

# mylist = ["Mumbai", "Chennai", "Delhi","India", "US", "UK"]
# mylist[1:3] = ["Russia", "Africa"]

# print(mylist)  # Chennai and Delhi is REPLACEd by RUSSIA AND AFRICA    because of 1:3 .......COnsider from 1-2 last index is ignored