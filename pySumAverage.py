#Sum/Average Program
#Brandon Garsson
#s1293728

x=1
y=0
sum=0
numbers=[]

while x<=20:
    n=input("Enter a number: ")
    numbers.append(n)
    x=x+1

while y<=19:
    sum=int(numbers[y])+sum
    y=y+1

print("\nThe sum of the numbers you entered is: "+str(sum))
print("The average of the numbers you entered is: "+str(float(sum)/len(numbers)))


#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
