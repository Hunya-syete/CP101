class RecordKeeper:
    def __init__(self):
        self.records = {}

    def add_data(self):
        """Add data to the records"""
        key = input("Enter Key: ")
        value = input("Enter Value: ")
        self.records[key] = value
        print("Data added successfully!")

    def delete_data(self):
        """Delete data from the records"""
        key = input("Enter Key: ")
        if key in self.records:
            del self.records[key]
            print("Data deleted successfully!")
        else:
            print("Key not found in records.")

    def display_records(self):  
        """Display the current records"""
        print("\nCurrent Records:")
        for key, value in self.records.items():
            print(f"{key}: {value}")

    def run(self):
        """Run the Record Keeping App"""
        while True:
            print("\nRecord Keeping App")
            print("1. Add Data")
            print("2. Delete Data")
            print("3. End")
            choice = input("Choose an option: ")
            if choice == "1":
                self.add_data()
                self.display_records()
            elif choice == "2":
                self.delete_data()
                self.display_records()
            elif choice == "3":
                print("THANK YOU")
                break
            else:
                print("Invalid option. Please choose again.")

if __name__ == "__main__":
    app = RecordKeeper()
    app.run()
