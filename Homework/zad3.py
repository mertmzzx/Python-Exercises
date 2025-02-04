class BankAccount:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner
        self.balance = float(balance)

    def deposit(self, money):
        if money > 0:
            self.balance += money
            print("Депозитът беше успешен.")
        else:
            print("Невалидна сума за депозит.")

    def withdraw(self, money):
        if money > 0:
            if self.balance >= money:
                self.balance -= money
                print("Тегленето беше успешно.")
            else:
                print("Недостатъчно средства!")
        else:
            print("Невалидна сума за депозит.")

    def display_balance(self):
        print(f"Банкова сметка с номер {self.account_number} на {self.owner} разполага с {self.balance} лв. ")


account1 = BankAccount(10001, "Иван Иванов", 0)
account1.deposit(5000)
account1.deposit(-100)

account1.withdraw(4500)
account1.display_balance()

account2 = BankAccount(10002, "Петър Петров", 100)
account2.deposit(200)
account2.withdraw(400)
account2.withdraw(300)
account2.display_balance()
