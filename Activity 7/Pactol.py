years_of_service = int(input("Enter years of service: "))
office = input("Enter office (IT, ACCT, HR): ")

if office == "IT":
    salary = 10000 if years_of_service >= 10 else 5000
elif office == "ACCT":
    salary = 12000 if years_of_service >= 10 else 6000
elif office == "HR":
    salary = 15000 if years_of_service >= 10 else 7500
else:
    salary = "Invalid office"

print("The salary is", salary)
