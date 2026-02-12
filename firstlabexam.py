class BankAccount:
    def create_account(self, name, account_number):
        self.name = name
        self.account_number = account_number
        self.balance = 0.0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount.")
    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Invalid withdrawal or insufficient funds.")
    def withdraw_with_fee(self, amount, fee):
        total = amount + fee
        if 0 < total <= self.balance:
            self.balance -= total
            print(f"Withdrawn: {amount} (Fee: {fee})")
        else:
            print("Insufficient balance.")
    def show_balance(self):
        print(f"Balance: {self.balance}")
    def account_info(self):
        print("\n--- Account Information ---")
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        self.show_balance()



print("Bank Account Semouleaytorinator")
name = input("Enter account holder name: ")
acc_num = input("Enter account number: ")
account = BankAccount()
account.create_account(name, acc_num)
account.account_info()

while True:
    print("\nChoose an option:")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Withdraw with fee")
    print("4. Show balance")
    print("5. Account info")
    print("6. Exit")

    choice = input("Enter choice: ")
    if choice == "1":
        amt = float(input("Enter deposit amount: "))
        account.deposit(amt)
    elif choice == "2":
        amt = float(input("Enter withdrawal amount: "))
        account.withdraw(amt)
    elif choice == "3":
        amt = float(input("Enter withdrawal amount: "))
        fee = float(input("Enter fee: "))
        account.withdraw_with_fee(amt, fee)
    elif choice == "4":
        account.show_balance()
    elif choice == "5":
        account.account_info()
    elif choice == "6":
        print("Exiting BAS. you are never getting your money back olollololol")
        break
    else:
        print("Invalid choice. Try again.")