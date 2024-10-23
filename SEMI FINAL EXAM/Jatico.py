# This indicates the addition of needed data 
def add_data(data_store):
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    data_store[key] = value
    print(f"Data added: {{{key}, {value}}}")

# This clears the data if needed to choose again
def delete_data(data_store):
    key = input("Enter Key to delete: ")
    if key in data_store:
        del data_store[key]
        print(f"Data with key '{key}' deleted.")
        print("Current data in the system:")
        for k, v in data_store.items():
            print(f"{{{k}, {v}}}")
    else:
        print(f"No data found with key '{key}'.")

# This shows the choices when adding, deleting, or ending the data gathering process
def show_menu():
    print("======================================")
    print("      RECORD KEEPING APPLICATION")
    print("======================================")
    print("These are the Available Choices for the data")
    print("a.) Add data        b.) Delete data")
    print("c.) End data")
    print()

# Dictionary is initialized when the data is stored after adding the information
def main():
    data_store = {}  
    while True:
        show_menu()
        choice = input("Enter your choice (a/b/c): ")
        
        if choice == 'a':
            add_data(data_store)
        elif choice == 'b':
            delete_data(data_store)
        elif choice == 'c':
            print("THANK YOU, for providing the needed information.")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
