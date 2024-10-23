def record_keeping_app():
    records = {}

    while True:
        print("\nChoose an option:")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")

        option = input("Enter your choice: ").lower()

        if option == '1':
            key = input("Enter Key (Lastname): ")
            value = input(f"Enter Value for {key}: ")
            records[key] = value
            print(f"Record added: {key} -> {value}")
            print(f"Current Records: {records}")
        
        elif option == '2':
            key = input("Enter Key to delete (Lastname): ")
            if key in records:
                del records[key]
                print(f"Record deleted: {key}")
            else:
                print(f"No record found for key: {key}")
            print(f"Current Records: {records}")

        elif option == '3':
            print("THANK YOU")
            break

        else:
            print("Invalid option. Please choose again.")

record_keeping_app()
