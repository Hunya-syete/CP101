# ( == Code 1 of 2 for Midterm Exam == )

# This determines the user when the number is inputted
number_input = float(input("Enter the Number: "))

# This checks if the number is positive, negative, or zero
if number_input == 0:
    print("This number is zero.")
if number_input > 0:
    print("This number is positive.")
if number_input < 0:
    print("This number is negative.")

# ( == Code 2 of 2 for Midterm Exam == )

# This determines if user wants to input 5 names
enter_input = input("Do you want to Enter Five Names in Uppercase? (yes/no): ")
if enter_input == "yes":
    
# This lets the user input the names 
        names = []
        for i in range(5):
            name = input(f"Enter name {i+1}: ")
            names.append(name)

# This prints the names, in uppercase, in string format, and in loops
        for name in names:
            print(f"{name.upper()}")
