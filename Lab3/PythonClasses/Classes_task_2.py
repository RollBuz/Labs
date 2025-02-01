class Shape:
    def area(self):
        return 0
    def __str__(self):
        return f"Shape area {self.area()}"

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length ** 2
    
shape = Shape()
print(shape)

square_area = Square(3)
print(square_area)