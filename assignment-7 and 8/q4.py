# Create a class "Employee" with attributes name and salary. Implement overloaded operators +
# and - to combine and compare employees based on their salaries.

class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def __add__(self,other):
        return (self.name + "&" +other.name, self.salary + other.salary )
    
    def __sub__(self,other):
        return self.salary - other.salary
    
emp1 = Employee("Kavya",120000)
emp2 = Employee("Someone",500)
print(emp1 + emp2)
print(emp1 - emp2)

        