# Using str.format() with positional placeholders
sampleText1 = "My name is {}. I love {}. I love playing {}. {}"
sampleText1a = sampleText1.format("Shawn Michael", "Chicken", "Mobile Legends", "Apple")
print(sampleText1a)

# Using str.format() with indexed placeholders
sampleText2 = "My name is {1}. I love {2}. I love playing {0}."
sampleText2a = sampleText2.format("COD", "Shawn Michael", "Chicken", "Mobile Legends", "Apple")
print(sampleText2a)

# Using str.format() with named placeholders
sampleText3 = "My name is {name}. I love {food}. I love playing {play}."
sampleText3a = sampleText3.format(food="Chicken", play="Mobile Legends", name="Shawn Michael")
print(sampleText3a)

# Using old-style string formatting
item = "Lamborgini"
cost = 2100000
SampleText4 = "The product is %s and the cost is %.5f." % (item, cost)
print(SampleText4)

# Using f-strings (Python 3.6+)
item = "Iphone16"
cost = 100000
SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)
