favorite_food = input("What is your favorite food? ")
favorite_drink = input("What is your favorite drink? ")
print(f"My favorite food is {favorite_food} and my favorite drink is {favorite_drink}.")

products = ["Laptop", "Phone", "Tablet"]
prices = [1200, 800, 450]
for i in range(len(products)):
    print("Product: {}, Price: ${}".format(products[i], prices[i]))

movie = input("Enter your favorite movie: ")
actor = input("Enter your favorite actor: ")
print("My favorite movie is " + movie + " and my favorite actor is " + actor + ".")

animal = input("Enter your favorite animal: ")
color = input("Enter your favorite color: ")
print("My favorite animal is a %s and my favorite color is %s." % (animal, color))
