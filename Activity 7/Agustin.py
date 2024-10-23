salary_changes = {}
years_of_service = int(input("Enter the number of years of service: "))
office = input("Enter the office (IT, acct, hr): ")

if office == "IT":
    if years_of_service >= 10:
        print("The salary is 10000")
    else:
        print("The salary is 5000")
elif office == "acct":
    if years_of_service >= 10:
        print("The salary is 12000")
    else:
        print("The salary is 6000")
elif office == "hr":
    if years_of_service >= 10:
        print("The salary is 15000")
    else:
        print("The salary is 7500")
else:
    print("Invalid office")


    number = {1,2,3,4,5}
