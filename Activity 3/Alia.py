# Write a program to prompt the user for hours and rate per hour to compute gross pay.
hours = float(input("Total of hours work: ")) # Will ask the user to enter number of hours work.
rate_per_hour = float(input("Enter desired rate: ")) # Will ask the user to enter the rate per hour.
gross_pay = hours * rate_per_hour # Formula for computing the gross pay.
print (f"Total Gross Pay:  {gross_pay:.2f}") # Will print the total gross pay using f-string format and .2f to record two decimal places.
