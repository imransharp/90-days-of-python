import random
import os

# Define the file name
filename = "quotes.txt"

try:
    # Check if file exists
    if not os.path.exists(filename):
        raise FileNotFoundError("⚠️ 'quotes.txt' is missing! Please create the file and add quotes.")

    # Read the file
    with open(filename, "r") as file:
        quotes = file.readlines()

    # Pick a random quote
    if quotes:
        quote = random.choice(quotes).strip()
        print("\n🌟 Today's Motivation 🌟")
        print(quote)
    else:
        print("⚠️ The file is empty! Please add some quotes.")

except FileNotFoundError as e:
    print(e)

except Exception as e:
    print(f"❌ An unexpected error occurred: {e}")
