class person:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    
    def info(self):
        print(f"{self.name} is a {self.role}")

a = person("Huzaifa","Developer")
b = person("Ali","Designer")
a.info()
b.info()