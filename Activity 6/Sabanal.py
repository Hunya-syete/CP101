# Part 1: Basic f-string Formatting
name = input("Enter your name: ")
age = input("Enter your age: ")
# Use an f-string to format the output
print(f"Hello, {name}! You are {age} years old.")

# Part 2: Using .format()
item = "apples"
count = 5
# Use the .format() method
sentence = "I bought {} {} today.".format(count, item)
print(sentence)

# Part 3: Legacy % formatting
city = "New York"
temperature = 22
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (city, temperature))
