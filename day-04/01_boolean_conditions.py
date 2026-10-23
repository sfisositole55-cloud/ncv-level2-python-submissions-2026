mark=int(input("enter mark:"))

if mark <0 or mark >100:
    
    print("invalid mark:")
elif mark>=75:
    print(" Distinction")
    
elif mark>=50:
    print("pass")   
else :
    print("fail")   