def place_order(item):
    
    print(f"order placed: your order is {item}")

def calculate_total(item):
    base_price = 25.5
    VAT = 0.15          
    totalprice = (base_price + len(item)) * (1 + VAT)  
    return totalprice   

def get_order():
    print("prepare order...")
    return "collect your order"

myfood = input("What would you like? ")   
place_order(myfood)
print(get_order())
order_total = calculate_total(myfood)
print(f"Your order costs: R{round(order_total, 2)}")