class test:
    def __init__(self):
        self.__name = "Huzaifa"
        self._age = 19

obj = test()
# print(obj.__name) #! Cannot be accessed directly
# print(obj._test__name) #! But can be accessed indirectly
print(obj._age) #! Used for protected modifier