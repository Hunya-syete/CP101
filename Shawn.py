def calculate_salary(years_of_service, office):
    # Define salary structure based on office type and years of service
    salary_structure = {
        "IT": (10000, 5000),
        "Acct": (12000, 6000),
        "HR": (15000, 7500)
    }
    
    if office not in salary_structure:
        return "Invalid office type"
    
    # Get the salary details for the given office
    salary_above_10_years, salary_below_10_years = salary_structure[office]

    # Determine the salary based on years of service
    if years_of_service >= 10:
        return salary_above_10_years
    else:
        return salary_below_10_years

def main():
    # Input years of service and office type from the user
    years_of_service = int(input("Enter years of service: "))
    office = input("Enter office (IT, Acct, HR): ").strip().capitalize()

    # Calculate and print the salary
    salary = calculate_salary(years_of_service, office)
    print(f"The salary for the employee is: {salary}")

