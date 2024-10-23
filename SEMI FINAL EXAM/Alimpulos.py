records = {} 

while True:
    print("Choose an option:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")

    choice = input("Enter your choice: ")

    if choice.lower() == 'a':
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        records[key] = value
        print("Data added successfully!")

    elif choice.lower() == 'b':
        key = input("Enter the Key to delete: ")
        if key in records:
            del records[key]
            print("Data deleted successfully!")
        else:
            print("Data not found!")

    elif choice.lower() == 'c':
        print("THANK YOU")
        break

    else:
        print("Invalid choice. Please try again.")
