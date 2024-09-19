#1

carlString1 = "Hi my name is {0} also known as {1} i love to compose {2} and also i want to be a {3} soon."

carlString2 = carlString1.format("Carl", "Almightycarl", "Rapsong", "Rapper")

print(carlString2)


#2
carlString3 = "Hi my name is {name} also known as {nickname} I love to compose {compose}."

carlString4 = carlString3.format(name="Carl", nickname="Almightycarl", compose="Rapsong")

print(carlString4)


#3
item = "COMPUTER"

cost = 99999999

carlString4 = "The product is %s the cost is %.5f" % (item, cost)

print(carlString4)
