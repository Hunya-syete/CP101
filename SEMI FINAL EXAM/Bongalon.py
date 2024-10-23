# Record Keeping App

# Dictionary to store records
data_store = {}

while True:
    print("\nOptions:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    option = input("Select an option (a/b/c): ")

    if option == 'a':
        # Add Data
        key = input("Enter a new key: ")
        if key in data_store:
            print(f"The key '{key}' already exists. Try a different key.")
        else:
            value = input(f"Enter a value for '{key}': ")
            data_store[key] = value
            print(f"Record added: {key} = {value}")
        print("Current Records:", data_store)

    elif option == 'b':
        # Delete Data
        key = input("Enter the key to remove: ")
        if key in data_store:
            del data_store[key]
            print(f"Record '{key}' removed.")
        else:
            print(f"No record found for key: '{key}'")
        print("Current Records:", data_store)

    elif option == 'c':
        # End
        print("Thank you!")
        break

    else:
        print("Invalid option, please choose again.")
