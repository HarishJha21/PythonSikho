test = int(input("Enter the number of test cases\n"))
lst = []
for i in range(test):
    lst.append(int(input("Enter your number\n")))

for num in lst:
    print(f"The next Palindrome for {num} is", end=" ")
    while True:
        if str(num) == str(num)[::-1]:
            print(num)
            break
        else:
            num += 1