# # a list comprehension are used for creating new lists from iterables.
# # As list comprehensions return lists, they consist of brackets containing the expression,
# # which is executed for each element along with the for loop to iterate over each element

# LIST COMPREHENSION
numbers =[1,2,3,4]
squares=[n**2 for n in numbers]
print(squares)