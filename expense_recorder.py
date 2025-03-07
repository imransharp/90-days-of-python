import csv
import os
from datetime import datetime

# File to store expenses
FILE_NAME = "expenses.csv"

def load_expenses():
    """Load existing expenses from the CSV file."""
    expenses = []
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            reader = csv.reader(file)
            next(reader, None)  # Skip header
            for row in reader:
                expenses.append(row)
    return expenses

def save_expense(date, category, amount, description):
    """Save a new expense to the CSV file."""
    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])

def show_expenses(expenses):
    """Display all recorded expenses."""
    print("\nPrevious Expenses:")
    print("Date         | Category       | Amount  | Description")
    print("-" * 50)
    total = 0
    for expense in expenses:
        print(f"{expense[0]:<12} | {expense[1]:<14} | ${expense[2]:<7} | {expense[3]}")
        total += float(expense[2])
    print("-" * 50)
    print(f"Total Spent: ${total}")

def main():
    """Main function to record and show expenses."""
    # Load previous expenses
    expenses = load_expenses()
    
    # Show previous expenses
    if expenses:
        show_expenses(expenses)
    else:
        print("No previous expenses found. Start tracking now!\n")
    
    # Get new expense input
    while True:
        category = input("Enter expense category (e.g., Food, Bills, Transport, etc.): ")
        amount = input("Enter amount spent: ")
        description = input("Enter short description: ")
        date = datetime.now().strftime("%Y-%m-%d")
        
        save_expense(date, category, amount, description)
        print("Expense recorded successfully!\n")
        
        another = input("Do you want to add another expense? (yes/no): ").lower()
        if another != "yes":
            break
    
    # Show updated expenses
    show_expenses(load_expenses())
    
if __name__ == "__main__":
    # Create file with headers if not exists
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Amount", "Description"])
    
    main()
