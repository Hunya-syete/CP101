sampleText1 = "My name {}. i love {}. and playing. {}"
sampleText1a = sampleText1.format("Alan", "apple", "basketball")
print(sampleText1a)

sampleText2 = "My name is {1} i love {0} and playing {2}"
sampleText2a = sampleText2.format("dogs", "Alan", "basketball")
print(sampleText2a)

Meow3 = "My name is {name}, and i love eating {food} and I also love to play {sport}"
Meow3a = Meow3.format(food="bananas", sport="basketball", name="Alan")
print(Meow3a)

item = "sisig"
cost = 35.5
Dog4 = "The product is %s the cost is %.5f." % (item, cost)
print(Dog4)

item = "tinula"
cost = 23647
back5 = f"the item is {item} and it will cost {cost} dollars"
print(back5)
