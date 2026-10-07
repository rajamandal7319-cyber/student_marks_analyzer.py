print("===== NOTES MANAGER =====")

while True:
    print("\n1. Add Note")
    print("2. Show Notes")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        note = input("Note likho: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")

        print("Note saved!")

    elif choice == "2":
        try:
            with open("notes.txt", "r") as file:
                notes = file.read()

            if notes == "":
                print("No notes yet.")
            else:
                print("\n===== YOUR NOTES =====")
                print(notes)

        except FileNotFoundError:
            print("No notes yet.")

    elif choice == "3":
        print("Notes Manager closed.")
        break

    else:
        print("Invalid option.")

print("Powered by : RAJ.K.M ©")