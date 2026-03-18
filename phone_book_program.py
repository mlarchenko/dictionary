phone_book = []
while True:
    command = input("Enter a command (add/delete/search/show/exit): ")
    if command == "exit":
        break
    elif command == "add":
        name = input("Enter the name: ")
        phone = input("Enter the phone number: ")
        phone_book.append({"name" : name, "phone" : phone})
    elif command == "delete":
        id = int(input("Enter user ID: "))
        phone_book.pop(id)
    elif command == "search":
        name = input("Enter the man of my dream: ")
        for person in phone_book:
            if person["name"] == name:
                print(f"User {person["name"]} - {person["phone"]}")
                break
        else:
            print("User is not found... BRUH...")
    elif command == "show":
        for cont in phone_book:
            print(cont["name"], cont["phone"])
