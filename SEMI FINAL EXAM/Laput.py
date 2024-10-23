record = {}

def display_data():
    if record:
        for key, value in record.items():
            print(f"{key}: {value}")
    else:
        print("No records available.")

def add_data():
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    record[key] = value
    print(f"Added: {key} = {value}")

def delete_data():
    key = input("Enter Key to delete: ")
    if key in record:
        del record[key]
        print(f"Deleted: {key}")
    else:
        print("Key not found.")

def main():
    while True:
        print("\nOptions:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")
        choice = input("Choose an option: ").lower()
        
        if choice == 'a':
            add_data()
        elif choice == 'b':
            delete_data()
        elif choice == 'c':
            print("THANK YOU")
            break
        else:
            print("Invalid choice")

        display_data()

if __name__ == "__main__":
    main(
