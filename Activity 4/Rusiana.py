# Get user's information
name = input("What's your name? ")
age = input("How old are you? ")
hobby = input("What's your favorite hobby? ")
place = input("What's your favorite place? ")
color = input("What's your favorite color? ")
dream = input("What's your biggest dream? ")

# Create a formatted string using f-strings
introduction = f"""
Hi, my name is {name}. I am {age} years old. 
My favorite hobby is {hobby}. I love going to {place}. 
My favorite color is {color}. My biggest dream is to {dream}.
"""

# Example using a % function
item = "apple"
cost = 20.00
sampletext4 = "The product %s cost %.2f" % (item, cost)
print (sampletext4)
