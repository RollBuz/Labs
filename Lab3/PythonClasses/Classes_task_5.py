class Account:
    def __init__(self, owner , balance):
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        if amount <= 0:
            print("The amount of deposit must be positive")
        else:
            self.balance += amount
            print(f"Your balance is {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print(f"You cant withdraw the summa, your balance is lower then summa you want to withdraw, youre balance {self.balance}")
        elif amount <= 0:
            print("Withdrawal summa must be positive!")
        else:
            self.balance -= amount
            print(f"Your transaction was complete, youre balance :{self.balance}")
        
client = Account("Rollan", 2500)
client.deposit(7500)
client.withdraw(9000)