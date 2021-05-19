#
# # do operations in stack
#
# list = [] #need to put a list=[],otherwise error will come, also in the outer loop
# def push():
#     for i in range(0, 4):
#         ele = int(input("enter the element"))
#         list.append(ele)
#
# def pop():
#
#     list.pop()
#
# print("select the operation")
# print("1.push")
# print("2.pop")
# print("3.display")
# while True:
#     op=input("choose the operator")
#     if op in ('1','2','3'):
#         if op=='1':
#             push()
#         if op=='2':
#             pop()
#         if op=='3':
#             print(list)
#             if list == []:
#                 break
#
#
# STACK OPERATION ANOTHER METHOD #
stk=[]
size=int(input("enter the size"))
top=0

n=0
def push():
    global top,size
    if(top>size):
        print("stack is full")
    else:
        p=int(input(" enter the element want to push"))
        stk.append(p)
        top+=1
def pop():
    global top, size
    if(top<=0):
        print("stack is empty")
    else:
        c=int(input(" enter the element want to pop"))
        stk.pop()
        top-=1
def display():
    print(stk)

while(n!=1):
    print("enter the operation you want to perform")
    opt=int(input("press 1)push 2)pop 3) display "))
    if(opt==1):
        push()
    elif(opt==2):
        pop()
    elif(opt==3):
        display()
    n=int(input(" do you want to continue press 1 for exit"))

