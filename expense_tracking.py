import pandas as pd
import csv
from datetime import datetime

# File name for storing expenses
FILE_NAME = "expenses.csv"

# Ensure the file exists with headers
try:
    with open(FILE_NAME, "x", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Date", "Category", "Amount", "Description"])
except FileExistsError:
    pass  # File already exists

def add_expense():
    """Function to add a new expense"""
    date = input("Enter date (YYYY-MM-DD): ")
    category = input("Enter category (Food, Transport, Bills, etc.): ")
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount, description])
    
    print("✅ Expense recorded successfully!")

def view_monthly_expenses():
    """Function to calculate and display monthly total expenses"""
    try:
        df = pd.read_csv(FILE_NAME)
        df["Date"] = pd.to_datetime(df["Date"])
        df["Month"] = df["Date"].dt.strftime("%Y-%m")  # Extract year-month
        
        monthly_total = df.groupby("Month")["Amount"].sum()
        print("\n📊 Monthly Total Expenses:")
        print(monthly_total)
    except Exception as e:
        print("❌ Error reading expenses file:", e)

# Main program loop
while True:
    print("\nExpense Tracker Menu:")
    print("1. Add Expense")
    print("2. View Monthly Expenses")
    print("3. Exit")
    
    choice = input("Choose an option: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        view_monthly_expenses()
    elif choice == "3":
        print("🚀 Exiting program. Stay on top of your expenses!")
        break
    else:
        print("❌ Invalid choice. Try again.")

