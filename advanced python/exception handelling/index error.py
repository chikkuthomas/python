lst=[1,2,3,4]
j=int(input("enter the index value"))
try:
    print(lst[j])
except:
    print("exception occured")  #when the index is out of range,this will be printed
finally:
    print("done")               # finally block will work both the times,i.e,during try and exception block
