def record_keeping_app():
    records = {}  # Dictionary to store key-value pairs
    
    while True:
        
        print("\nChoose an option:")
        print("A. Add data")
        print("B. Delete data")
        print("C. End")
        choice = input("Enter your choice (A, B, C): ").strip().upper()
        
        if choice == 'A':
            
            key = input("Enter key: ").strip()
            value = input("Enter value: ").strip()
            records[key] = value
            print("\nData added!")
            print("Current Records:", records)
        
        elif choice == 'B':
            
            key = input("Enter the key to delete: ").strip()
            if key in records:
                del records[key]
                print("\nData deleted!")
            else:
                print("\nKey not found!")
            print("Current Records:", records)
        
        elif choice == 'C':
            
            print("THANK YOU")
            break
        
        else:
            # Invalid choice
            print("\nInvalid choice, please select A, B, or C.")


record_keeping_app()
