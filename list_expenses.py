# Write a function that takes a list of expenses and returns the total.

# list = ["food","grocery", "travel"]
dict_list = {"food":10,"grocery":20, "travel":30}

def total_expense(list_of_expenses):
    total = sum([list_of_expenses[key] for key in list_of_expenses])
    return total


print(total_expense(dict_list))

# this function takes a dict of expenses sum the total and return
