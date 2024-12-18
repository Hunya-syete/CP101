# This will input the years of service on the taken jobs.
IT_Years = float(input("Years worked in the IT: "))
Account_Years = float(input("Years worked in the ACCT Department: "))
HR_Years =float(input("Years worked in the HR: "))

# This determines the amount of bonuses to be given depending on the years worked.
if IT_Years >= 10:
    bonus_IT = 10000
    print ("Department Bonus in the IT: 10000")
elif IT_Years < 10 and IT_Years > 0:
    bonus_IT = 5000
    print ("Department Bonus in the IT: 5000")
else:
    bonus_IT = 0
    print ("No Bonus given. Do your job.")

if Account_Years >= 10:
    bonus_acct = 12000
    print("Department Bonus in ACCT: 12000")
elif Account_Years < 10 and Account_Years > 0:
    bonus_acct = 6000
    print("ACCT Department Bonus: 6000")
else:
    bonus_acct = 0
    print ("No bonus given. Your maths are wrong.")

if HR_Years >= 10:
    bonus_HR = 15000
    print ("HR Department Bonus: 15000")
elif HR_Years < 10 and HR_Years > 0:
    bonus_HR = 7500
    print ("HR Department Bonus: 7500")
else:
    bonus_HR = 0
    print ("No bonus given, you are risking this")

 # This computes all the bonuses.
total_bonusses = bonus_IT + bonus_ACCT + bonus_HR
print (f"The total computed bonuses from each department: {total_bonusses}")
