import time as t

# seconds = t.time()
# print(seconds)     ===> This will print seconds passed since 1970

# currentTime = t.ctime(seconds)
# print(currentTime)  ===> For Readable Format

time = t.localtime() #? This returns time struct
# timeString = t.strftime("%H",time) #? And this prints String in given format.
#?                    Specified-Format
#?                        |
convertedTime = int(t.strftime("%H",time))
if convertedTime >= 14:
    print("Good Evening")
elif convertedTime < 11:
    print("Good Morning")
else:
    print("Good Afternoon")

#! NOTE:
# time.strftime() function converts a tuple or struct_time representing a time as returned by gmtime() or localtime() to a string as specified by the format argument.