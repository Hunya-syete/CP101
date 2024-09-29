# Prompt the user for hours worked
hours = input("Enter hours worked: ")

# Prompt the user for the rate per hour
rate = input("Enter rate per hour: ")

# Calculate gross pay
gross_pay = float(hours) * float(rate)

# Display the result
print("Gross Pay: $", gross_pay)
