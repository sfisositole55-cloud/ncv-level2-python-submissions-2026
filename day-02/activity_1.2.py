

# activity 1,2 highest common factor
first_number = int(input("Enter the first number: "))    
second_number = int(input("Enter the second number: "))   


if first_number < second_number:
    factor = first_number     
else:
    factor = second_number     

while first_number % factor != 0 or second_number % factor != 0:
    print("Error:", factor, "is not a common factor")   
    factor = factor - 1
    
print("The highest common factor of", first_number, "and", second_number, "is", factor)