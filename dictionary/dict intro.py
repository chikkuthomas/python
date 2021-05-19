#all element in 'key: value' pair

# no duplicate keys allowed

# values can be duplicated

# curly brackets are used

#the given order is satisfied

#dictionary is mutable

dict={'name':"zara",'age':90,'job':'engineer'}
# print(dict)
# print(type(dict))  #to check the type of dictionary
#
# #to acess the value from dictionary
#
# print("dict['name']:",dict['name'])
# print("dict['age']:",dict['age'])
#
# #to create empty dictionary:
#
# dic={}
# print(dict)
# print(type(dic))
#
# #to update an existing entry in dictionary
# dict['age']=35
# print(dict)
#
# # to add new element to the dictionary
#
# dict['college']='GCEK'
# print(dict)
#
# #to add a dictionary to a dictionary
#
dict.update({'location':'kochi'})
print(dict)

# to remove an element
del dict['name']
print(dict)

#to remove all entries
dict.clear()
print(dict)

#to delete that dictionary
del dict
print(dict)