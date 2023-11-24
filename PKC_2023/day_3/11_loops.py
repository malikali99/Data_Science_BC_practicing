# Timestamp: 01:39:00
# Loops:
# bar bar kisi chez ko use krna ka liya hum loops ko use krta hain
# Now in Loops, there are two types of loops.
# While and For Loops
# 01. While loop

# x=0
# while x<=5:
#     print(x)
#     x=x+1

# 02. For loop

# for x in range (4,10):
#     print(x)
    
# Now how to use this loop in program

# for example hum na 1 array baney ha

#array
# days = ["Mon","Tue","wed","thru","fri","sat","sun"]

# for d in days:
#     print(d)
    
# we use logical opeartors
days = ["Mon","Tue","wed","thru","fri","sat","sun"]

for d in days:
    if (d=="fri"):break     # loops stop
    # if(d=="fri"):continue # in dono ko ap alag alag laga kr check karain
    print(d)