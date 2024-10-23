def record_keeping_app():
    # Initialize the dictionary to store records
    records = {}

    while True:
        # Display menu options
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        # Take user input for the option
        option = input("Enter your choice: ").lower()

        if option == 'a':
            # Add Data option
            key = input("Enter Key (Lastname): ")
            value = input(f"Enter Value for {key}: ")
            records[key] = value
            print(f"Record added: {key} -> {value}")
            print(f"Current Records: {records}")
        
        elif option == 'b':
            # Delete Data option
            key = input("Enter Key to delete (Lastname): ")
            if key in records:
                del records[key]
                print(f"Record deleted: {key}")
            else:
                print(f"No record found for key: {key}")
            print(f"Current Records: {records}")

        elif option == 'c':
            # End option
            print("THANK YOU")
            break

        else:
            print("Invalid option. Please choose again.")

# Run the app
record_keeping_app()
