class BankSystem:
    def __init__(self):
        self.accounts = {}
        self.next_account_number = 1  

    def generate_account_number(self):
        """
        Sequential account number allocation from 1 up to 5000.
        
        """
        if self.next_account_number > 5000:
            raise Exception("Account number limit reached (5000)")
        acc_num = self.next_account_number
        self.next_account_number += 1
        return acc_num

    def create_account(self):
        name = input("Enter your name: ")
        password = input("Enter your password: ")
        try:
            balance = float(input("Enter initial deposit amount: "))
        except ValueError:
            print("Invalid deposit amount.")
            return

        acc_num = str(self.generate_account_number())
        self.accounts[acc_num] = Account(name, password, balance)

        print('\nAccount Created Successfully')
        print(f" Name: {name}")
        print(f" Balance: {balance}")
        print(f" Account Number : {acc_num}\n") 

    def login(self):
        try:
            acc_num = str(int(input("Enter your account number: ")))
        except ValueError:
            print("Invalid input. Account number must be digits only.")
            return
        
        if acc_num not in self.accounts:
            print("No Account found with that number")
            return
        
        password = input("Enter your password: ")
        account = self.accounts[acc_num]

        if account.password != password:
            print("Incorrect Password")
            return

        print(f"\n Welcome {account.name}!\n")
        self.after_login(account, acc_num)

    def after_login(self, account, acc_num):
        while True:
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Change Password")
            print("5. Logout")

            try:
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Please enter a number between 1 and 5.")
                continue

            if choice == 1:
                account.check_balance()
            elif choice == 2:
                try:
                    amount = float(input("Enter amount to deposit: "))
                    account.deposit(amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == 3:
                try:
                    amount = float(input("Enter amount to withdraw: "))
                    account.withdraw(amount)
                except ValueError:
                    print("Invalid amount.")
            elif choice == 4:
                new_password = input("Enter new password: ")
                account.change_password(new_password)
            elif choice == 5:
                print("Logged out.\n")
                break
            else:
                print("Invalid Choice. Please select a number between 1 to 5")

bank = BankSystem()
bank.create_account()

