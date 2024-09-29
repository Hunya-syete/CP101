#1
item = "vitamins"
cost = 350

Shiela1 = "The product is %s the cost is %.5f" % (item, cost)
print(Shiela1)

print("\n")

#2
Shiela2 = "My name is {}, I am {} years old, I love the subject {}"

Shiela3 = Shiela2.format("Shiela", "18", "English")

print(Shiela3)

print("\n")

#3
Shiela4 = "My name is {0}, I am {1} years old, I love the subject {2} and also i love to play {3}"

Shiela4s = Shiela4.format("Shiela", "18", "English", "Badminton")

print(Shiela4s)

print("\n")


#4
Shiela5 = "My name is {name}, I love {food}, I am {age}. my favorite food is {food}, and my hobby is {hobby}"

Shiela5s = Shiela5.format(age="18", name="Shiela", food="adobo", hobby="music")

print(Shiela5s)

print("\n")


item  = "laptop"
cost = 25000

Shiela5 = f"The item is a {item} and the cost is {cost * 10} pesos."
print(Shiela5)
