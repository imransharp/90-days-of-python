# choice_car = input("tell me about what car you want to buy?")
# print(f"let me check if i can find {choice_car} for you")

# number_of_people = input("How many people for dinner?")
# if int(number_of_people) > 8:
#     print("Table is not available")
# else:
#     print("table is ready please come for dinner")


# List of sandwich orders
sandwich_orders = ["Tuna", "Chicken", "Egg", "Turkey", "Veggie"]

# Empty list to store finished sandwiches
finished_sandwiches = []

# Loop through each sandwich order
# while sandwich_orders:
#     current_sandwich = sandwich_orders.pop(0)  # Remove the first order from the list
#     print(f"I made your {current_sandwich} sandwich.")  
#     finished_sandwiches.append(current_sandwich)  # Move it to finished list

# # Print all finished sandwiches
# print("\nAll sandwiches have been made:")
# for sandwich in finished_sandwiches:
#     print(f"- {sandwich} sandwich")

# list of 5 names
names = ["imran", "salman", "qurabn", "farhan", "tim",]
for name in names:
    print(name)
response = ""
while response != "exit":
    response = input("enter name:")
    names.append(response)
    for name in names:
        print(name)



