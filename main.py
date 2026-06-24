import os

FILE_NAME = "expenses.txt"


def add_expense():
    date = input("Enter Date (DD-MM-YYYY): ")
    category = input("Enter Category: ")
    amount = input("Enter Amount: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{date},{category},{amount}\n")

    print("Expense Added Successfully!")


def view_expenses():
    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    if not data:
        print("No expenses found!")
        return

    print("\nExpenses:")
    for i, line in enumerate(data, start=1):
        date, category, amount = line.strip().split(",")
        print(f"{i}. {date} | {category} | ₹{amount}")


def update_expense():
    view_expenses()

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    index = int(input("Enter expense number to update: ")) - 1

    if 0 <= index < len(data):
        date = input("New Date: ")
        category = input("New Category: ")
        amount = input("New Amount: ")

        data[index] = f"{date},{category},{amount}\n"

        with open(FILE_NAME, "w") as file:
            file.writelines(data)

        print("Expense Updated!")
    else:
        print("Invalid Expense Number")


def delete_expense():
    view_expenses()

    with open(FILE_NAME, "r") as file:
        data = file.readlines()

    index = int(input("Enter expense number to delete: ")) - 1

    if 0 <= index < len(data):
        data.pop(index)

        with open(FILE_NAME, "w") as file:
            file.writelines(data)

        print("Expense Deleted!")
    else:
        print("Invalid Expense Number")


def expense_report():
    if not os.path.exists(FILE_NAME):
        print("No expenses found!")
        return

    total = 0

    with open(FILE_NAME, "r") as file:
        for line in file:
            _, _, amount = line.strip().split(",")
            total += float(amount)

    print(f"\nTotal Expenses: ₹{total}")


while True:
    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Update Expense")
    print("4. Delete Expense")
    print("5. Expense Report")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        update_expense()

    elif choice == "4":
        delete_expense()

    elif choice == "5":
        expense_report()

    elif choice == "6":
        print("Thank You!")
        break

    else:
        print("Invalid Choice")