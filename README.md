# SOLID-Principle
**Single Responsibility Principle:**
The Single Responsibility Principle (SRP) is one of the five SOLID principles of object-oriented design. It states that:

A class should have only one reason to change.

Explanation:
This means that a class should only have one responsibility or one job. If a class has multiple responsibilities, it becomes tightly coupled, making it harder to modify and maintain.

Why is SRP Important?
Improves Maintainability – Since each class has a clear purpose, changes are easier to implement.

Enhances Readability – Code is more structured and easier to understand.

Reduces Coupling – Modifying one responsibility does not affect another.

Supports Reusability – A well-defined class can be reused in different contexts.



**Open Closed Principle:**
The Open/Closed Principle (OCP) is the second principle in SOLID and states that:

Software entities (classes, modules, functions) should be open for extension but closed for modification.

What does it mean?
Open for extension → You should be able to add new functionality without modifying existing code.

Closed for modification → Once a class is written and tested, you shouldn’t have to modify it for new features.

Why is OCP Important?
Avoids breaking existing code – Since modifications are not made to existing classes, there is less risk of introducing bugs.

Supports scalability – New features can be added without changing existing implementations.

Encourages maintainability – Easier to update and manage large systems.