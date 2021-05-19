# # how to represent
# s={1,2,3,4}
# print(s)   here output=s={1,2,3,4}

# s={1,9,7,4}
# print(s)
# #here we never keeps our format
# #curley braces are used to identify it as sets
# print(type(s))  #to check the type

#to create an empty set
# s=set()   #we cannot use{ }because it is considered as dictionary
# print(s)
# print(type(s))

# to add an element to the set
# s=set()
# print(s)
# s.add(11)   integer
# s.add("chikku")  string
# s.add(0.8) -   float
# s.add(True) -boolean
# print(s)
# we can add different type of elements inside a set

#dulicate elements are not allowed in a set it will consider it as same element only

#create an empty set and add each element the user adds using loop
s=set()

# for i in range (1,10):#range is given to how much elements should be alocated in the set
#     ent =(input("enter the element"))
#     s.add(ent)
# print(s)

#to do operations in a set
# a={1,2,3}
# b={4,5,6,7}
# print(a.union(b))  #add set a  and b
# print(a.intersection(b))  # to find the common in two sets
# print(a.difference(b))  # to find the set a removing elements from b

#we cannot include a set inside a set
#nested sets not possible
s={1,2,3,{5,7,8}}
print(s) #not possible

