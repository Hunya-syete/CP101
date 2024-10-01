
years_of_service = int(input("Years the employee has been in service? "))
office = input("What office do you belong to (it, acct, hr)? ").lower()  # Ensure office is lowercased


payment_criteria = {
    "it": {10: 10000, "else": 5000},
    "acct": {10: 12000, "else": 6000},
    "hr": {10: 15000, "else": 7500}
}

if office in payment_criteria:
    
    if years_of_service >= 10:
        amount = payment_criteria[office][10]
    else:
        amount = payment_criteria[office]["else"]
    
    
    print(f"As an employee of the {office.upper()} office with {years_of_service} years of service, your payment is Pesos {amount}.")
else:
    print("Invalid office entered. Please enter one of the following: it, acct, hr.")
  
