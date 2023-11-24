# What is type conversion?
# 1 type ko dosri data type ma convert krna ko kehta hain type conversion.

# Now there are two types of type conversion
# 01. Implicit Type conversion:
# Is ma python ka convertor khud hi type change kr deta ha
# Example of Implicit Type conversion
# a=34
# b=33.3
# c=a+b
# print(c,type(c)) # Now you that the type of c is float # python na khud hi type check kr li ha

# 02. Explicit Type conversion: Also called type casting
# is ma user ko khud sa built in fuction ki help sa type change krni hoti ha
# Example of explicit Type conversion
p='345'
q=342
p=int(p) # Now you see that we change their type from string to integer..
s=p+q
print(s,type(s)) 