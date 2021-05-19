# functions in lambda
#map = to aplly function to all elements
#filter = to filter out the elements using condition and give filtered statements
#reduce = to get single element output

#1) MAP FUNCTION
arr=[2,3,4,5,6]
# def square(num):
#     return num**2

squarelist=list(map(lambda num:num**2,arr))
print(squarelist)

#list to convert the map to list
# lamda fn to make the condition directly in map function
# arr to get the iterable from list arr
# lambda is used to reduce the code length , or consise
#.......................................................................................................................
# to convert to upper case

lst=['ajay','arun','nikhil','nivin']
def upper(name):
    return name.upper()

# hello.upper() = HELLO

uppername=list(map(lambda name:name.upper(),lst))
print(uppername)