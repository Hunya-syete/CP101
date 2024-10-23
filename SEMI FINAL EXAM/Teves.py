def add_data(data_dict):
    key = input("Enter key: ")
    value = input("Enter value: ")
    data_dict[key] = value
    print("\nData added successfully!")
    display_data(data_dict)

def delete_data(data_dict):
    key = input("Enter key to delete: ")
    if key in data_dict:
        del data_dict[key]
        print("\nData deleted successfully!")
    else:
        print("\nKey not found!")
    display_data(data_dict)

def display_data(data_dict):
    if data_dict:
        print("\nCurrent Data:")
        for key, value in data_dict.items():
            print(f"{key}: {value}")
    else:
        print("\nNo data available!")

def record_keeper():
    data_dict = {}
    
    while True:
        print("\nChoose an option:")
        print("A. Add data")
        print("B. Delete data")
        print("C. End")
        
        choice = input("Enter your choice: ").upper()

        if choice == 'A':
            add_data(data_dict)

        elif choice == 'B':
            delete_data(data_dict)

        elif choice == 'C':
            print("\nTHANK YOU!")
            break

        else:
            print("Invalid option! Please try again.")

record_keeper()
