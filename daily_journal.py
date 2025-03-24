import datetime

# Define the journal file
filename = "journal.txt"

# Function to read and display previous entries
def show_previous_entries():
    try:
        with open(filename, "r") as file:
            content = file.read()
            if content:
                print("\n📖 Your previous journal entries:")
                print(content)
            else:
                print("\n📖 No previous entries found.")
    except FileNotFoundError:
        print("\n📖 No journal file found. Creating a new one...")

# Function to add a new entry
def add_new_entry():
    entry = input("\n📝 Enter your new journal entry: ")
    date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open(filename, "a") as file:
        file.write(f"{date}: {entry}\n")

    print("✅ Entry saved!")

# Run the journal program
show_previous_entries()
add_new_entry()
