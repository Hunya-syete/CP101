# Create a Python code that solves the following exercises by applying the appropriate string 

# Part 1: Basic f-string Formatting
# Prompt the user for input.

name = input("unsay name nimo? ")
hobby = input("unsay hobby nimo? ")
kpop_idol = input("kinsa imong kpop idol? ")

# Using an f-string to format the output

print (f"Hi, my name is {name}, my hobby is {hobby} . I idolized {kpop_idol}.")


# Part 2: Using  .format()
# Prompt the user for input.

game_name1 = input("favorite game name: ")
game_name2 = input("least game name: ")

# Using .format()

message = "My favorite game is {} and least favorite is {}." .format(game_name1, game_name2)
print (message)


# Part 3: Legacy % formatting.

country = "Thailand"
weather_celsious = 36
weather_fahrenheit = 90.2
input("Omg! init kaayos Thailand oy.")

# Using % operator

print ("Weather in the %s is %d degrees in celcious and %.1f in fahrenheit." % (country, weather_celsious, weather_fahrenheit))
