# different Youtube ki videos dekh ma na smajna ki kosis ki ha

# and = check two or more conditions if True
# and check krti ha ka 2 ya 2 sa zada conditions true ho then wo statement run kare ga

# or = check if atleast one condition is true
# or check kr ha ka bhot sari condition ma sa sirf 1 hi true ho to wo run kr deta ha statement ko

# not = true if condition is false and vice versa
# not check krta ha ka statement ma koi bi na sahi ho then we print kare ga
# not ap ka true chez ko false karar deta ha

# Example: AND logical operators
# temperature=-1

# if temperature > 0 and temperature < 30:
#     print("The tempearture is Good")
# elif temperature < 0:
#     print("The temperature is too cold")
# else:
#     print("The tempeature is too hot")
    
# Example: OR logical opeartor
# temperature=22

# if temperature <= 0 or temperature >= 30:
#     print("The tempearture is bad")
# else:
#     print("The tempeature is normal")
    
# Example: NOT logical opeartor
temperature=22
sunny= False # yahain pr ap True and False dono condition laga kr check krain apna results

if temperature <= 0 or temperature >= 30:
    print("The tempearture is bad")
else:
    print("The tempeature is normal")
    
if not sunny: # Ab ap na yahan pr not ko hata kr bi check karain ka kya ata ha 
    print("IT is sunny outside")
else:
    print("In is cloudy outside")