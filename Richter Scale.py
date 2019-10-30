#Python Richter Scale Calculation
#Brandon Garsson
#s1293728

gameOver=False

print("Enter the Richter scale value or -99 to end: ")
while gameOver==False:
    r=float(input("Enter the Richter value: "))

    if r >= 8.0:
        print("Most structures will fall\n")

    elif r >= 7.0:
        print("Many buildings destroyed\n")

    elif r >= 6.0:
        print("Many buildings considerably damaged, some collapse\n")

    elif r >= 4.5:
        print("Damage to poorly constructed buildings\n")

    elif r > 0.0:
        print("No destruction of buildings\n")

    elif r <= 0.0 and r != -99.0:
        print("Value must be greater than 0\n")
    
    if r == -99.0:
        gameOver=True
    
