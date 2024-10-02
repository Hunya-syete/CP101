office = (input("enter course (it,hm,acct):"))
salary = int(input("enter more/equal 10 years:"))


if office == "it":
    if salary >= 10:
        print(10000)
    elif salary <= 10:
        print(5000)

if office == "hm":
    if salary >= 10:
        print(12000)
    elif salary <= 10:
        print(6000)

if office == "acct":
    if salary >= 10:
        print(15000)
    elif salary <= 10:
        print(7500)
