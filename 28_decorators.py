def greet(fn):
    def mfn(*args,**args1):
        print("Welcome to my function")
        fn(*args,**args1)
        print("Thanks for using my function")
    return mfn

@greet
def add(a,b):
    print(a + b)

add(2,3)