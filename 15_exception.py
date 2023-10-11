inp = int(input("Enter Your number: "))
try:
    for i in range(1,11):
        print(f"{inp} X {i} = ", inp * i)
except:
    print("Invalid input")