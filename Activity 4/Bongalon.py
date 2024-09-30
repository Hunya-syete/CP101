sampleText1 = "My name is {}. I love {}. and I hate {} the most."
sampleText1a = sampleText1.format("Law", "manga comix", "Math subjects")
print(sampleText1a)

sample2 = "My name is {2} I love {1} and I hate {0} the most."
sample2a = sample2.format("Math subject", "Manga comix", "Law")
print(sample2a)

Text3 = "My name is {name}, and I love reading {comix} and my enemy is to solve {subject}"
Text3a = Text3.format(comix ="Manga", subject ="Math", name ="Law")
print(Text3a)

item = "book"
cost = 340.1
Text4 = "The product is %s the cost is %.5f." % (item, cost)
print(Text4)

item = " Novelbook1"
cost = 5800
Sample5 = f"the item is {item} that cost {cost} pesos"
print(Sample5)
