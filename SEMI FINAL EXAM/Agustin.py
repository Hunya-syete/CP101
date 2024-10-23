def record_keeping_app():
    records = {}  
    while True:
        print("\nChoose an option:")
        print("a. Add Data")
        print("b. Delete Data")
        print("c. End")

        choice = input("Enter your choice (a/b/c): ").strip().lower()

        if choice == 'a':  
            key = input("Enter Key: ").strip()  
            value = input("Enter Value: ").strip() 
            records[key] = value  
            print(f"Data added: {key} -> {value}")  
            print("Current Records:", records) 

        elif choice == 'b':  
            key = input("Enter Key to delete: ").strip()  
            if key in records:
                del records[key]  
                print(f"Data deleted for key: {key}")  
            else:
                print("Key not found.")  
            print("Current Records:", records)  

        elif choice == 'c':  
            print("THANK YOU")  
            break  

        else:
            print("Invalid choice. Please try again.")  


record_keeping_app()
