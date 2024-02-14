class Account:
    def __init__(self, balance, account_no):
        self.balance = balance
        self.account_no = account_no
    def debit(self,amount):
        self.balance-=amount
        print("Rs",amount,"was debited")
        print("Your new balance is Rs", self.get_balance())
    def credit(self,amount):
        self.balance+=amount
        print("Rs",amount,"was Credited")
        print("Your new balance is Rs", self.get_balance())
    def get_balance(self):
        return self.balance

acc1=Account(10000,1234)  #creating an object 
acc1.debit(7000)          #calling the method of the object
acc1.credit(800)          #another call to the same method on the same object

