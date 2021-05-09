#operators in programming languages can be overloaded to perform other functions instead of their usual process.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
    def __str__(self):
        return "({0}, {1})".format(self.x, self.y)

point1 = Point(1, 4)
point2 = Point(2, 8)
print(point1 + point2)
    