#to slice a list- to make the list into two
a=[1,2,3,4,5,6,7,8,9]
print(a[0:3]) # to take elements from 1st postion till 3rd position. i.e= 1,2,3
print(a[-5:-1]) #to take elements from last 4 positions
print(a[:5]) #to take elements till 5th,considered as from 0 to 5th
print(a[4:]) #from 4th to last

#to update the list- to change an element to another (list and set are mutable)
print(a)
a[0]=44  # 1 in 0th position is changed to 44
print(a)