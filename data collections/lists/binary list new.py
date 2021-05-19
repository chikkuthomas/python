# a=[1,2,3,4,5]
# def bsearch():
#     a.sort()
#     ele=int(input("enter the element"))
#     flag=0
#     low=0
#     upp=len(a)-1
#
#     while low<=upp:
#         mid=(low+upp)//2   #MID POSITION IS ALWAYS LOW+UPP // 2
#
#         if ele>a[mid]:
#             low=mid+1
#         elif ele<a[mid]:
#             upp= mid-1
#         elif ele==a[mid]: #THIS IS THE MAIN ALGORITHM FOR BINARY SEARCH
#             flag=1
#             break
#     if flag==1:
#         print("found")
#     else:
#         print("not found")
# bsearch()

#........................................................................................................................

# USING RECURSION

#  COMPARE X WITH THE MIDDLE ELEMENT
#  F X MATCHES WITH THE MIDDLE ELEMENT,WE RETURN THE MID INDEX
#  ELSE IF X> THE MID ELEMENT, THEN X CAN LIE IN THE RIGHT SUBARRAY AFTER THE MID EEMENT.SO WE RECUR THE FIRST HALF.
#  ELSE IF X< MID ELEMENT, RECUR THE LEFT HALF.

# A RETURN IS USED TO END THE EXECUTION AND RETURN THE VALUE OF EXPRESSION TO THE CALLER

def bsearch(a,low,upp,x):
    a.sort()
    if(low<=upp):
        mid=(low+upp)//2
        if(x==a[mid]):
            return 1
        elif(x>a[mid]):
            return bsearch(a,mid+1,upp,x)
        elif(x<a[mid]):
            return bsearch(a,low,mid-1,x)
    else:
        return 0
a=[1,5,2,7,3]

# function call
result=bsearch(a,0,len(a)-1,7)
if result==1:
    print("found")
else:
    print("not found")
