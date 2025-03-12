# classes

class ExpenseTracker:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount

expense = ExpenseTracker("Lunch", 500)
print(expense.name, expense.amount)