
def calculate_gross_pay(hours, rate):
    return hours * rate


def main():
    try:
        
        hours = float(input("Enter hours worked: "))
        
        
        rate = float(input("Enter rate per hour: "))
        
        
        gross_pay = calculate_gross_pay(hours, rate)
        
      
        print(f"Gross Pay: ${gross_pay:.2f}")
        
    except ValueError:
        print("Please enter valid numbers for hours and rate.")
