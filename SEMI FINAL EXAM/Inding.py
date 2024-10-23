class record_keeping_app():
    records = {} 

    while True:
        print("Choose an option:")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            key = input("Enter Key (Lastname): ")
            value = input("Enter Value: ")
            records[key] = value
            print("Record added successfully!")

        if choice == 2:
            key = input("Enter Key (Lastname) to delete: ")
            if key in records:
                del records[key]
                print("Record deleted successfully!")
            else:
                print("Record not found.")

        if choice == 3:
            print("THANK YOU!")
            break

        else:
            print("Invalid choice. Please try again.")

        print("\nCurrent Records:")
        for key, value in records.items():
            print(f"{key}: {value}")
        print()

if __name__ == "__main__":
    record_keeping_app()
