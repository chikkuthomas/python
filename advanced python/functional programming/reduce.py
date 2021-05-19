#reduce
# to use map or filter has modules built in already
# but we need to import modules of reduce library
# here we can use 2 parameters in lambda
# only numbers can passed to the reduce function

# import functools
#functools.reduce

from functools import reduce
arr=[1,2,3,4,5,6]
#to find the sum
total=reduce(lambda num1,num2:num1+num2,arr)
print("total:",total)

# to avoid functools while using reduce
from functools import * #[* used to denote reduce here]

# to find the highest numbers
high=reduce(lambda num1,num2:num1 if num1>num2 else num2,arr) # terinary operation-program in single line
print("highest:",high)
