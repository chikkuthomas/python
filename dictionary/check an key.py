dict={'name':'luna',"count":80,'bags':94}
# ele=input("enter the key")
# for i in dict:
#     if i==ele:
#         print("present")
#         break
# else:
#     print("not present")

 #using function
def key(x):
    if x in dict:
        print("present")
    else:
        print(x,"not present")
key('name')