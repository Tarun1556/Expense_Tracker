import json
from collections import defaultdict

# Function to add an expense
def add_expense(expenses):
    """
    Allows the user to input details of an expense and adds it to the list.
    """
    try:
        amount = float(input("Enter amount spent: "))
        description = input("Enter a brief description: ")
        category = input("Enter category (e.g., food, transport, entertainment): ").lower()
        expenses.append({'amount': amount, 'description': description, 'category': category})
        print("Expense added successfully!")
    except ValueError:
        print("Invalid input. Please enter a numeric value for the amount.")

# Function to save expenses to a JSON file
def save_data(expenses, filename="expenses.json"):
    """
    Saves the expenses list to a JSON file.
    """
    with open(filename, "w") as file:
        json.dump(expenses, file, indent=4)
    print("Data saved successfully!")

# Function to load expenses from a JSON file
def load_data(filename="expenses.json"):
    """
    Loads expenses from a JSON file. Returns an empty list if the file doesn't exist.
    """
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []  # Return an empty list if file doesn't exist

# Function to list all categories in expenses
def list_categories(expenses):
    """
    Lists all unique categories from the expenses list.
    """
    categories = set(exp['category'] for exp in expenses)
    if categories:
        print("Available categories:", ", ".join(categories))
    else:
        print("No categories found. Add some expenses first.")

# Function to analyze expenses and provide a summary
def analyze_expenses(expenses):
    """
    Provides a summary of total and category-wise expenses.
    """
    if not expenses:
        print("No expenses recorded yet.")
        return

    total_expenses = sum(exp['amount'] for exp in expenses)
    category_wise = defaultdict(float)

    for exp in expenses:
        category_wise[exp['category']] += exp['amount']

    print("\n--- Expense Summary ---")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print("Category-wise Breakdown:")
    for category, amount in category_wise.items():
        print(f"{category.title()}: ${amount:.2f}")

# Function to display the menu
def menu():
    """
    Displays the main menu of the program.
    """
    print("\nExpense Tracker")
    print("1. Add Expense")
    print("2. View Summary")
    print("3. List Categories")
    print("4. Save Data")
    print("5. Exit")

# Main function to run the program
def main():
    """
    Main program loop that handles user interactions.
    """
    expenses = load_data()
    print("Welcome to the Expense Tracker!")

    while True:
        menu()
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_expense(expenses)
        elif choice == "2":
            analyze_expenses(expenses)
        elif choice == "3":
            list_categories(expenses)
        elif choice == "4":
            save_data(expenses)
        elif choice == "5":
            save_data(expenses)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Entry point of the program
if __name__ == "__main__":
    main()
