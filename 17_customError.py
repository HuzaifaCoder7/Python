a = int(input("Enter number b/w 5 to 50: "))
if(a<5 or a>50):
    raise ValueError("Sahi value dal")
    

#! We can specify our custom Errors using "raise" keyword. There are many other errors like MemoryError