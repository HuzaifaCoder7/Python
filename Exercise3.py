#!                   Program that encodes the message and decode if password is correct


import random as ran
name = input("Enter message to encode: ")
i = len(name)
s = ""
while(i > 0):
    i = i - 1
    s = s + name[i]
symbol = "!@#$%^&*"
letters = "abcdefghijklmnopqrstuvwxyz"
print(ran.choice(symbol)+ran.choice(letters)+s+ran.choice(symbol))


password = int(input("Enter password to decode: "))
if password == 100:
    s.replace(symbol,"") 
    j = 0
    st = ""
    while(j < len(name)):
        st = st + name[j]
        j = j + 1
    print(st)
else:
    print("Invalid password")