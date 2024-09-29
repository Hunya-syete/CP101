boxText1 = "My name {}. i love {}. and playing. {}"
boxText1a = boxText1.format("Carl", "sisig", "Call of Duty Mobile")
print(boxText1a)

sugarText2 = "My name is. {1} i love. {0} and playing. {2}"
sugarText2a = sugarText2.format("nuggets", "Oscar", "Scatter")
print(sugarText2a)

Summit3 = "My name is. {name}, and i love eating. {food} and I also love to play. {playing}"
Summit3a = Summit3.format(food="sheken joy", playing="guitar", name="Blu")
print(Summit3a)

item = "Lechon de mickey"
cost = 300
rat4 = "The food is %s the cost is %.5f." % (item, cost)
print(rat4)

item = "Fried de mickey"
cost = 800
prito5 = f"The item is {item} and it will cost {cost} pesos"
print(prito5)
