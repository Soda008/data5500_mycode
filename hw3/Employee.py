class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increase_salary(self):
        return self.salary*1.1

John = Employee("John", 5000)

print("The updated salary is:", John.increase_salary())