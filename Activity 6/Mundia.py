name = input("Enter your name: ")
age = input("Enter your age: ")
# use an f-string to format the output 
print(f"Hello, {name}! You are {age} years old.")

item = "milktea"
total = 10
# Use the .format() method
sentence = "I bought {} {} today.".format(total, item)
print(sentence)
place = "America"
temperature = 36
# Use the % operator
print("The temperature in %s is %d degrees Celsius." % (place,temperature))
