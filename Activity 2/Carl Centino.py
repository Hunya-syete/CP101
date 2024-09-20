
print("SUBJECTS:")

grade_1st = float(input("MATH: "))
grade_2nd = float(input("SCIENCE: "))
grade_3rd = float(input("ENGLISH: "))

resultofgrades = (grade_1st + grade_2nd + grade_3rd)/3

print("THE AVERAGE OF GRADE IS: " + str(resultofgrades))

if resultofgrades >100 or resultofgrades <=50:
    print("INVALID GRADE")


elif resultofgrades >=98:
    print("WITH HIGHEST HONOR")

elif resultofgrades >=95:
    print("WITH HIGH HONOR")

elif resultofgrades >=90:
    print("WITH HONOR")

elif resultofgrades >=75:
    print("PASSED")

else:
    print("FAILED")
