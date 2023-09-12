#                        For-Loop
#? 1
# name = 'Huzaifa'
# for c in name:
#     print(c)
#? 2
# subjects = ['Math','Physics','Chemistry','English']
# for subject in subjects:
#     print(subject)
#? 3
# for i in range(100):
#     print(i)  ==> Here range shows how much value to print in this case it can also be written in range(1,100)-->[Print from 1 to 100] first argument is from where to start and second argument where to stop. There is also third argument which tells how many number to skip
#? 4
for i in range(1,100,10):
    print(i)

#!                      While-Loop 
# i = 100
# while(i == i):
#     number = int(input("Enter"))
#     if number == 100:
#         break

#? Although there is no do-while loop in Python but you can emulate it

# while(True):
#     num = int(input("Enter"))
#     if(num < 100):
#         break