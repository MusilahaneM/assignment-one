import math


class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


def total_area(shapes):
    return sum(shape.area() for shape in shapes)


# Demonstration
if __name__ == "__main__":
    shapes = [
        Circle(5),  # Radius = 5
        Rectangle(4, 6),  # Width = 4, Height = 6
        Triangle(3, 7),  # Base = 3, Height = 7
        Circle(2)  # Radius = 2
    ]

    # Calculate and display total area
    total = total_area(shapes)
    print(f"Total area of all shapes: {total:.2f}")