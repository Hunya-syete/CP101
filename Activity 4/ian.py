sampleText1 = "My name {}. i love {}. and playing. {}"
sampleText1a = sampleText1.format("Gerald", "Joyride", "mobilelegend")
print(sampleText1a)

sampleText2 = "My name is {1} i love {0} and playing {2}"
sampleText2a = sampleText2.format("tiger", "Gerald", "mobilelegend")
print(sampleText2a)

Meow3 = "My name is {name}, and i love eating {food} and I also love to play {sport}"
Meow3a = Meow3.format(food="manggo", sport="basketball", name="Gerald")
print(Meow3a)

item = "adobo"
cost = 35.5
Dog4 = "The product is %s the cost is %.5f." % (item, cost)
print(Dog4)

item = "tinulang baboy"
cost = 23647
back5 = f"the item is {item} and it will cost {cost} dollars"
print(back5)
