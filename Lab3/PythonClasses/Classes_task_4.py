import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def show(self):
        print(f"({self.x}, {self.y})")
    
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    
    def dist(self, another):
        return math.sqrt((self.x - another.x) ** 2 + (self.y - another.y) ** 2)
    
p1 = Point(0,0)
p2 = Point(3, 4)
p1.show()
p2.show()

print(p1.dist(p2))

p1.move(3, 6)
p1.show()