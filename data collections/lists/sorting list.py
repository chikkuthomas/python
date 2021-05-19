#Initialize array
a = [5, 2, 8, 7, 1]
temp = 0
print(a)

#Sort the array in ascending order
for i in range(0, len(a)):
    for j in range(i+1, len(a)):
        if(a[i] > a[j]):
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
#Displaying elements of the array after sorting

print("Elements of array sorted in ascending order: ")
print(a)