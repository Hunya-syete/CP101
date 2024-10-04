hours = float(input("Enter hours: "))
rate = float(input("Enter rate: "))

# Calculate the total pay
total_pay = hours * rate

# Print the total pay
print("The total pay is: ${:.2f}".format(total_pay))
