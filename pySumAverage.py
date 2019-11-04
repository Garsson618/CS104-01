#Sum/Average Program
#Brandon Garsson
#s1293728

x=1
sum=0

while x<=20:
    n=input("Enter a number: ")
    x=x+1
    sum=sum+int(n)

print("\nThe sum of the numbers you entered is: "+str(sum))
print("The average of the numbers you entered is: "+str((float(sum)/20)))


#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
