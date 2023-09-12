def average(*num):
    sum = 0
    for i in num:
        sum = sum + i
        print("Average is: ",sum/len(num))
        


choice = int(input("Enter numbers to give average: "))
for j in range(choice):
      c =  int(input("Enter:"))
      

average(c)
