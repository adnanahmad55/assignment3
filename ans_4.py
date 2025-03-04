
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_person_info(self):
        return f"Name: {self.name}, Age: {self.age}"


class Employee:
    def __init__(self, employee_id, salary):
        self.employee_id = employee_id
        self.salary = salary

    def display_employee_info(self):
        return f"Employee ID: {self.employee_id}, Salary: ₹{self.salary}"


class Manager(Person, Employee):
    def __init__(self, name, age, employee_id, salary, department):
     
        Person.__init__(self, name, age)
        Employee.__init__(self, employee_id, salary)
        self.department = department

    def display_manager_info(self):
        return (f"{self.display_person_info()}, {self.display_employee_info()}, "
                f"Department: {self.department}")


manager = Manager("Rahul Sharma", 35, "MGR101", 80000, "IT")

print(manager.display_manager_info())
