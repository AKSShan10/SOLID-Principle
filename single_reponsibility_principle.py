'''''
The Single Responsibility Principle (SRP) is one of the five SOLID principles of object-oriented design. It states that:

A class should have only one reason to change.

Explanation:
This means that a class should only have one responsibility or one job. If a class has multiple responsibilities, it becomes tightly coupled, making it harder to modify and maintain.

Why is SRP Important?
Improves Maintainability – Since each class has a clear purpose, changes are easier to implement.

Enhances Readability – Code is more structured and easier to understand.

Reduces Coupling – Modifying one responsibility does not affect another.

Supports Reusability – A well-defined class can be reused in different contexts.

'''


# Without SRP (Violating the Principle)

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def calculate_salary(self):
        # Logic for salary calculation
        pass

    def generate_report(self):
        # Logic for generating reports (violates SRP)
        pass

    def save_to_database(self):
        # Logic for saving to a database (violates SRP)
        pass

'''''
👉 Here, the Employee class is responsible for:

Salary calculation

Report generation

Database operations

If we need to change the way we save data, we must modify this class, which could also affect other functionalities.
'''

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        # Logic for salary calculation
        pass

class ReportGenerator:
    def generate_report(self, employee):
        # Logic for generating reports
        pass

class EmployeeRepository:
    def save_to_database(self, employee):
        # Logic for saving employee data
        pass


# Shape example

import math

# Shape classes (Only data, no logic)
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Circle:
    def __init__(self, radius):
        self.radius = radius

# AreaCalculator class (Only logic, no data)
class AreaCalculator:
    def calculate_rectangle_area(self, rectangle: Rectangle):
        return rectangle.width * rectangle.height

    def calculate_circle_area(self, circle: Circle):
        return math.pi * circle.radius ** 2

# Main logic to take user input and calculate area
def main():
    print("Choose a shape to calculate area:")
    print("1. Rectangle")
    print("2. Circle")
    choice = input("Enter choice (1 or 2): ")

    calculator = AreaCalculator()

    if choice == "1":
        width = float(input("Enter width of rectangle: "))
        height = float(input("Enter height of rectangle: "))
        rect = Rectangle(width, height)
        area = calculator.calculate_rectangle_area(rect)
        print(f"Area of Rectangle: {area:.2f}")

    elif choice == "2":
        radius = float(input("Enter radius of circle: "))
        circ = Circle(radius)
        area = calculator.calculate_circle_area(circ)
        print(f"Area of Circle: {area:.2f}")

    else:
        print("Invalid choice!")

if __name__ == "__main__":
    main()



# Employee with input
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

class SalaryCalculator:
    def calculate_salary(self, employee):
        bonus = employee.salary * 0.10
        return employee.salary + bonus

class ReportGenerator:
    def generate_report(self, employee):
        return f"Employee Report:\nName: {employee.name}\nSalary: {employee.salary:.2f}"

class EmployeeRepository:
    def save_to_database(self, employee):
        print(f"Saving {employee.name}'s data to the database...")

def main():
    # Input data
    name = input("Enter employee name: ")
    salary = float(input("Enter employee base salary: "))

    # Create employee object
    emp = Employee(name, salary)

    # Calculate salary
    salary_calc = SalaryCalculator()
    updated_salary = salary_calc.calculate_salary(emp)
    emp.salary = updated_salary

    # Generate report
    report_gen = ReportGenerator()
    report = report_gen.generate_report(emp)
    print(report)

    # Save employee
    repo = EmployeeRepository()
    repo.save_to_database(emp)

if __name__ == "__main__":
    main()
