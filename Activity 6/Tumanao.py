name_input = input("ENTER YOUR NAME: ")
address_input = input("ENTER YOUR ADDRESS: ")
fav_flower = input("ENTER YOUR FAVORITE FLOWER: ")


print (f"Hi, my name is {name_input}, i'am {address_input} years of age as a student and my favorite flower is {fav_flower}.")


# Part 2

brandName1 = input("ENTER FAVORITE BRAND: ")
brandName2 = input("ENTER LEAST FAVORITE BRAND: ")


message = "My favorite brand is {} and least favorite is {}." .format(brandName1, brandName2)
print (message)


# Part 3

country = "Spain"
weatherCelcious = 20
weatherFahrenheit = 85.2


print(f"Weather in the %s is %d degrees in celcious and %.1f in fahrenheit." % (country, weatherCelsious, weatherFahrenheit))
