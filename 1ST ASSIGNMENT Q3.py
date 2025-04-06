class Shape:
    def __init__(self, name):
        self.name = name
        print(f"Initializing Shape: {self.name}")

    def calculate_area(self):
        print("Shape area calculation (base class does nothing)")
        return 0


class Rectangle(Shape):
    def __init__(self, name, width, height):
        # Call the parent class's __init__ using super()
        super().__init__(name)
        self.width = width
        self.height = height
        print(f"Initializing Rectangle with width={width}, height={height}")

    def calculate_area(self):
        # You could call the parent's calculate_area() first if needed
        # super().calculate_area()  # This would call Shape's version

        # Rectangle-specific area calculation
        area = self.width * self.height
        print(f"Calculating Rectangle area: {area}")
        return area


# Demonstration
if __name__ == "__main__":
    rect = Rectangle("My Rectangle", 5, 3)
    print("\nRectangle properties:")
    print(f"Name: {rect.name}")
    print(f"Width: {rect.width}")
    print(f"Height: {rect.height}")

    area = rect.calculate_area()
    print(f"\nFinal area: {area}")