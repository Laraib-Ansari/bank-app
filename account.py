class Account():
    def __init__(self, name, password, balance):
        self.name=name
        self.password=password
        self.balance
    
    def chech_balance(self):
        print(f"Your current balance is{self.balance:.2f}\n")
    
    def deposit(Self, amount):
        """
        No negative amount shall be deposited

        """
        self.balance+= amount
        print(f"INR {amount:.2f} deposited successfully\n")

    def withdraw(Self, amount):
        """
        check if sufficient amount is present

        """
        if self.balance==0:
            print("Balance is zero")

        elif self.balance>=amount:
            sefl.balance-=amount
            print(f"INR {amount:.2f} has been withdrawn\n")
        else:
            print("Insufficient Balance")
    
    def change_password(self, new_password):
        self.password=new_password
        print("Password Updated\n")

        