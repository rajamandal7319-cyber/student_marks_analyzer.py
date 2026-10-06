print("===== TO-DO LIST =====")

tasks = []

while True:
    print("\n1. Add Task")
    print("2. Show Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Task likho: ")
        tasks.append(task)
        print("Task added!")

    elif choice == "2":
        print("\n===== YOUR TASKS =====")

        if len(tasks) == 0:
            print("No tasks yet.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, task in enumerate(tasks, 1):
                print(i, ".", task)

            number = int(input("Kaunsa task delete karna hai? "))
            if 1 <= number <= len(tasks):
                deleted = tasks.pop(number - 1)
                print("Deleted:", deleted)
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("To-Do List closed.")
        break

    else:
        print("Invalid option. Please try again.")

print("Powered by : RAJ.K.M ©")