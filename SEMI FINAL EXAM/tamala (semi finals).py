def record_keeping_app():
    record = {}

    while True:
        
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        choice = input("Enter your choice (a/b/c): ").lower()

        
        if choice == 'a':
            key = input("Enter Key: ")
            value = input(f"Enter Value for {key}: ")
            record[key] = value
            print("\nCurrent Record:")
            print(record)

       
        elif choice == 'b':
            key = input("Enter Key to delete: ")
            if key in record:
                del record[key]
                print(f"\n'{key}' has been deleted.")
            else:
                print(f"\nKey '{key}' not found.")
            print("\nCurrent Record:")
            print(record)

        
        elif choice == 'c':
            print("\nTHANK YOU")
            break

        
        else:
            print("Invalid choice, please select again.")

record_keeping_app()
