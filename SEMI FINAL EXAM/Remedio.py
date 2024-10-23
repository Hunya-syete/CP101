records = {}

while True:
    
    print("\nSelect an option:")
    print("a. Add Data")
    print("b. Delete Data")
    print("c. End")
    
    choice = input("Enter your answer (a/b/c): ").lower()
    
    if choice == 'a':
        
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        records[key] = value
        print("\nData added successfully!")
        print(f"Current Records: {records}")
    
    elif choice == 'b':
        
        key = input("Enter Key to delete: ")
        if key in records:
            del records[key]
            print("\nData deleted successfully!")
        else:
            print("\nKey not found.")
        print(f"Current Records: {records}")
    
    elif choice == 'c':
        
        print("THANK YOU")
        break
    
    else:
        print("Invalid choice, please select a, b, or c.")
