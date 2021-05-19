#to print
#5 4 3 2 1
#4 3 2 1
# 3 2 1
# 2 1
# 1

# for i in range(0,5):          #0           1          2       3     4
#     for j in range(5-i,0,-1): #5,0         4,0        3,0     2,0   1
#         print(j,end=" ")      #5 4 3 2 1   4 3 2 1    3 2 1   2 1   0
#     print()

# for i in range(0,6):
#     for j in  range(0,i):
#         print("*",end=" ")
#     print()

#to print traingle pattern
     #    *
     #   * *
     #  * * *
     # * * * *

# def triangle(n):        #n=5
#     k=2*n-2            #k=2*5-2=8
#     for i in range(0,n): # (0,5)
#         for j in range(0,k): #(0,8)
#             print(end=" ")    #here 8 spaces
#         k=k-1             #k=8-1=7     here each time we need to decrement the space
#         for j in range(0,i+1):
#             print("*",end=" ")
#         print()
# triangle(5)



