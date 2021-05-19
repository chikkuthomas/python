# to print the details of the book
def book(**details):
    for k,v in details.items():
        print(k,"=",v)
        print(type(details))
book(name="WHY WE TOOK THE CAR",Author="Wolfgang Herrndorf",pages=345,price="54$")

# WE GET THE OUTPUT AS #
# name = WHY WE TOOK THE CAR
# Author = Wolfgang Herrndorf
# pages = 345
# price = 54$