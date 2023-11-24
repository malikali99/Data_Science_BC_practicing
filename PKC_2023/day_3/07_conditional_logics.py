# Logical operators are either True or False / Yes or No / 0 or 1
# Equal to                      ==
# Not equal to                  !=
# less than                     <
# greater than                  >
# Less than and equal to        <=
# GreaterLess than and equal to >=

# Is 4 is equal to 4
# How to write this in python
# Print(4==4)
# print(4==4)
# print(4==5)
# print(4!=2)
# print(4<2)
# print(4>3)

# print(3>=4)
# print(5<=3)
# Check why >= <= came true what is reason behind that? what is in this operators?
# Timestamp: 53:30

# Applications of Logical Operators
# hammad_age=4
# age_at_school=5
# print(hammad_age==age_at_school)
# Agar true aya to hamad school ja sakta ha agar ni to hammad school ni ja sakta


# Input Function and logicals operator
# Dono ko use kr ka check krta hain is example ma 
age_at_school=5
hammad_age=input("How old is hammad? ") #Input Function
# Agar ap hamad_age ma 5 bi put karain ga tab bi answer false aye ga
# Until and unless ap us ko string sa integer ma convert na kr la 
#  Ap beshaq is ko practice kr ka chaeck krain terminal ma kia answer kia a ra ha
# Ab hum string sa integer ma convert krna ka liya ye below step krna ja ra ha
hammad_age=int(hammad_age) # To change the class of hammad_age variable
print(type(hammad_age))
print(hammad_age==age_at_school) # logical operators