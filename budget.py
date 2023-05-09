#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.items = list()
        return 

    def __repr__(self):
        #print(self.ledger)
        line = list()
        for i,item in enumerate(self.items):
            print(self.ledger[i])
            print(item[0:23])
            number = format(self.ledger[i],".2f")
            print(len(f"{number}"))
            len(item[0:23])
        title = self.name.center(30,"*")
        return f"{title}"

    def deposit(self, amount, description=""):
        self.ledger.append(amount)
        self.items.append(description)
        return

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(-amount)
            self.items.append(description)
            return True
        else:
            return False

    def get_balance(self):
        return sum(self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append(-amount)
            self.items.append(f"Transfer to {other}")
            other.ledger.append(amount)
            other.items.append(f"Transfer from {other}")
            return True
        else:
            return False

    def check_funds(self, amount):
        check = self.get_balance()
        if amount <= check:
            return True
        else:
            return False


def create_spend_chart(categories: list[str]):
    for item in categories:
        print(item.get_balance())
    return


eg = Category("examplename")
eg.deposit(100, "12345678901234567890")
eg.deposit(100, "1234567890123456789012345")
eg.withdraw(100)
eg.transfer(10, eg)
eg.withdraw(99999, "big amount")
print(eg, "print statement")
