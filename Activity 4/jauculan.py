sampleText1 = "My name {}. i love {}. and playing. {}"
sampleText1a = sampleText1.format("noe", "mango float", "pyat2")
print(sampleText1a)

sampleText2 = "My name is {1} i love {0} and playing {2}"
sampleText2a = sampleText2.format("mango float", "noe", "pyat2")
print(sampleText2a)

wiggie = "My name is {name}, and i love eating {food} and I also love to play {playing}"
oscar = wiggie.format(food="mango float", playing="pyat2", name="noe")
print(oscar)

item = "saging ni wiggie"
cost = 100
saging2 = "The product is %s the cost is %.5f." % (item, cost)
print(saging2)

item = "talong ni joshua"
cost = 240
back5 = f"the item is {item} and it will cost {cost} pesos dollars yen won"
print(back5)
