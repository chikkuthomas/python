arr=[10,8,11,9,12]
#to sort in ascending order
arr.sort() #here .sort is used to sort elements
print(arr) # output= [8, 9, 10, 11, 12]

# to sort in descending order
arr.sort(reverse=True)
print(arr) #[12, 11, 10, 9, 8]

#arr.sort()= here sort() act as  a method inside a class
#srt=sorted(arr) = here sorted is a function

#ascending order
srt=sorted(arr)
print(srt)

#descending order
srt=sorted(arr,reverse=True)
print(srt)
# so in the sort function there is (*args,**kwargs)
#because "reverse=True is in the form of keyword argument format