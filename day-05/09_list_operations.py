marks = []   
i = 0        

mark = int(input("Enter marks (or -1 to stop): "))  

while mark != -1:            
    marks.append(mark)       
    i += 1                   
    mark = int(input("Enter marks (or -1 to stop): "))  

print(f"Our list has {len(marks)} elements")  

print("Marks:", end=" ")           
for x in range(len(marks)):        
    print(marks[x], end=" ")       
print()                            

total_sum = 0                                 
for x in range(len(marks)):
    mark = marks[x]                           
    total_sum = total_sum + mark              

print(f"The sum of all marks = {total_sum}")  

total = 0
for x in range(len(marks)):
    mark = marks[x]
    total = total + mark

if len(marks) > 0:                            
    avg = total / len(marks)                  
    print(f"The average of all marks = {avg}")
else:
    print("No marks were entered, so there is no average.")