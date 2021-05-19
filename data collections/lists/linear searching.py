def linear():   # can be used to search for integers
    inp=int(input("enter the element"))
    a=[1,2,3,4,5,6]
    for i in a:
        if i==inp:  #use== when using integer
            print(i,"is in list")

linear()