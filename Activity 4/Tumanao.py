jam01 = "My name is {}. I love {}. I love  {}. {}."
jam01a = sampleText1.format("Jamaica", "Sleeping", "Eating", "Kdrama")
print(jam01a)

jam02 = "My name is {1}. I love {2}. My favorate flower {0}."
jam02a = sampleText2.format("Rose", "Jamaica", "Traveling" )
print(jam02a)

jam03 = "My name is {name}. I love {food}. I love playing {play}."
jam03a = sampleText3.format(food="Halang²", play="With my sis and bro", name="Jamaica")
print(jam03a)

item = "cake"
cost = 160.9 
SampleText4 = "The product is %s the cost is %.5f." % (item, cost)
print(SampleText4) 

item = "samsung s24"
cost = 200000
SampleText5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(SampleText5)
