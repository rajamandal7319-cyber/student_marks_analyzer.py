print("===== EXPENSE TRACKER =====")

expenses = []

while True:
    print("\n1. Add Expense")
    print("2. Show Expenses")
    print("3. Show Total")
    print("4. Delete Expense")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Expense ka naam: ")
        amount = float(input("Amount ₹: "))

        expenses.append([name, amount])
        print("Expense added!")

    elif choice == "2":
        print("\n===== YOUR EXPENSES =====")

        if len(expenses) == 0:
            print("No expenses yet.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, ".", expense[0], "- ₹", expense[1])

    elif choice == "3":
        total = 0

        for expense in expenses:
            total = total + expense[1]

        print("Total Expense: ₹", total)

    elif choice == "4":
        if len(expenses) == 0:
            print("No expenses to delete.")
        else:
            for i, expense in enumerate(expenses, 1):
                print(i, ".", expense[0], "- ₹", expense[1])

            number = int(input("Kaunsa expense delete karna hai? "))

            if 1 <= number <= len(expenses):
                deleted = expenses.pop(number - 1)
                print("Deleted:", deleted[0])
            else:
                print("Invalid expense number.")

    elif choice == "5":
        print("Expense Tracker closed.")
        break

    else:
        print("Invalid option. Please try again.")

print("Powered by : RAJ.K.M ©")