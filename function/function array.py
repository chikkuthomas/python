#print a pattern using function
# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()

def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pattern(10)