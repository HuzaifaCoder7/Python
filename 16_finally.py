# finally keyword block is always executed whether error occur or not.
def fun1():
    try:
        list = [1,2,3,4,5]
        inp = int(input("Enter the number: "))
        print(list[inp])
    except:
        print("Index out of range")
    finally:
        print("I will always be executed")
        a=5
        b=5
        print(a+b)

fun1()

