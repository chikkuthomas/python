# filter function
# find the even numbers from the list

lst=[7,8,9,4,3,1]
evens=list(filter(lambda num:num%2==0,lst))
print(evens)

# here the filter condition is num%2==0
#.......................................................................................................................
lst1=['ajay','arun','nikhil','nivin']
anames=list(filter(lambda name:name[0]=='a',lst1))
print(anames)

#starting with "a" to find first position = name[0]
#.......................................................................................................................