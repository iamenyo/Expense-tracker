from datetime import date
import json

print("EXPENSE TRACKER")

expense_list = []


def menu():
    print("Add_expense [1]")
    print("Show_menu [2]")
    print("View_expenses [3]")
    print("Edit_expenses [4]")
    print("Remove_expense [5]")
    print("Statistics [6]")
    print("Quit [7]")


def add_expense():
    print("Enter the expense")

    expense_dict = {
        "amount": "",
        "category": "",
        "description": "",
        "date": date.today(),
    }

    try:
        expense_dict["amount"] = int(input("Enter an amount: "))
    except ValueError:
        print("Amount must be a number.")
        return

    expense_dict["category"] = input("Category: ")
    expense_dict["description"] = input("Description: ")

    expense_list.append(expense_dict)


def view_expenses():
    if not expense_list:
        print("There is no expense available")
        return

    for index, expense in enumerate(expense_list, start=1):
        print(
            f"{index}.{expense['description']} - {expense['date']}\n"
            f"Amount: {expense['amount']}\n"
            f"Category: {expense['category']}\n"
        )


def statistics():
    if not expense_list:
        print("No expenses available.")
        return

    total = sum(expense["amount"] for expense in expense_list)
    count = len(expense_list)
    average = total / count
    lowest = min(expense["amount"] for expense in expense_list)
    highest = max(expense["amount"] for expense in expense_list)

    print(f"Total expenses: {total}")
    print(f"Number of expenses: {count}")
    print(f"Average expense: {average:.2f}")
    print(f"Lowest expense: {lowest}")
    print(f"Highest expense: {highest}")


def remove_expense():
    if not expense_list:
        print("There is no expense available")
        return

    try:
        index = int(input("Expense to remove: "))
    except ValueError:
        print("Your input must be a number.")
        return

    if index == 0:
        print("Expense number must start at 1.")
    elif 1 <= index <= len(expense_list):
        removed = expense_list.pop(index - 1)
        print(f"{removed['description']} has been removed")
    else:
        print(
            f"Invalid expense number. Must be between 1 and"
            f"{len(expense_list)}."
        )


def edit():
    if not expense_list:
        print("There is no expense available")
        return

    view_expenses()

    try:
        index = int(input("Expense number to edit: "))
    except ValueError:
        print("Your input must be a number.")
        return

    if index == 0:
        print("Expense number must start at 1.")

    elif 1 <= index <= len(expense_list):
        expense = expense_list[index - 1]

        print(
            f"[{index}. {expense['description']}\n"
            f"Amount: {expense['amount']}\n"
            f"Category: {expense['category']}\n]"
        )

        description = input(
            "Description (leave empty to keep current): "
        )

        amount = input(
            "Amount (leave empty to keep current): "
        )

        category = input(
            "Category (leave empty to keep current): "
        )

        if description:
            expense["description"] = description

        if amount:
            try:
                expense["amount"] = int(amount)
            except ValueError:
                print("Amount must be a number.")
                return

        if category:
            expense["category"] = category

        print("Expense updated successfully.")

    else:
        print(
            f"Invalid expense number. Must be between 1 and"
            f"{len(expense_list)}."
             )


def load():
    try:
        with open("expense.json", "r", encoding="utf-8") as file:
            data = json.load(file)

            expense_list.extend(data)

            for expense in expense_list:
                expense["date"] = date.fromisoformat(expense["date"])

    except FileNotFoundError:
        print("No expenses saved")


def save():
    data_to_save = []

    for expense in expense_list:
        expense_copy = expense.copy()

        if isinstance(expense_copy["date"], date):
            expense_copy["date"] = expense_copy["date"].isoformat()

        data_to_save.append(expense_copy)

    with open("expense.json", "w", encoding="utf-8") as file:
        json.dump(data_to_save, file, indent=4)

    print("Expenses saved successfully.")


load()
menu()

while True:
    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Your choice must be a number.")
        continue

    if choice == 1:
        add_expense()

    elif choice == 2:
        menu()

    elif choice == 3:
        view_expenses()

    elif choice == 4:
        edit()

    elif choice == 5:
        remove_expense()

    elif choice == 6:
        statistics()

    elif choice == 7:
        save()
        break

    else:
        print("Your choice must be between 1 and 7.")
