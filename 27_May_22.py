#Tuple   ()..........

#Stores Multiple DATA intems in Single Variable
# Ordered , Unchangable,  Allows Duplication,  Indexed 
#  
# 


# Cities=("Mumbai", "Chennai", "Delhi")
# print(Cities)

# print(type(Cities)) 

# Cities = tuple(("Mumabai", "Chennai", "Delhi", 50, 50.56, True , False))  #COnstructor  use (())
# print(Cities) 
# print(type(Cities))


# "Mumabi" , "Chennai" , "Delhi", 50 , 50.56 , True , False
# # 0         1           2      3    4       5       6
#-7          -6          -5     -4    -3     -2      -1


# print(Cities[5])                     #Positive Indexing Start from "0"
# print(Cities[-5])                    #Negative Indexing Start from "-1"


# print(Cities[2:5])
# print(Cities[:5])
# print(Cities[2:])


# print(len(Cities))
# Cities.insert("Mandwa")

# Cities=("Mumbai",)
# print(type(Cities))

# Cities=("Mumbai")
# print(type(Cities))

# Cities = tuple(("Mumabai", "Chennai", "Delhi", 50, 50.56, True , False))  #COnstructor  use (())
# x= list(Cities)
# x[2]= "Kolkatta"

# FOR MODIFYING THE TUPLE .....

# x= list(Cities)               #Covert to List 
# x.insert(3,"Punjab")
# Cities= tuple(x)             #COnvert to Tuple
# print(Cities)

# x= list(Cities)               #Covert to List 
# x.append(2,"Udata")
# Cities= tuple(x)             #COnvert to Tuple
# print(Cities)


# Cities=("A","B","C")
# Count=("X","Y","Z")

# newtup= Cities + Count 
# Multup= Cities*2
# print(newtup)
# print(Multup)    #DUPLICATION in Tuple


#-----------------------------------------------------------------------------------------

#Sets..............



#Sets stores  ultiole daat a in single variable

#unordedred , unchangable , duplication not allowed


# Cities = {"Mumbai", "Chennai", "Delhi","Chennai"}

# # for x in Cities:
# #     print(x)

# print("Chennai" in Cities)                        # O / 1  Check the value In the Set



# Cities = {"Mumbai", "Chennai", "Delhi","Chennai"}
# Cities.add("Hariyana")                            #Added data into The List        
# print(Cities)

# Countries= ("India", "UK","US")
# Cities.update(Countries)                          #Updated  List to the SET
# print(Cities)



# Cities = {"Mumbai", "Chennai", "Delhi","Chennai"}
# print(Cities) 

 
# Cities.remove("Mumbai")                            #Can REMOVE also in Stes!!

# a= Cities.pop()                                    #Randomly Removes Value
# print()

# Cities.clear()

# del Cities                                           #Delets the WHOLE variable



# # Cities.discard("Punjab")
# print(Cities)



# ------------------------------------------------------------------------------
#
#Dictionary............

#Dicrtionary= Key:Value
# Ordered , Changable , Duplication NOT Allowed   #If we try to Duplicate It will OverWrite 

newdictionary= {"Name": "Mike",
                "RollNo":"126",
                "Age":"20"} 


# newdictionary["BirthMonth"] ="DEC"                #ADDing VAlue to Dictionary

# print(newdictionary)

# # print(newdictionary["RollNo"])

# print(type(newdictionary))

# print(len(newdictionary))

# newdictionary.pop("RollNo")                    #Pop the Particular Value

# newdictionary.popitem()                        #Pop the DATA at the Last

# del newdictionary["Name"]                        #Delet the Key

# newdictionary.clear()

print(newdictionary.get("Age"))
print(newdictionary.keys())
print(newdictionary.pop("Age"))
newdictionary.update({"Location":"Alibag"})

print(newdictionary)
