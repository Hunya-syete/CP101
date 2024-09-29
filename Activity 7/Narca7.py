years_in_IT = float(input("Years of service rendered in IT Department: "))
years_in_ACCT = float(input("Years of service rendered in ACCT Department: "))
years_in_HR =float(input("Years of service rendered in HR: "))


if years_in_IT >= 10:
    bonus_IT = 10000
    print ("IT Department Bonus: 10000")
    
elif years_in_IT <10 and years_in_IT> 0:
    bonus_IT = 5000
    print ("IT Department Bonus: 5000")
    
else:
    bonus_IT = 0
    print ("No Bonus in IT")

if years_in_ACCT >= 10:
    bonus_ACCT = 12000
    print("ACCT Department Bonus: 12000")
    
elif years_in_ACCT <10 and years_in_ACCT> 0:
    bonus_ACCT = 6000
    print("ACCT Department Bonus: 6000")
    
else:
    bonus_ACCT = 0
    print ("No Bonus in ACCT!")

if years_in_HR >= 10:
    bonus_HR = 15000
    print ("HR Department Bonus: 15000")
    
elif years_in_HR <10 and years_in_HR> 0:
    bonus_HR = 7500
    print ("HR Department Bonus: 7500")
    
else:
    bonus_HR = 0
    print ("No Bonus in HR!")


total_bonus = bonus_IT + bonus_ACCT + bonus_HR
print (f"The total bonus of each department is: {total_bonus}")
