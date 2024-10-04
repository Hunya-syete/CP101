# Part 1: Basic f-string Formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Your name is {name} and you are {age} years old.")

# Part 2: Using .format()
items = ["Grapes", "Banana", "Orange"]
prices = [10, 10, 10]

print("{:<10} {:<10}".format("Item", "Price"))
for item, price in zip(items, prices):
    print("{:<10} {:<10.2f}".format(item, price))

item = "Banana"
count = 3

sentence = "I have 500 pesos and I buy {} {} today.".format(count,item)
# Part 3: Legacy % formatting
barangay = "Guinles"
temperature = 25
print("The temperature in %s is %d degrees Celsius. " % (barangay, temperature)) 
