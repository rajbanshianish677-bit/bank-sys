class BankAccount:
    total_accounts_created = 0    
    _bank_name = "Kumari Digital Bank"
    __vault_security_code = "SECURE-99X"

    def __init__(self, account_holder, initial_deposit):
        self.account_holder = account_holder      
        self._account_type = "Standard Savings"    
        self.__balance = initial_deposit           
        BankAccount.total_accounts_created += 1

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited ${amount}. New balance: ${self.__balance}")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("Insufficient funds!")
        else:
            self.__balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.__balance}")

    def display_account_status(self):
        print(f"Holder: {self.account_holder}")
        print(f"Type: {self._account_type}")
        print(f"Current Balance: ${self.__balance}")
        
        if self.__balance >= 10000:
            print("Tier Status: Premium Member (Eligible for bonus interest)")
        else:
            print("Tier Status: Regular Member")

    @classmethod
    def get_bank_info(cls):
        return f"Welcome to {cls._bank_name}. System Code: {cls.__vault_security_code}"

    @staticmethod
    def calculate_interest(balance, rate_percentage):
        return balance * (rate_percentage / 100)


# --- RUNNING THE BANKING SYSTEM ---

print(BankAccount.get_bank_info())
print("---")

# Creating accounts (Triggers Constructor)
user1 = BankAccount("Anish", 12000)
user2 = BankAccount("Ram", 500)

# Alice's Transactions
print(f"--- {user1.account_holder}'s Session ---")
user1.display_account_status()
user1.deposit(1500)
user1.withdraw(4000)

print("---")

# Bob's Transactions
print(f"--- {user2.account_holder}'s Session ---")
user2.display_account_status()
user2.withdraw(600)  # Should trigger the insufficient funds if/else condition

print("---")

# Using the Static Method to project earnings
projected_interest = BankAccount.calculate_interest(10000, 4.5)
print(f"Static Calculation: 4.5% interest on $10,000 is ${projected_interest}")

print(f"Total Bank Accounts Active: {BankAccount.total_accounts_created}")