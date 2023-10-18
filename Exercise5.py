import os
#!  Program of Library which adds books and displays it
class Library:
    books = ["Atomic Habits"]
    def addBook(self,num):
        for j in range(num):
            inpbook = input("Enter the book name: ")
            self.books.append(inpbook)
            print("Your book has been added")
    def showbook(self):
        i = 0
        for book in self.books:
            print(f"{i}: {book}")
            i = i + 1

obj = Library()

for k in range(3):
    print("Welcome to Huzaifa Library.Enter following function from following: ")
    print("1: Add a book")
    print("2: Show available book")
    print("3: Exit")
    index = int(input("Enter: "))
    if (index == 1):
        bn = int(input("How many books do you want to add: "))
        obj.addBook(bn)
        os.system('cls')
    elif(index == 2):
        obj.showbook()
    elif(index == 3):
        exit()
    else:
        print("Invalid Input")
    