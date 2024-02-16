class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        if isinstance(other, Point):
            return self.x == other.x and self.y == other.y
        return False


# Creating two instances of the Point class
point1 = Point(3, 5)
point2 = Point(3, 5)
point3 = Point(1, 2)

# Using the equality operator (==) calls __eq__
print(point1 == point2)  # Output: True (point1 and point2 have the same x and y values)
print(point1 == point3)  # Output: False (point1 and point3 have different x or y values)
