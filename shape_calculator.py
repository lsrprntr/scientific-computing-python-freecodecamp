class Rectangle():
    def __init__(self, width=0, height=0):
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

    def get_picture(): 
        return "*" 
                                                                                                                                                                                                                                   
    def get_amount_inside(self,object): 
        return False
    
    def __str__(self):
        return f"Width={self.width},Height={self.height}"



class Square(Rectangle):
    def __init__(self):
        pass
        
    def set_side(self,side):
        self.width = side
        self.height = side
        
#test cases
