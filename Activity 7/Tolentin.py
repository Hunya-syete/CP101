class EmployeeOffice:
    def __init__(self, it_dept, acct_dept, hr_dept):
        # Initialize years of service for each department
        self.it_dept = it_dept
        self.acct_dept = acct_dept
        self.hr_dept = hr_dept

    def display_service_years(self):
        # Display years of service in each department
        print("Years of service rendered in IT Department: {:.2f}".format(self.it_dept))
        print("Years of service rendered in ACCT Department: {:.2f}".format(self.acct_dept))
        print("Years of service rendered in HR: {:.2f}".format(self.hr_dept))


# List to store employee office information
employee_office_list = []

while True:
    # Get input for employee years of service
    it_dept_years = float(input("Enter years of service in IT Department: "))
    acct_dept_years = float(input("Enter years of service in ACCT Department: "))
    hr_dept_years = float(input("Enter years of service in HR: "))
    print("\n")

    # Calculate and display bonus for IT department
    if it_dept_years >= 10:
        it_bonus = 10000
        print("IT Department Bonus: {:.2f}".format(it_bonus))
    elif 0 < it_dept_years < 10:
        it_bonus = 5000
        print("IT Department Bonus: {:.2f}".format(it_bonus))
    else:
        it_bonus = 0
        print("NO BONUS IN IT!")

    print("\n")

    # Calculate and display bonus for Accounting department
    if acct_dept_years >= 10:
        acct_bonus = 12000
        print("ACCT Department Bonus: {:.2f}".format(acct_bonus))
    elif 0 < acct_dept_years < 10:
        acct_bonus = 6000
        print("ACCT Department Bonus: {:.2f}".format(acct_bonus))
    else:
        acct_bonus = 0
        print("NO BONUS IN ACCT!")

    print("\n")

    # Calculate and display bonus for HR department
    if hr_dept_years >= 10:
        hr_bonus = 15000
        print("HR Department Bonus: {:.2f}".format(hr_bonus))
    elif 0 < hr_dept_years < 10:
        hr_bonus = 7500
        print("HR Department Bonus: {:.2f}".format(hr_bonus))
    else:
        hr_bonus = 0
        print("NO BONUS IN HR")

    print("\n")

    # Ask the user if they want to create another employee record
    user_choice = input("Create another employee record? (Y/N): ")
    if user_choice.upper() == "Y":
        continue
    else:
        break

    print("\n")
