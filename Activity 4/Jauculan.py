def compute_gross_pay(hours, rate):
    return hours * rate


hours_worked = float(input("Enter hours worked: "))
hourly_rate = float(input("Enter rate per hour: "))


gross_pay = compute_gross_pay(hours_worked, hourly_rate)
print(f"Gross pay is: Php.{gross_pay:.2f}")
