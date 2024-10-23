def main():
    records = {}

    while True:
        print("\nRecord Keeper")
        print("1. Add Data")
        print("2. Delete Data")
        print("3. End")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            key = input("Enter Key: ")
            value = input("Enter Value: ")
            records[key] = value
            print(f"Record added: {key} - {value}")
            
            
            print("Current Records:")
            if not records:
                print("No records to display.")
            else:
                for a, z in records.items():
                    print(f"{a} - {z}")
            
        elif choice == '2':
            key = input("Enter Key to delete: ")
            if key in records:
                del records[key]
                print(f"Record deleted: {key}")
                
                
                print("Current Records:")
                if not records:
                    print("No records to display.")
                else:
                    for a, z in records.items():
                        print(f"{a} - {z}")
            else:
                print(f"Record not found: {key}")
                
        elif choice == '3':
            print("THANK YOU")
            break
            
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
