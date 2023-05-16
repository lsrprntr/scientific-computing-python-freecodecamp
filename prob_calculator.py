import copy
import random
from collections import Counter

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        self.total = 0
        self.drawn = []

        for key,value in kwargs.items():
            self.total += value
            for i in range(1,value+1):
                self.contents.append(key)

        self.original = list(self.contents) #copy
        self.oritotal = int(self.total) #copy

    def draw(self):
        if self.total == 0: #returns to original bag contents
            self.contents = list(self.original) #copy
            self.total = self.oritotal
            self.drawn = []
            return print("Restarted/Set to original")
        else:
            r = random.randint(0,self.total-1)
            ball = self.contents[r]
            self.contents.pop(r)
            self.total-=1
            self.drawn.append(ball)
            return self.drawn
        



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = num_balls_drawn
    n = int(num_experiments) #copy
    success = 0

    while num_experiments > 0:
        num_experiments -= 1
        problist = list()
        drawpile = list()
        for i in range(0,m):
            hat.draw()
        print(hat.drawn)
        d = Counter(hat.drawn)
        for key in expected_balls:
            if d[key] >= expected_balls[key]:
                print("Matches prob")
            else:
                print("No Match")
                break
            success += 1
                
            


    
    probability = success/n
    return probability

hat1 = Hat(yellow=1,dfdas=1)
