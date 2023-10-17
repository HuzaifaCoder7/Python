class MyClass:
    def __init__(self, value):
        self.modifiedValue = value

    @property
    def value(self):
        return self.modifiedValue

    @value.setter
    def value(self, new_value):
        self.modifiedValue = new_value

obj = MyClass(10)
obj.value = 47 #? With no setter you cannot set value 
print(obj.value)



#! You can use "@property" for getter and "@methodName.setter" for setter.
#! Function name of Getter and Setter should be same with value name.