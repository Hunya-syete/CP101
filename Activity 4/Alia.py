Activity 4👇
item = "Apple Pie"
cost = 35.5 
SampleText1 = "The product is %s the cost is %.5f" % (item, cost)
print(SampleText1)

sampleText2 = "My name is {}, I am {} years old, I love the subject {}"
sampleText2a = sampleText2.format("Marchel", "20", "Math")
print(sampleText2a)

sampleText3 = "My name is {0}, I am {1} years old, I love {3}"
sampleText3a = sampleText3.format("Marchel", "20", "Math", "Bloons TD 6")
print(sampleText3a)

sampleText4 = "My name is {name}, I love {food}, I am {age}."
sampleText4a = sampleText4.format(age="20", name="Marchel", food="Noodles")
print(sampleText4a)

item  = "Teddy bear"
cost = 200

SampleText5 = f"The item is a {item} and the cost is {cost * 10} pesos."
print(SampleText5)
