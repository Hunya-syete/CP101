IT = float(input("Years of service rendered in IT Department: "))
ACCT = float(input("Years of service rendered in ACCT Department: "))
HR = float(input("Years of service rendered in HR: "))

# Will check for the amount of bonuses to be given.
if IT >= 10:
    bonus_IT = 10000
    print ("IT Department Bonus: 10000")
  
elif IT < 10 and years_in_IT > 0:
    bonus_IT = 5000
    print ("IT Department Bonus: 5000")
  
else:
    IT = 0
    print ("No Bonus in IT!")

if ACCT >= 10:
   bonus_ACCT = 12000
    print("ACCT Department Bonus: 12000")

elif ACCT < 10 and years_in_ACCT > 0:
    bonus_ACCT = 6000
    print("ACCT Department Bonus: 6000")

else:
    bonus_ACCT = 0
    print ("No Bonus in ACCT!")

if HR >= 10:
    bonus_HR = 15000
    print ("HR Department Bonus: 15000")
  
elif HR < 10 and years_in_HR > 0:
    bonus_HR = 7500
    print ("HR Department Bonus: 7500")

else:
    bonus_HR = 0
    print ("No Bonus in HR!")

# Computation of all Bonuses receive.
total_bonusses = bonus_IT + bonus_ACCT + bonus_HR
print (f"The total bonus of each department is: {total_bonusses}")
  
