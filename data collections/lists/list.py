# listt=[1,2,3,4,5,6]
# print(listt)  # same order
# print(type(listt))

#all type of datas are supported in a listt

#to create empty listt
# listt=[]
# listt.append("name")  #to add element
# listt.append(10.6)
# listt.append(5)
# listt.append(True)
# print(listt)
#
# listt.remove(5)  #to remove
# print(listt)
# listt.clear() #to clear the listt
# print(listt)
# del listt
# print(listt)
# print(len(a)) to print length of list

# listt=[1,2,3,4,1,2]   #duplicate elements are supported
# print(listt)

# listt=[1,2,3,4,[1,14,17],[1,2,[1,4,4]] ]  #nesting of listt is allowed
# print(listt)
# for i in listt:
#     print(i)

s=[4,5,6,7,8]
res=s[-0]+s[-3]  #s[-0]=s[0]=4, s[-3]=6
print(res)  #answer is 4+6=10

# pop operation in list
lst=[1,2,3,4,5,6,7,8,9,10]
lst.pop(1)
print(lst)   #here that value in the index is removed
lst.pop()   # here the last element is removed

#to make a list into set
st=[1,2,3]
set=set(st)
print(set)
# to make set into list
p=list(set)
print(p)

# to reverse a list
lt=[1,2,3,4,5,6]
lt.reverse()
print(lt)
