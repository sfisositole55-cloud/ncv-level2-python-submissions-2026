#produce 5 cubes
#1: 1**3
#2: 2**3
#3: 3**3
#4: 4**3
#5: 5**3

n = int(input("number: "))

if n < 1:
    print("Invalid input, Enter a number greater than 0.")
else:
    total = 0

    for c in range(1, n + 1):
        cube = c ** 3
        print(cube)
        total = total + cube

    print("cubes total:", total)