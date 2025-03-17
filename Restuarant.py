class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Creating an instance of Restaurant
restaurant = Restaurant("Tasty Bites", "Italian")

# Printing attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling methods
restaurant.describe_restaurant()
restaurant.open_restaurant()




# Ice Cream Stand: An ice cream stand is a specific kind of restaurant. Write
# a class called IceCreamStand that inherits from the Restaurant class you wrote in
# Exercise 9-1 (page 162) or Exercise 9-4 (page 166). Either version of the class
# will work; just pick the one you like better. Add an attribute called flavors that
# stores a list of ice cream flavors. Write a method that displays these flavors.
# Create an instance of IceCreamStand, and call this method.
