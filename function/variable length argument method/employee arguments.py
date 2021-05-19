# def employee(*args):
#     print(args)
# employee(100,"Engineer","kakkanad","thrissur")

# in this case the output will be = (100,"Engineer","kakkanad","thrissur")
# here we cannot distiguish what each argument means
# we cannot distuingish what kakkanad and thrissur is meant by'
# it can either be place of work or place of stay
# so make it more clear we use keywords too while defining the function method

def employee(*args):
    for val in args: # iterating to get each arguments separately
        print(val)

employee(50,"kochi","kannur")
#here instead of tuple each argument id printed
#50
#kochi
# kannur

#.......................................................................................................................

# here we need to add keyword ,hence we use kwargs {keyword and arguments}
# we can use any word instead but we nee to use " **"

# PRINT EMPLOYEE DETAILS #
def details(**kwargs):
    print(kwargs) # here details are printed as dictionary {keyword:value} =
                    # duplicate keys not allowed, duplicate values allowed
details(id=54,name="chikku",place="kochi")

# output: {'id': 54, 'name': 'chikku', 'place': 'kochi'}

# to print the details separately:
def emp(**det):
    for k,v in det.items(): # here we need to iterate keyword and values, so we use k and v for iterating
                            # det.items() syntax used to get the elements from the dictionary
        print(k,"=>",v)
emp(name="Chikku Thomas",id=1452,job="Engineer",place="Cochin")