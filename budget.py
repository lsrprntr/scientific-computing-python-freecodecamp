#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/budget-app


class Category:

    def __init__(self, name):
        self.name = name
        self.ledger = list() #{"amount": amount, "description": description}
        
    def __str__(self):
        lines = list()
        for object in self.ledger:
            number = format(object["amount"],".2f")
            space = 30 - len((object["description"][0:23])) - len(f"{number}")
            line = f"{object['description'][0:23]}{' '*space}{number}"
            lines.append(line)
        title = self.name.center(30,"*")+"\n"
        body = '\n'.join(lines)
        total = format(self.get_balance(),".2f")
        return f"{title}{body}\nTotal: {total}"

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})
        

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        return sum((object["amount"] for object in self.ledger))

    def transfer(self, amount, other):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": f"Transfer to {other.name}"})
            other.ledger.append({"amount": amount, "description": f"Transfer from {self.name}"})
            return True
        else:
            return False

    def check_funds(self, amount):
        check = self.get_balance()
        if amount <= check:
            return True
        else:
            return False


def create_spend_chart(categories):
    ptotal = 0
    cats = list()
    padding = 0
    for item in categories:
        names = item.name
        costs = item.get_balance()
        cats.append((names,costs))
        ptotal += costs
        padding = max(len(names),padding)

    for i,(name,cost) in enumerate(cats):
        cats[i] = (name.ljust(padding),cost/ptotal*100//1)        
    title = "Percentage spent by category"
    graph = ["100| ",
            " 90| ",
            " 80| ",
            " 70| ",
            " 60| ",
            " 50| ",
            " 40| ",
            " 30| ",
            " 20| ",
            " 10| ",      
            "  0| "]
    xline = "    -"+"---"*len(categories)
    body = "     "
    for (name,cost) in cats:
        for index, plot in enumerate(graph):
            if cost >= int(plot[:3]):
                graph[index]+= "o  "
            else:
                graph[index]+= "   "
    for index in range(padding):
        for (name,cost) in cats:
            body += name[index]+"  "
        body += "\n     "
    body = body[:-6]

    
    #print(title+"\n"+'\n'.join(graph)+"\n"+xline+"\n"+body)
    return title+"\n"+'\n'.join(graph)+"\n"+xline+"\n"+body

"""
#Test case
food = Category("Food")
business = Category("Business")
entertainment = Category("Entertainment")
food.deposit(900,"deposit")
business.deposit(900,"deposit")
entertainment.deposit(900,"deposit")
food.withdraw(105.55)
entertainment.withdraw(33.40)
business.withdraw(10.99)

create_spend_chart([business, food, entertainment])
print(business)
print(food)
print(entertainment)
"""