# It will input the employee's years of service rendered in each category.
IT_yrs = float(input("Years serviced in IT Dept.: "))
ACCT_yrs = float(input("Years serviced in ACCT Dept.: "))
HR_yrs = float(input("Years servicedin HR Dept.: "))

# Amount of bonuses to be given.
if IT_yrs >= 10:
    IT_bns = 10000
    print ("Bonus in IT Dept.: 10000")
elif IT_yrs < 10 and IT_yrs > 0:
    IT_bns = 5000
    print ("Bonus in IT Dept.: 5000")
else:
    IT_bns = 0
    print ("Don't expect. There is no bonus in IT!")

if ACCT_yrs >= 10:
    ACCT_bns = 12000
    print("Bonus in ACCT Dept.: 12000")
elif ACCT_yrs < 10 and ACCT_yrs > 0:
    ACCT_bns = 6000
    print("Bonus in ACCT Dept.: 6000")
else:
    ACCT_bns = 0
    print ("No Bonus. Betterluck next time ;> ")

if HR_yrs >= 10:
    HR_bns = 15000
    print ("Bonus in HR Dept.: 15000")
elif HR_yrs < 10 and HR_yrs > 0:
    HR_bns= 7500
    print ("Bonus in HR Dept.: 7500")
else:
    HR_bns= 0
    print ("No bonus again.")

# Computes all bonuses.
a_bns = IT_bns + ACCT_bns + HR_bns
print (f"The total computed bonuses from each department: {a_bns}")



