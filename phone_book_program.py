phone_book = []
while True:
    command = input("Enter a command (add/delete/search/show/exit")
    if command == "exit":
        break
    elif command == "add":
        name = input("Enter the name: ")
        phone = input("Enter the phone number")
        phone_book.append({"name" : name, "phone" : phone})
