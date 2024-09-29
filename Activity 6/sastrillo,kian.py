# Part 1: Basic f-string Formatting
# Prompt the user for input.
user_name = input("What is your name? ")
user_course = input("What course are you taking? ")
user_color = input("What is your favorite color? ")

# Using an f-string to format the output
print(f"Hello! I'm {user_name}, studying {user_course}, and I love the color {user_color}.")

# Part 2: Using .format()
# Prompt the user for input.
preferred_brand = input("What is your favorite brand? ")
unpreferred_brand = input("What is your least favorite brand? ")

# Using .format()
formatted_message = "I prefer {} over {}, which I don't like much." .format(preferred_brand, unpreferred_brand)
print(formatted_message)

# Part 3: Legacy % formatting.
nation = "Canada"
temperature_celsius = 22
temperature_fahrenheit = 71.6

# Using % operator
print("In %s, the temperature is %d degrees Celsius and %.1f degrees Fahrenheit." % (nation, temperature_celsius, temperature_fahrenheit))
