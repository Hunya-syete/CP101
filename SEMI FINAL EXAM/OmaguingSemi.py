def display_menu():
    """Display the main menu options."""
    print("\nChoose among the following:")
    print("1. Add Data")
    print("2. Delete Data")
    print("3. End")

def display_records(records):
    """Display the current records."""
    if records:
        print("Current Records:")
        for key, value in records.items():
            print(f"{key}: {value}")
    else:
        print("No records available.")

def main():
    records = {}  # Dictionary to store records

    while True:
        display_menu()
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':  # Add Data
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value  # Store the data
            print(f"Record added: {key} -> {value}")
            display_records(records)

        elif choice == '2':  # Delete Data
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]  # Remove the item
                print(f"Record deleted: {key}")
            else:
                print("Key not found. Please try again.")
            display_records(records)

        elif choice == '3':  # End
            print("THANK YOU")
            break

        else:
            print("Invalid choice. Please enter '1', '2', '3'.")
            
if __name__ == "__main__":
    main()
