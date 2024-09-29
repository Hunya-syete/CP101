item = "chocolate bar"
cost = 45.75 
SampleText1 = "The product is %s and the cost is %.3f." % (item, cost)
print(SampleText1)

sampleText2 = "My name is {0}, I am {1} years old, and my favorite subject is {2}."
sampleText2a = sampleText2.format("(kian", "20", "Physics")
print(sampleText2a)

sampleText3 = "Hello, I'm {0}, I'm {1} years old, and I enjoy playing {3}."
sampleText3a = sampleText3.format("kian", "20", "Physics", "Valorant")
print(sampleText3a)

sampleText4 = "I am {name}, I love eating {food}, and I am {age} years old."
sampleText4a = sampleText4.format(age="20", name="kian", food="Pasta")
print(sampleText4a)

item  = "laptop"
cost = 35000

SampleText5 = f"The item is a {item} and the cost is {cost * 1.2} pesos with tax."
print(SampleText5)
