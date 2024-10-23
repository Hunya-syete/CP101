records = {}  # Initialize an empty dictionary

while True:
    print("1. Add Data")
    print("2. Delete Data")
    print("3. End")
    choice = input("Enter your choice: ")

    if choice == '1':
        key = input("Enter Key (Lastname): ")
        value = input("Enter Value: ")
        records[key] = value
        print("Records:", records)
    elif choice == '2':
        key = input("Enter Key (Lastname) to delete: ")
        if key in records:
            del records[key]
            print("Records:", records)
        else:
            print("Key not found.")
    elif choice == '3':
        print("THANK YOU")
        break
    else:
        print("Invalid choice.")
