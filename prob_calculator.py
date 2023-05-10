import copy
import random

class Hat:
    def __init__(self,**kwargs):
        self.contents,self.total = [],0
        for key,value in kwargs.items():
            self.total += value
            for i in range(1,value+1):
                self.contents.append(key)
        self.original = list(self.contents)
        self.oritotal = int(self.total)

    def draw(self):
        if self.total == 0: #returns to original bag contents
            self.contents = list(self.original)
            self.total = self.oritotal
            return print("Restart")
        else:
            r = random.randint(0,self.total-1)
            ball = self.contents[r]
            self.contents.pop(r)
            self.total-=1
            return ball
        



def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    d = hat.draw()
    
    return

hat1 = Hat(yellow=1,dfdas=1)
hat1.draw()
hat1.draw()

hat1.draw()
hat1.draw()

hat1.draw()
hat1.draw()

hat1.draw()
hat1.draw()

hat1.draw()
hat1.draw()