sampleText1 = "My name is {}, I love {} and playing {}."
sampleText1a = sampleText1.format("Neil", "letchon", "online games")
print(sampleText1a)

sampleText2 = "My name is {2}, I love {0} and playing {1}."
sampleText2a = sampleText2.format("letchon", "Neil", "online games")
print(sampleText2a)

Sol3 = "My name is {name}, and I love eating {food} and I also love to play {sport}"
Sol3a = Sol3.format(food="letchon baboy", sport="online games", name="Neil")
print(Sol3a)

item = "Kalabasa"
cost = 35.5
Meow4 = "The product is %s the cost is %.5f" % (item, cost)
print(Meow4)

item = "Chicken Pastel"
cost = 25
Meow5 = f"The item is {item} and it will cost {cost} dollars."
print(Meow5)
