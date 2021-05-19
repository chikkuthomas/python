# LINKED LIST #

# most commonly used data structure in a programming languages
# they store elements in memory
#while lists use a contiguous memory block to store references to thier data, linked lists store references as part of
# their own elements

# each element of a linked list is called a node, and every node has two different fields.
#1. "data" contains the value to be stored in the node
#2. "next" contains a reference to the next node on the list.

#linked lists can be used to implement "queues" or "stacks" as well as "graphs"

# first node is called "head"
# the last node must have its next reference pointing to "none"

#you can insert elements into a list using .insert() and .remove() for removing elelements at a specefic position
#we use.append() and.pop() only to insert or remove elements at the end of a list, here the time complexity is always constant.
# inserting and removing elements not at the end of the list requires some element shifting in the background
# and it takes considerate amount of time

# linked list on the other hand, are much more straightforward when it comes to insertion and deletion of elements at
# the beginning or end of a list and here the time complexity is always constant.

#linked lists have performance advantage over normal lists when implimenting a queue(FIFO)where elements are
# added and removed at the beginning of the list,but they perform similar to a list when implementing stack(lifo),
# in which elements are inserted and removed at the end of the list.

#for element lookup- linked list more time, list conctant time
# specific element lookup-list and linked list perform similarly

## COLLECTIONS.DEQUE ##
#deque pronounced as deck
# double ended queue
# collections.deque uses an implementation of a linked list in which you can access, insert ,or remove elements from the
# beginning or end of a list.

## HOW TO USE "collections.deque" ##
# to create a linked list-code:
from collections import deque

# # to create an empty linked list
# deque()
# deque([])
#
# # to create a non empty linked list
# llist=deque("1234")
#
#
# llist.append(5) # to add elements at the right of the list
# print(llist)
# llist.appendleft('g') # to add elements at the left of the list
# print(llist)
#
# llist.pop() # to remove elements at the right of list
# print(llist)
# llist.popleft() # to remove elements at the left of the list
# print(llist)

#.......................................................................................................................

# QUEUE USING LINKED LIST #

#FIFO

from collections import deque
queue=deque([])
top=0
size=int(input("enter the size of the queue"))
n=1
def push():
    global top,size
    if top>size:
        print("queue is overflowed")
    else:
        i=int(input("enter the element you want to add"))
        queue.append(i)
        top+=1
def pop():
    global top,size
    if top<=0:
        print("the queue is in underflow")
    else:
        queue.popleft()
        top-=1
def display():
    print(queue)
def front():
    print("from element is ",queue[0])
def rear():
    print("last element is ",queue[-1])
while n!=0:
    print("choose the operation")
    print("1.PUSH, 2.POP, 3.FRONT, 4.REAR, 5.DISPLAY")
    c=int(input("enter the operation"))
    if c==1:
        push()
    elif c==2:
        pop()
    elif c==3:
        front()
    elif c==4:
        rear()
    elif c==5:
        display()
    n=int(input("press 0 to exit or 1 to continue"))



