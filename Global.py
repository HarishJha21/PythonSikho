# l=10 #Global
# def function1(n):
#     # l=5 #local
#     m=8 #local
#     global l
#     l=l+33
#     print(l,m)
#     print(n, "I have printed")

# function1("This is Harish")
# # print(m)
x=88
def Harish():
    x=19
    def anshuman():
        global x
        x=87
    # print("before calling anshuman()",x)
    anshuman()
    print("after calling anshuman()",x)

Harish()
print(x)
