x=[]
r=[]
try:
    n=int(input("How much number you want to insert in list \n"))
    for i in range(n):
        t=int(input("Please input the numbers "))
        x.append(t)
        if t>10:
            while True:
                t=t+1
                p=str(t)
                if p==p[::-1]:
                    r.append(p)
                    break
                else:
                    continue
        else:
            r.append(t)
    print(r)
except Exception as e:
    print(e)

