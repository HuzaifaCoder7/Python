# f = open('23_Files2/marks.txt', 'r')
f = open('23_Files2/marks.txt', 'w')
# i = 0
# while True:
#   i = i + 1
#   line = f.readline()
#   if not line:
#     break
#   m1 = int(line.split(",")[0])
#   m2 = int(line.split(",")[1])
#   m3 = int(line.split(",")[2])
#   print(f"Marks of student {i} in Maths is: {m1}")
#   print(f"Marks of student {i} in English is: {m2}")
#   print(f"Marks of student {i} in SST is: {m3}")

#   print(line)

#!  Writing to File
lines = ["Line1\n","Line2\n","Line3\n"]
f.writelines(lines)
f.close()