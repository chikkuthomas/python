# bank (account creation, cash deposit, withdraw,balance check)
class Bank:
    Bname = "STATE BANK OF INDIA"
    def account(self,name,age,place):

        self.name=name
        self.age=age
        self.place=place
        self.min=1000
        print("Bank Name =", Bank.Bname)
        print("name =",self.name,)
        print("age =", self.age)
        print("place =", self.place)
        self.balance=self.min



    def deposit(self,amount):
        self.amount=amount
        self.balance+=self.amount
        print("your bank account is credited with amount ",self.balance)

    def withdraw(self,wamount):
        self.wamount=wamount
        if self.wamount>self.balance:
            print("insufficient balance to withdraw")
        else:
            print(" Account debited with Rs ",self.wamount)
            self.balance -= self.wamount
            print("Available balance =",self.balance)


a=Bank()
a.account("suresh",27,"Thrissur")
a.deposit(2500)
a.withdraw(0)

