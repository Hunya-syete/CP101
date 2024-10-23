def record_keeper():
    records = {}

    while True:
        print("Choose an option:")
        print("A. Add Data")
        print("B. Delete Data")
        print("C. End")
        choice = input("Enter your choice (A/B/C): ").strip().upper()

        if choice == 'A':
            key = input("Enter key: ")
            value = input("Enter value: ")
            records[key] = value
            print("Current records:", records)

        elif choice == 'B':
            key = input("Enter key to delete: ")
            if key in records:
                del records[key]
                print("Current records:", records)
            else:
                print("Key not found.")

        elif choice == 'C':
            print("THANK YOU")
            break

        else:
            print("Invalid choice. Please try again.")

record_keeper()
