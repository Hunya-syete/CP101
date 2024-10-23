class RecordKeeper:
    def __init__(self):
        self.records = {}  # Initialize an empty dictionary to store records

    def add_data(self):
        """Add data to the records"""
        key = input("Enter Key: ")  # Prompt user for the key
        value = input("Enter Value: ")  # Prompt user for the value
        self.records[key] = value  # Store the key-value pair in the dictionary
        print("Data added successfully!")
        self.display_records()  # Display current records after adding

    def delete_data(self):
        """Delete data from the records"""
        key = input("Enter Key: ")  # Prompt user for the key to delete
        if key in self.records:
            del self.records[key]  # Remove the key-value pair from the dictionary
            print("Data deleted successfully!")
        else:
            print("Key not found in records.")  # Inform if key does not exist
        self.display_records()  # Display current records after deletion

    def display_records(self):
        """Display the current records"""
        if self.records:  # Check if there are any records
            print("\nCurrent Records:")
            for key, value in self.records.items():  # Iterate through the records
                print(f"{key}: {value}")  # Print each key-value pair
        else:
            print("No records available.")  # Inform if there are no records

    def run(self):
        """Run the Record Keeping App"""
        while True:
            print("\nRecord Keeping App")
            print("1. Add Data")
            print("2. Delete Data")
            print("3. End")
            choice = input("Choose an option: ")  # Prompt user for an option
            if choice == "1":
                self.add_data()  # Call add_data method
            elif choice == "2":
                self.delete_data()  # Call delete_data method
            elif choice == "3":
                print("THANK YOU")  # Print thank you message
                break  # Exit the loop and end the program
            else:
                print("Invalid option. Please choose again.")  # Handle invalid input

if __name__ == "__main__":
    app = RecordKeeper()  # Create an instance of RecordKeeper
    app.run()  # Run the application
