sample1= "My name is {}. I love {}. I love watching{}."
first = sample1.format("Erich C. Omaguing", "Enhypen", "Kdramas")
print(first)

sample2 = "My name is {1}. I am {0} years old. {2} is my bias in Enhypen." 
second = sample2.format("19", "Erich", "Jay")
print(second)

sample3 = "My name is {name}. I love {food}. I love playing {play}."
third = first.format(food="Pork sisig", play="Codm", name="Erichcute")
print(third)

item = "wireless headphones"
cost = 650.75
Sample4 = "The product is %s the cost is %.2f." % (item, cost)
print(Sample4) 
