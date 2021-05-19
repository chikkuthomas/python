a=[4,2,6,1]
temp=0
print(a)
print("elements of list to be sorted:")
for i in range(0,len(a)):
    print(a[i],end=" ")
for i in range(0,len(a)):
    for j in range(i+1,len(a)):
        if(a[i]<a[j]):
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
print()
print("list after sorting elements in ascending order:")
print(a)
#...............................................................................................................
#EXPLANATION
#   a=[4,2,6,1]
#   for i in range(0,4)
#       for j in range(i+1,4)
# when i=0, j=(1,4)
#           j=1
#      a[0]=4,a[1]=2
#       4>2 (no  change) ,a=[4,2,6,1]

#           j=2
#     a[0]=4, a[2]=6
#       4<6
#   a[0]=6, a[2]=4 ,  a=[6,2,4,1]

#          j=3
#  a[0]=6, a[3]=1
#     6>1, no change, a=[6,2,4,1]

# i=1,j=(2,4)
# a[1]=2, a[2]=4
#    2<4
# a[1]=4, a[2]=2,  a=[6,4,2,1]

#NOW SINCE ALL THE ELEMENTS ARE IN DESCENDING ORDER
#THE LOOP WILL EXIT AND WE NEED TO PRINT THE OUTPUT