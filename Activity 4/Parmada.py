# Using a String Placeholders

#1
faith1 = "Hi! My name is {}. I love {}. I love playing {}. {}"
faith1a = faith1.format("Mae Faith", "Wattpad", "Mobile Legends", "Plants vs. Zombies")
print(faith1a)



#2 
faith2 = "My name is {2}. I love {1}. I love playing {0}."
faith2a = faith2.format("Plants vs. Zombies", "Wattpad", "Mae Faith", "Mobile Legends")
print(faith2a)



#3
faith3 = "My name is {name}. I love {food}. I love playing {game}."
faith3a = faith3.format(food="siomai", name="Mae Faith", game="Plants vs. Zombies")
print(faith3a)




#4
item = "water"
cost = 25.90
faith4 = "The product is %s the cost is %.90f." % (item, cost)
print(faith4) 

#5
item = "liptint"
cost = 150

faith5 = f"The item is {item} and the cost is {cost * 100} pesos."
print(faith5)  
