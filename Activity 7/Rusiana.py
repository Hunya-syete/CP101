print("Welcome to the Employee Bonus Calculator!")

def calculate_bonus(years_of_service):
  """Calculates the bonus based on years of service."""
  if years_of_service >= 10:
    return 10000
  elif 0 < years_of_service < 10:
    return 5000
  else:
    return 0

while True:
  it_years = float(input("Enter years of service in IT: "))
  acct_years = float(input("Enter years of service in Accounting: "))
  hr_years = float(input("Enter years of service in HR: "))

  print("\nBonus Breakdown:")
  print(f"IT Department Bonus: {calculate_bonus(it_years)}")
  print(f"Accounting Department Bonus: {calculate_bonus(acct_years)}")
  print(f"HR Department Bonus: {calculate_bonus(hr_years)}")

  continue_choice = input("\nDo you want to calculate bonuses for another employee? (y/n): ")
  if continue_choice.lower() != 'y':
    break

print("\nThank you for using the Employee Bonus Calculator!")
