lst1=[7,8,9,4,3,1]

#if num>5 num+1
#else num-1
# op list = [8,9,10,3,2,0]

# lst1=[7,8,9,4,3,1]
# l=[]
# for i in range(0,len(lst1)): #(0,6)
#     if lst1[i]>5:
#         lst1[i]+=1
#         l.append(lst1[i])
#     else:
#         lst1[i]-=1
#         l.append(lst1[i])
# print(l)
# using lambda ,map function
# in lambda only one argument
#
# The map() function applies a given to function to each item of an iterable and returns a list of the results.
# The returned value from map() (map object) can then be passed to functions like list()
# (to create a list), set() (to create a set) and so on.

op=list(map(lambda num:num+1 if num>5 else num-1,lst1))
print(op)