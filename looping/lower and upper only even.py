#read low and up numbers and only print even numbers
low=int(input("enter lower input"))
up=int(input("enter upper input"))

while(low<=up):
    if(low%2==0):
      print(low)
    low+=1   #increment outside for loop only inside while loop