print("Enter the numbers of the list one by one\n")
size=int(input("Enter size of list\n"))
mylist=[]
for i in range(size):
    mylist.append(int(input("Enter list element\n")))

# mylist=[5,4,3,2,1]
print(f"Your list is {mylist}\n")

reverse1=mylist[:]
reverse1.reverse()

reverse2=mylist[::-1]
print(f"My first reversed list of {mylist} is {reverse1}\n")
print(f"My second reversed list of {mylist} is {reverse2}\n")

reverse3=mylist[:]
for i in range(len(reverse3)//2):
    reverse3[i], reverse3[len(reverse3)-i -1]=reverse3[len(reverse3) -i -1], reverse3[i]
    # print(f"the reverse list at i={i} is {reverse3}")

print(f"My third reversed list of {reverse3} is {reverse3}\n")
if reverse1==reverse2 and reverse2==reverse3:
    print("All three methods give same result")

