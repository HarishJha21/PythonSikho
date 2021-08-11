n=int(input("Enter number of rows:"))
print("Enter 1 for 'True' or 0 for 'False'")
a=int(input())
boolean=bool(a)

if boolean==True:
    for i in range(n):
        print("* " * (i+1))
else:
    for i in range(n):
        print(("* " * (n-i)))


