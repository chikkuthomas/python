# EXCEPTION HANDLING CASES #
#bank user pin change
def bank(user,pin):
    mypin=pin
    return mypin
print(bank('chikku',7654))

#.......................................................................................................................

#pin change using exception
def bpin(user,pin):
    if user=='admin':
        mypin=pin
        return mypin
    else:
        raise Exception("you are not allowed to do this operation")

try:
    print(bpin("admin", 876))
except Exception as a:
    print(a.args)

#.......................................................................................................................

#using decorators
def bankval(func):
    def wrapper(user,pin):
        if user!='admin':
            raise Exception("you are not allowed to do the operation") # raise exception means this is he place where
                                                                        # exception has to start
        else:
            return func(user,pin)
    return wrapper
@bankval
def bnk(user,pin):
    mypin=pin
    return mypin
print(bnk("admin",23451))

#.......................................................................................................................



















