#Part 1: Basic f-string Formatting
#Prompt the user for input and display it using f-strings. 
Name = (input("What's up! what is your name?: "))
age = (input("pilay edad nimo?:"))
print(f"hello {Name}! sana oil {age} na!")



# Part 2: Using  .format() 
product = "burger/s"
count = 5
# Use the .format() method
Meow = "I ate {} {} today.".format(count, product)
print(Meow)



#Part 3: Legacy % formatting
## Use the % formatting for displaying a string.
city = "Philippines"
temp = 39
print("The temperature in %s is %d degree celcius." % (city,temp))
