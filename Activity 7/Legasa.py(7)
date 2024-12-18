# Function to calculate salary based on office and years in service
def calculate_salary(years, office):
    # Define salary brackets based on years and office
    if office == 'it':
        if years >= 10:
            return 10000
        else:
            return 5000
    elif office == 'acct':
        if years >= 10:
            return 12000
        else:
            return 6000
    elif office == 'hr':
        if years >= 10:
            return 15000
        else:
            return 7500
    else:
        return "Invalid office entered!"

# Input from user for years in service and office
years_in_service = int(input("Enter the number of years in service: "))
office = input("Enter the office (it, acct, hr): ").lower()

# Calculate the salary
salary = calculate_salary(years_in_service, office)

# Output the salary or error message
print(f"Salary: {salary}")
