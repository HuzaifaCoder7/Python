from functools import reduce


l = [23,43,22,15,98,75,56]

#! High-Order Function:
#? A function that takes another function as an argument is known as high order function. Map, Filter and Reduce are example of it.

#! MAP
# newl = list(map(lambda x: x * x, l))
# print(newl)                                  ------> Prints square of all elements in list

#! FILTER
# newl = list(filter(lambda x: x > 50, l))
# print(newl)                                  ------> Prints value greater than 50

#! REDUCE
# newl = reduce(lambda x,y:x+y, l)
# print(newl)                                  ------> Would print sum of all elements in list