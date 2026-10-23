mark=int(input("enter mark:"))

if mark <0 or mark >100:
    
    print("invalid mark:")
    int(input("enter mark:"))
    
if mark >= 80:
    print("outstanding:")
    
elif mark>=70:
    print("highly competent")
    
elif mark>=50:
    print(" competent")
    
elif mark>=40:
    print("Not yet competent")   
else :
    print(" not achieved")
        
    

    
    


