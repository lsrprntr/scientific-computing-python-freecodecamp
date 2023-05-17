#import copy
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

    def draw(self,to_draw = 1): #reoccuring draw loop
        if self.total == 0: #returns to original bag contents and draws one
            self.reset()
            self.draw()
            return self.drawn
        else:
            r = random.randint(0,self.total-1)
            ball = self.contents[r]
            self.contents.pop(r)
            self.total-=1
            self.drawn.append(ball)
            if to_draw > 1:
                self.draw()
            return self.drawn
        
    def reset(self):
        self.contents = list(self.original)
        self.total = self.oritotal


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    n = int(num_experiments) #copy

    success = 0
    successes = 0

    while num_experiments > 0:
        num_experiments -= 1
        hat.drawn = []
        for i in range(0,num_balls_drawn):
            hat.draw()
        d = Counter(hat.drawn)
        for key in expected_balls:
            if d[key] >= expected_balls[key]:
                success = 1
            else:
                success = 0
                break
        if success == 1:
            successes += 1
        hat.reset()

    prob = successes/n
    return prob

'''
TESTS
hat3 = Hat(blue=3,red=2,green=6)
probability = experiment(hat=hat3, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
print(probability) #0.272 expected

hat = Hat(yellow=5,red=1,green=3,blue=9,test=1)
probability=experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
print(probability) #1.0 expected
'''