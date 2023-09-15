list1 = ["C++","Python","Java","JavaScript","C"]
# print(list1)
# print(list1[2])

#? Iterating through for loop
# for i in list1:
#     print(i)
    
#? List can also contain different types of data-types although it is not recommended
list2 = [ 1, 2, "Huzaifa", True]
# print(list2[3])
# print(list2[-2]) #? The best solution for this is to minus the negative index from actual length in upper case it is 4.
#! Note that index always starts from 0 but length starts from 1.

#? Check whether element is present in List or not
# if "Huzaifa" in list2:
#     print("Yes he is present")
# else:
#     print("No he is not present")

#? Printing form initialised to where want to end
# print(list2[1:4])
# print(list2[0:4:2]) #! In this 0 is starting length and 4 is ending length but 2 means that after printing first value it will jump to 2 length basically it will jump from 1 length and will print second one.

#? Printing all list items at once without for-loop
# print(list2[:])