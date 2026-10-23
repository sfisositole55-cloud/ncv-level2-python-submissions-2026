import math
side_a = float(input(" enter side_a:"))
if  side_a  <= 0:
    print(" side cannot less than zero")
    side_a = float(input(" enter side_a:"))
    
side_b = float(input(" enter side_b:"))
if side_b <= 0:
    print(" side cannot less than zero")
    side_b = float(input(" enter side_b:"))

r = math.sqrt((math.pow(side_a, 2) + math.pow(side_b, 2)))
print(r)         