def calculate_salary(years, office):

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
        return None 
try:

    years = int(input("Enter the number of years in service: "))  
    office = input("Enter the office (it, acct, hr): ").lower()   

    salary = calculate_salary(years, office)
    

    if salary is not None:
        print(f"The salary for {years} years in the {office.upper()} department is: {salary}")
    else:
        print("Invalid office entered. Please enter one of the following: it, acct, hr.")

except ValueError:
    print("Invalid input for years. Please enter a valid number.")
