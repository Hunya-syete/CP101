item = "orange juice can"
cost = 35.5 
SampleText1 = "The product is %s the cost is %.5f" % (item, cost)
print(SampleText1)

sampleText2 = "My name is {jommil}, I am {19} years old, I love the subject {CP}"
sampleText2a = sampleText2.format("Jommil", "19", "CP")
print(sampleText2a)

sampleText3 = "My name is {0}, I am {1} years old, I love {3}"
sampleText3a = sampleText3.format("Jommil", "19", "CP", "Minecraft")
print(sampleText3a)

sampleText4 = "My name is {Jommil}, I love {burger}, I am {19}."
sampleText4a = sampleText4.format(age="19", name="Jommil", food="burger")
print(sampleText4a)

item  = "smart watch"
cost = 200

SampleText5 = f"The item is a {fruties} and the cost is {cost * 10} pesos."
print(SampleText5)