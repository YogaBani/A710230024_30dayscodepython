# Definisikan kelas "BankAccount"
class BankAccount:
  def __init__(self, account_number, account_holder, initial_balance):
    self.account_number = account_number
    self.account_holder = account_holder
    self.balance = initial_balance

  def deposit(self, amount):
    self.balance += amount
    print(f"Deposit {amount} to account {self.account_number}. New balance: {self.balance}")

  def withdraw(self, amount):
    if amount > self.balance:
      print("Insufficient balance")
    else:
      self.balance -= amount
      print(f"Withdraw {amount} from account {self.account_number}. New balance: {self.balance}")

  def get_balance(self):
    return self.balance

# Buat objek "account1" dari kelas "BankAccount"
account1 = BankAccount("1234567890", "John Doe", 1000)

# Deposit 500 ke account1
account1.deposit(500)

# Withdraw 200 dari account1
account1.withdraw(200)

# Tampilkan balance account1
print(f"Balance: {account1.get_balance()}")

# Buat objek "account2" dari kelas "BankAccount"
account2 = BankAccount("9876543210", "Jane Doe", 500)

# Deposit 1000 ke account2
account2.deposit(1000)

# Withdraw 800 dari account2
account2.withdraw(800)

# Tampilkan balance account2
print(f"Balance: {account2.get_balance()}")
