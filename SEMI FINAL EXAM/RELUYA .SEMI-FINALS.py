# Simple Record Keeping App with Dictionary

def display_menu():
    print("\nChoose an option:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

def add_data(records):
    key = input("Enter key (e.g., Lastname): ")
    value = input("Enter value: ")
    records[key] = value
    print(f"Data added: {key} -> {value}")
    display_records(records)

def delete_data(records):
    key = input("Enter key to delete: ")
    if key in records:
        del records[key]
        print(f"Data with key '{key}' deleted.")
    else:
        print(f"Key '{key}' not found.")
    display_records(records)

def display_records(records):
    print("Current Records:")
    for key, value in records.items():
        print(f"{key}: {value}")

def main():
    records = {}
    while True:
        display_menu()
        choice = input("Enter your choice (a/b/c): ").strip().lower()
        
        if choice == 'a':
            add_data(records)
        elif choice == 'b':
            delete_data(records)
        elif choice == 'c':
            print("THANK YOU!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
