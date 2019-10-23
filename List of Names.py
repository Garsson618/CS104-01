x=1
end=False
names=[]

while x<=10:
    n=input("Enter Name #"+str(x)+": ")
    names.append(n)
    x=x+1

while end == False:
search=input("\nSearch for a name (type 'e' to stop")
if search in names:
    print(search," was found")
else:
    if search="e":
    end=True
    else:
    print (search," was not found")
