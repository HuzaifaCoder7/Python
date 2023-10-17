class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
    def show(self):
        print(f"The employee {self.name} has {self.id} id")

class Programer(Employee):
    def default(self):
        print("The default language in company is Python and framework is Django")

e1 = Employee("Ali",7)
e1.show()
# e2 = Employee("Ali",10)
# e2.show()
e3 = Programer("Huzaifa-Amjad",47)
e3.show()
e3.default()