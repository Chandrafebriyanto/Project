print("Welcome to the Daily Expense Tracker!")
print("""
Menu:
1. Add a new expense
2. View all expenses
3. Calculate total and average expense
4. Clear all expenses
5. Exit""")

expenses = []

while True:
    choice = float(input())
    if choice == 1:
        print("Expense added successfully!")
        expense = float(input())
        expenses.append(expense)
    elif choice == 2:
        if expenses:
            print("Your expenses:")
            for i, expense in enumerate(expenses, start=1):
                print(f"{i}. {expense}")
        else:
            print("No expenses recorded yet.")
    elif choice == 3:
        if expenses:
            total = sum(expenses)
            average = total / len(expenses)
            print(f"Total expense: {total}")
            print(f"Average expense: {average}")
        else:
            print("No expenses recorded yet.")
    elif choice == 4:
        expenses.clear()
        print("All expenses cleared.")
    elif choice == 5:
        print("Exiting the Daily Expense Tracker. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")