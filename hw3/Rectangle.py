#class Rectangle: 
#    def __init__(self, length, width):
#        self.length = length
#        self.width = width
#
#    def calc_area_rect(self):
#        return self.length*self.width
#
#Rectangle = Rectangle(5, 3)
#
#print("The area of the rectangle is", Rectangle.calc_area_rect())


class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_area_rect(self):
        return self.length * self.width


# test code
rect = Rectangle(5, 3)
print("The area of the rectangle is", rect.calc_area_rect())
