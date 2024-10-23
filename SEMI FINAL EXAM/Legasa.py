data_dict = {}

while True:
    print("\nChoose an option: a. Add Data b. Delete Data c. End")
    option = input("Enter your choice: ")

    if option.lower() == 'a':
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        data_dict[key] = value
        print("\nCurrent Data:")
        for key, value in data_dict.items():
            print(f"{key}: {value}")
    elif option.lower() == 'b':
        key = input("Enter Key: ")
        if key in data_dict:
            del data_dict[key]
            print(f"Item with key '{key}' deleted successfully.")
        else:
            print(f"Key '{key}' not found in the dictionary.")
    elif option.lower() == 'c':
        print("THANK YOU")
        break
    else:
        print("Invalid option. Please choose from 'a', 'b', or 'c'.")
