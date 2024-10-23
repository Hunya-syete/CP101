def record_keeping_app():
    records = {} 

    while True:
        
        choice = input("\nChoose an option (a: Add, b: Delete, c: End): ").strip().lower()

        if choice == 'a':
          
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value  
            
            print("Current Records:", records)

        elif choice == 'b':
            
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]  
                
                print(f"Deleted record with key '{key}'.")
            else:
                print(f"No record found with key '{key}'.")
            print("Current Records:", records) 

        elif choice == 'c':
           
            print("THANK YOU")
            break  

        else:
            print("Invalid choice. Try again.")


record_keeping_app()
