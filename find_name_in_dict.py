# Create a dictionary with names and ages
people = {
    "Ali": 30,
    "Sara": 25,
    "John": 40
}

# Ask the user for a name
name = input("Enter a name: ")

# Check if the name exists in the dictionary
if name in people:
    print(f"{name} is {people[name]} years old.")
else:
    print("Name not found.")
