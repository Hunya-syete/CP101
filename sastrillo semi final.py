def record_keeping_():
    records = {} 

    while True:
        print("\nChoose an option:")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")

        choice = input("Enter your choice (1/2/3): ").strip().lower()

        if choice == '1':  
            key = input("Enter Key: ").strip()
            value = input("Enter Value: ").strip()
            records[key] = value  
            print(f"Data added: {key} -> {value}")
            print("Current Records:", records)

        elif choice == '2': 
            key = input("Enter Key to delete: ").strip()
            if key in records:
                del records[key]  
                print(f"Data deleted for key: {key}")
            else:
                print("Key not found.")
            print("Current Records:", records)

        elif choice == '3': 
            print("THANK YOU")
            break 

        else:
            print("Invalid choice. Please try again.")


record_keeping_()
