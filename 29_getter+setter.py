class test:
    def __init__(self,value):
        self.value = value
    
    def show(self):
        print(f"Value is {self.value} :")
    @property
    def newValue(self):
        return self.value
    @newValue.setter
    def newValue(self,newval):
        self.value = val

val1 = test(47)
# val1.newValue = 8 --> Gives error
print(val1.newValue)
val1.show()

#! You can use "@property" for getter and "@methodName.setter" for setter