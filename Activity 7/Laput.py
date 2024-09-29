def calculate_salary(office, years):
    if office not in ['IT', 'acct', 'hr']:
        return "Invalid office"
    
    if years >= 10:
        if office == 'IT':
            return 10000
        elif office == 'acct':
            return 12000
        elif office == 'hr':
            return 15000
    else:
        if office == 'IT':
            return 5000
        elif office == 'acct':
            return 6000
        elif office == 'hr':
            return 7500

# User input
office = input("Enter office (IT, acct, hr): ").strip().lower()
years = int(input("Enter years in service: "))

salary = calculate_salary(office, years)
print(f"The salary for an employee in {office} with {years} years of service is: {salary}"
