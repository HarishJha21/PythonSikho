import time

initial=time.time()

k=0
while(k<7):
    print("This is Harish Bhai")
    time.sleep(2)
    k+=1
print("While loop ran in", time.time()-initial, "Seconds")
initial2=time.time()
for i in range(7):
    print("This is Harish Bhai")
print("for loop ran in", time.time()-initial2, "Seconds")

# localtime=time.asctime(time.localtime(time.time()))
# print(localtime)