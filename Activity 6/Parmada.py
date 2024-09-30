# Create a Python code that solves the following exercises by applying the appropriate string 

#1:Basic f-string Formatting
n = input("What is your name? ")
h = input("How old are you? ")
fav_colour = input("Your favorite colour? ")

# Using an f-string to format the output
print (f"Hi! I am {n}. A {h} years old student and my favorite colour is {fav_colour}.")


#2:Using  .format()
# Prompt the user for input.
bn1 = input("Your fav. brand: ")
bn2 = input("Your least fav. brand: ")

# Using .format()
text = "My fav. brand is {} and least fav. brand is {}." .format(bn1, bn2)
print (text)


#3: Legacy % formatting.
ct = "Dubai"
weath_c = 38
weath_f = 43.5

# Using % operator
print ("Weather in the %s is %d degrees in celcious and %.5f in fahrenheit." % (ct, weath_c, weath_f))
