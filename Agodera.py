names = []

for i in range(5):
    name = input("Enter name " + str(i + 1) + ": ")
    names.append(name)

print("Names in uppercase:")
for name in names:
    print(name.upper())
