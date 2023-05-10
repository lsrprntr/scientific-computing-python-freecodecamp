#https://www.freecodecamp.org/learn/scientific-computing-with-python/scientific-computing-with-python-projects/polygon-area-calculator

class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self,width):
        self.width = width
        
    def set_height(self,height):
        self.height = height

    def get_area(self): 
        return self.width * self.height
        
    def get_perimeter(self): 
        return (2 * self.width + 2 * self.height)

    def get_diagonal(self): 
        return  ((self.width ** 2 + self.height ** 2) ** 0.5)

    def get_picture(self): 
        if self.width>50 or self.height>50:
            return "Too big for picture."
        return '\n'.join(["*"*self.width for w in range(1,self.height+1)])+"\n"
                         
    def get_amount_inside(self, object):
        times = self.get_area() // object.get_area()
        print(times)
        if times < 1:
            return False
        return times
    
    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"

class Square(Rectangle):
    def __init__(self,side):
        self.height = side
        self.width = side
        
    def set_side(self,side):
        self.width = side
        self.height = side
    
    def __str__(self):
        return f"Square(side={self.width})"
                
#test cases
'''
rect = Rectangle(10, 15)
print(rect.get_area())
rect.get_picture()

sq = Square(2)
print(sq.get_picture())
sq.set_width(4) 
print(type(sq))
print(sq.get_picture())

rect.get_amount_inside(sq)

The replit test cases do not test when a square class is created then using a rectangle class method to change the width.
You could easily make more methods to keep the square a square but it isn't required in this exercise.
'''

