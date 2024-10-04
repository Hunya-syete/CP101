# Get the grades from the user
programming_grade = float(input("Enter Programming Grade: "))
computing_grade = float(input("Enter computing Grade: "))
CSS_grade = float(input("Enter CSS Grade: "))

# Calculate the average grade
average_grade = (programming_grade + computing_grade + CSS_grade) / 3

# Print the average grade
print("Average Grade:", average_grade)
