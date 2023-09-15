import random






question1 = {
    "q1" : "Who invented Bulb?",
    "choice": ["A: Thomas", "B: Newton", "C: Einstein"],
    "answer":"A"
}
question2 = {
    "q2" : "Who is the owner of Microsoft?",
    "choice": ["A: Elon", "B: Apple", "C: Bill"],
    "answer":"C"
}
question3 = {
    "q3" : "Which language is used for Machine-Learning?",
    "choice": ["A: C++", "B: Python", "C: Java"],
    "answer":"B"
}
question4 = {
    "q4" : "Is Python Object Oriented or not?",
    "choice": ["A: Yes", "B: No"],
    "answer":"A"
}
question5 = {
    "q5" : "Is DSA important?",
    "choice": ["A: Yes", "B: No"],
    "answer":"A"
}

print(question1["q1"])
for choice in question1["choice"]:
    print(choice)
score = 0
#
inp = input("Enter Your answer in A, B or C  ")
if(inp == question1["answer"]):
    print("Correct")
    score = score + 10
    print(question2["q2"])

for choice in question2["choice"]:
    print(choice)

#
inp = input("Enter Your answer in A, B or C:   ")
if (inp == question2["answer"]):
    print("Correct")
    score = score + 10
    print(question3["q3"])

for choice in question3["choice"]:
    print(choice)

#
inp = input("Enter Your answer in A, B or C:   ")
if (inp == question3["answer"]):
    print("Correct")
    score = score + 10
    print(question4["q4"])

for choice in question4["choice"]:
    print(choice)

#
inp = input("Enter Your answer in A, B or C:   ")
if (inp == question4["answer"]):
    print("Correct")
    score = score + 10
    print(question5["q5"])

for choice in question5["choice"]:
    print(choice)

#
inp = input("Enter Your answer in A, B or C:   ")
if (inp == question5["answer"]):
    print("Correct")
    score = score + 10

print("Total Score is: ",score)

    