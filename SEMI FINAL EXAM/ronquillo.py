# Record Keeping App

# Initialize an empty dictionary to store records
records = {}

# Function to add a new record
def add_record():
    key = input("Enter key (e.g. Last name): ")
    value = input("Enter value (e.g. Doe): ")
    records[key] = value
    print(f"\nRecord '{key}: {value}' has been added.\n")
    display_records()

# Function to view all records
def display_records():
    if records:
        print("--- Current Records ---")
        for key, value in records.items():
            print(f"{key}: {value}")
        print()
    else:
        print("No records found.\n")

# Function to delete a record
def delete_record():
    key = input("Enter key to delete: ")
    if key in records:
        del records[key]
        print(f"\nRecord '{key}' has been deleted.\n")
    else:
        print(f"\nRecord '{key}' not found.\n")
    display_records()

# Main app loop with choices
def record_keeping_app():
    while True:
        print("Choose an option:")
        print("a. Add data")
        print("b. Delete data")
        print("c. End")
        choice = input("Enter your choice: ").lower()

        if choice == 'a':
            add_record()
        elif choice == 'b':
            delete_record()
        elif choice == 'c':
            print("THANK YOU")
            break
        else:
            print("Invalid choice. Please try again.\n")

# Run the app
record_keeping_app()
Choose an option:

a. Add data

b. Delete data

c. End

Enter your choice: a

Enter key (e.g. Last name): RONQUILLO

Enter value (e.g. Doe): LOVELY



Record 'RONQUILLO: LOVELY' has been added.



--- Current Records ---

RONQUILLO: LOVELY



Choose an option:

a. Add data

b. Delete data

c. End

Enter your choice: b

Enter key to delete: RONQUILLO



Record 'RONQUILLO' has been deleted.



No records found.



Choose an option:

a. Add data

b. Delete data

c. End

Enter your choice: c

THANK YOU



=== Code Execution Successful ===
