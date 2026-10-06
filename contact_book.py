print("===== CONTACT BOOK =====")

contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Show Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Name likho: ")
        phone = input("Phone number likho: ")

        contacts[name] = phone
        print("Contact added!")

    elif choice == "2":
        print("\n===== CONTACTS =====")

        if len(contacts) == 0:
            print("No contacts yet.")
        else:
            for name, phone in contacts.items():
                print(name, ":", phone)

    elif choice == "3":
        name = input("Search name: ")

        if name in contacts:
            print("Phone:", contacts[name])
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Delete name: ")

        if name in contacts:
            del contacts[name]
            print("Contact deleted!")
        else:
            print("Contact not found.")

    elif choice == "5":
        print("Contact Book closed.")
        break

    else:
        print("Invalid option. Please try again.")

print("Powered by : RAJ.K.M ©")