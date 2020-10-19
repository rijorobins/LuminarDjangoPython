import datetime
class Bank:
    bank_name="SBI"
    def createAccount(self,acno,pname):
        self.account_number=acno
        self.person_name=pname
       # self.bank_name=bname bank name is set as a static vbl.so this step can be avoided
        self.balance=balance=3000 #fixed balance
    def deposit(self,amount):
        self.balance+=amount
        print("Your",Bank.bank_name,"account has been credited with",amount,"on",datetime.date.today())
        print("Available Balance=",self.balance)
    def withdraw(self,amount):
        if (amount>self.balance):
            print("Insufficient balance in your account")
        else:
            self.balance-=amount
            print(amount,"has been debited from your",Bank.bank_name,"account on",datetime.date.today())
            print("Available Balance=", self.balance)
    def balanceEnquiry(self):
        print("Balance:",self.balance)
obj=Bank()

obj.createAccount(10000002,"Jack")
obj.deposit(5000)
obj.withdraw(2000)
obj.balanceEnquiry()