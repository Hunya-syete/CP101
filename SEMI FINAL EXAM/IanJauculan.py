def record_keeping_app():
    records = {}

    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value
            print(f"Added: {key} -> {value}")
            print("Current Records:", records)

        elif choice == 'b':
            key = input("Enter Key: ")
            if key in records:
                del records[key]
                print(f"Deleted: {key}")
            else:
                print(f"Key '{key}' not found.")
            print("Current Records:", records)

        elif choice == 'c':
            print("THANK YOU")
            break

        else:
            print("Invalid choice. Please select a valid option.")

record_keeping_app()
