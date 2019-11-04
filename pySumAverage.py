#Sum/Average Program
#Brandon Garsson
#s1293728

x=1
numbers=[]

while x<=20:
    n=input("Enter a number: ")
    numbers.append(n)
    x=x+1

sum=int(numbers[0])+int(numbers[1])+int(numbers[2])+int(numbers[3])+int(numbers[4])+int(numbers[5])+int(numbers[6])+int(numbers[7])+int(numbers[8])+int(numbers[9])+int(numbers[10])+int(numbers[11])+int(numbers[12])+int(numbers[13])+int(numbers[14])+int(numbers[15])+int(numbers[16])+int(numbers[17])+int(numbers[18])+int(numbers[19])
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
