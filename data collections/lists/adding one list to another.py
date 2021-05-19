#to add the elements for one list to another with iteration in one step

a=['abc','efg','hij']
b=[1,2,3,4]
# a.append(b)  = here nested list will be formed
a.extend(b)
print(a)