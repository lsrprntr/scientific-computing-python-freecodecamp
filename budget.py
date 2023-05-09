#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.items = list()
        return

    def deposit(self, amount, description=""):
        self.amount = amount
        self.description = description
        self.ledger.append(amount)
        self.items.append(description)
        return

    def withdraw(self, amount, description=""):
        self.amount = amount
        self.description = description
        if self.check_funds(amount):
            self.ledger.append(-amount)
            self.items.append(description)
            return True
        else:
            return False

    def get_balance(self):
        print("THIS IS HOW MUCH BALANCE",sum(self.ledger))
        return sum(self.ledger)

    def transfer(self, amount, name):
        self.amount = 1
        name.amount = 2
        return

    def check_funds(self, amount):
        check = self.get_balance()
        if check != 0:
            print("No moneys")
            return False
        else:
            return True


def create_spend_chart(categories: list[str]):
    for item in categories:
        item.get_balance()
        print("balance ^^^")
    return


damn = Category("damn")
damn.deposit(10, "Pizza")
damn.get_balance()
