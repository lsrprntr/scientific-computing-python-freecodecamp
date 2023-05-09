#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list()
        self.receipts = list()
         
    def __str__(self):
        lines = list()
        for i,item in enumerate(self.receipts):
            number = format(self.ledger[i],".2f") 
            space = 30-len(item[0:23])-len(f"{number}")
            line = f"{item[0:23]}{' '*space}{number}"
            lines.append(line)
        title = self.name.center(30,"*")+"\n"
        body = '\n'.join(lines)
        return f"{title}{body}"

    def deposit(self, amount, description=""):
        self.ledger.append(amount)
        self.receipts.append(description)
        

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append(-amount)
            self.receipts.append(description)
            return True
        else:
            return False

    def get_balance(self):
        return sum(self.ledger)

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append(-amount)
            self.receipts.append(f"Transfer to {other.name}")
            other.ledger.append(amount)
            other.receipts.append(f"Transfer from {other.name}")
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
    cats = list()
    for item in categories:
        names = item.name
        cost = item.get_balance()
        cats.append((names,cost))
    print(cats)
    return


eg = Category("examplename")
eg.deposit(100, "twentyletternameeee")
eg.deposit(100, "twentythreeletternamee")
eg.withdraw(100)
eg.transfer(10, eg)
eg.withdraw(99999, "big amount")

create_spend_chart([eg,eg])