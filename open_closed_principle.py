'''''
The Open/Closed Principle (OCP) is the second principle in SOLID and states that:

Software entities (classes, modules, functions) should be open for extension but closed for modification.

What does it mean?
Open for extension → You should be able to add new functionality without modifying existing code.

Closed for modification → Once a class is written and tested, you shouldn’t have to modify it for new features.

Why is OCP Important?
Avoids breaking existing code – Since modifications are not made to existing classes, there is less risk of introducing bugs.

Supports scalability – New features can be added without changing existing implementations.

Encourages maintainability – Easier to update and manage large systems.
'''
 # Violation of OCP
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

class AreaCalculator:
    def calculate_area(self, shape):
        if isinstance(shape, Rectangle):
            return shape.width * shape.height
        elif isinstance(shape, Circle):
            return 3.14159 * shape.radius * shape.radius
        return 0


# Following OCP
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


class AreaCalculator:
    def calculate_area(self, shape):
        return shape.calculate_area()


# The solution with input value
from abc import ABC, abstractmethod
import math


# Abstract base class
class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass


# Rectangle class
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height


# Circle class
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def calculate_area(self):
        return math.pi * self.radius * self.radius


# AreaCalculator class
class AreaCalculator:
    def calculate_area(self, shape: Shape):
        # print(Shape)
        return shape.calculate_area()


# Main function with user input
def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Enter your choice (1 or 2): ")

    calculator = AreaCalculator()

    if choice == "1":
        width = float(input("Enter width of rectangle: "))
        height = float(input("Enter height of rectangle: "))
        rect = Rectangle(width, height)
        # print(rect)
        print(f"Area of Rectangle: {calculator.calculate_area(rect):.2f}")

    elif choice == "2":
        radius = float(input("Enter radius of circle: "))
        circ = Circle(radius)
        print(f"Area of Circle: {calculator.calculate_area(circ):.2f}")

    else:
        print("Invalid choice!")


if __name__ == "__main__":
    main()
