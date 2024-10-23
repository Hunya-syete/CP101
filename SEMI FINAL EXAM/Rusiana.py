records = {}  # Create an empty dictionary to store the records

while True:
  print("Choose an option:")
  print("a. Add Data")
  print("b. Delete Data")
  print("c. End")

  choice = input("Enter your choice: ")

  if choice == 'a':
    key = input("Enter Key: ")
    value = input("Enter Value: ")
    records[key] = value  # Add the key-value pair to the dictionary
    print("Data added successfully!")
    print(records)  # Display the updated dictionary

  elif choice == 'b':
    key = input("Enter Key: ")
    if key in records:  # Check if the key exists in the dictionary
      del records[key]  # Delete the key-value pair
      print("Data deleted successfully!")
      print(records)  # Display the updated dictionary
    else:
      print("Key not found!")

  elif choice == 'c':
    print("THANK YOU")
    break  # Exit the loop

  else:
    print("Invalid choice. Please try again.")
