class account:
    def __init__(self , title = None , balance = 0):
        self.title = title
        self.balance = balance

    def display(self):
        print("(" , self.title , "," , self.balance , ")")

class savingsaccount(account):
    def __init__(self , title = None , balance = 0 , interestrate = 0):
        super().__init__(title , balance)
        self.interestrate = interestrate

    def display(self):
        print("(" , self.title , "," , self.balance , "," , self.interestrate , ")")


account_obj = account("Ashish" , 5000)
account_obj.display()
savingsaccount_obj = savingsaccount("Ashish" , 5000 , 5)
savingsaccount_obj.display()