# !            List Comprehension

names = ["Huzaifa", "Sharjeel", "Ali", "Davvy Jones"]

#? Basically we are iterating through list
# comp_list = [item for item in names]
comp_list = [item for item in names if len(item)>5]
#? In upper list we are printing names whose length is greater than 5.
print(comp_list)

