# QUEUE

# Like in stack, queue is a data structure that stores items in the FIRST IN FIRST OUT (FIFO) manner.

# eg: a queue of consumers who come first is served first

# OPERATIONS ASSOCIATED WITH QUEUE

# ENQUEUE: Add an item to the queue. If the que is full, then it is said to be an overflow condition
# DEQUE: Removes an item from the queue.The items are popped in the same order in which they are pushed.
#        if the queue is empty,then it is said to be  in an underflow condition.
# FRONT: Get the front from queue
# REAR: Get the last item from the queue

queue=[]
top=0
size=int(input("enter the size"))
n=0

def enqueue():
    global top,size
    if top>size:
        print("queue is in overflow condition")
    else:
        p=int(input("enter the element"))
        queue.append(p)
        top+=1

def dequeue():
    global top, size
    if top<=0:
        print("queue is in the overflow condition")
    else:
        queue.pop(0)
        top-=1

def front():
    print("first item in the queue",queue[0])

def gear():
    print("last item in the queue", queue[-1])
def display():
    print(queue)

while n!=1:
    print("select the operation")
    op=int(input("1)ENQUEUE, 2)DEQUEUE, 3)FRONT, 4)GEAR, 5)DISPLAY"))
    if op==1:
        enqueue()
    elif op==2:
        dequeue()
    elif op==3:
        front()
    elif op==4:
        gear()
    elif op==5:
        display()
    n=int(input("press 1 to exit or press 0 to continue"))



