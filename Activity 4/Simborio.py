sampleText1 = "My name {}. i love {}. and playing. {}"
sampleText1a = sampleText1.format("thomas", "sheken joy", "guitar")
print(sampleText1a)

sampleText2 = "My name is {1} i love {0} and playing {2}"
sampleText2a = sampleText2.format("sheken joy", "thomas", "guitar")
print(sampleText2a)

iring = "My name is {name}, and i love eating {food} and I also love to play {playing}"
saging = iring.format(food="sheken joy", playing="guitar", name="thomas")
print(saging)

item = "sinugbang bulinaw"
cost = 50
cat2 = "The product is %s the cost is %.5f." % (item, cost)
print(cat2)

item = "tinolang ilaga"
cost = 800
back5 = f"the item is {item} and it will cost {cost} pesos dollars yen won"
print(back5)
