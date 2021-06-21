try:
    n=int(input('Enter the value for the n :'))
    mx=int(input('Enter the value for the mx :'))
    mn=int(input('Enter the value for the mn :'))

except ValueError:
    print('Enter integers only ')
    exit()

if mn>=mx:
    print('This can not be the range as the min should be less than max')

for i in range (mn,mx+1):
    if n%i==0:
        print(i,'is a divisor of',n)
    else:
        print(i,'is not a divisor of',n)