# list comprehension
arr=[1,2,3,4,5]
squares=[num**2 for num in arr]
print(squares)

dbl=[num*2 for num in arr]
print("double:",dbl)

fruits=['mango','apple','orange']
# op: [('mango','mango'),('apple',apple'),('orange','orange')]
pairs=[(fruit,fruit) for fruit in fruits] # always give a relatable name as iterable
print(pairs)

lst1=[1,2]
lst2=[10,20]
#[(1,10),(1,20),(2,10),(2,20)]
lst=[(num,num1) for num in lst1 for num1 in lst2]
print(lst)

# even number list
l=[10,21,30,41,50,62]
evens=[num for num in l if num%2==0  ]
print(evens)

lst3=[7,8,9,4,2]
# 8,9,10,3,1
l1=[num+1 if num>5 else num-1 for num in lst3 ]
print(l1)

