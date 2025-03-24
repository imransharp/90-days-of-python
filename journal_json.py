import json
import os

# Define the JSON file
filename = "expenses.json"

# Load existing expenses if the file exists
if os.path.exists(filename):
    try:
        with open(filename, "r") as file:
            expenses = json.load(file)
    except json.JSONDecodeError:
        expenses = []  # If file is empty or corrupted, start fresh
else:
    expenses = []  # If file doesn't exist, start fresh

def save_expenses():
    """Save expenses to the JSON file."""
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)

def add_expense():
    """Get user input and add a new expense."""
    category = input("Enter expense category (e.g., Food, Rent, Transport): ")
    amount = input("Enter expense amount: ")
    date = input("Enter date (YYYY-MM-DD): ")

    # Create expense dictionary
    expense = {"category": category, "amount": amount, "date": date}
    
    # Add to the list and save
    expenses.append(expense)
    save_expenses()
    print("✅ Expense added successfully!\n")

def show_expenses():
    """Display all recorded expenses."""
    if not expenses:
        print("📌 No expenses recorded yet.\n")
        return
    
    print("\n📊 Previous Expenses:")
    for idx, expense in enumerate(expenses, 1):
        print(f"{idx}. {expense['date']} | {expense['category']} | ${expense['amount']}")

while True:
    print("\n🔹 Expense Tracker (JSON Version) 🔹")
    print("1. View Expenses")
    print("2. Add New Expense")
    print("3. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        show_expenses()
    elif choice == "2":
        add_expense()
    elif choice == "3":
        print("Exiting... Your data is saved. 📝")
        break
    else:
        print("❌ Invalid choice. Please select again.")
