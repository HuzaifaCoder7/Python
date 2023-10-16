class person:
    name = "Huzaifa"
    role = "Developer"
    def info(self):
        print(f"{self.name} is a {self.role}")

a = person()
b = person()
# print(a.name)
# a.info()
b.name = "Ali"
b.role = "Designer"
b.info()
a.info() #? Would print with default argument
#! You can create many objects from one class