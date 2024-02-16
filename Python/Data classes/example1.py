from dataclasses import dataclass

@dataclass
class Point:
    x: float
    y: float


# Usage
p1 = Point(2.5, 3.0)
print(p1)  # Output: Point(x=2.5, y=3.0)
print(p1.x)  # Output: 2.5
print(p1.y)  # Output: 3.0

