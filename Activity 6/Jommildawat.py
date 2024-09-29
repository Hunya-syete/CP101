name_input = input("ENTER YOUR NAME: ")
age_input = input("ENTER YOUR AGE: ")
fav_food = input("ENTER YOUR FAVORITE FOOD: ")


print (f"Hi, my name is {name_input}, i'am {age_input} years of age as a student and my favorite food is {fav_food}.")


# Part 2: Using  .format()
brandName1 = input("ENTER FAVORITE BRAND: ")
brandName2 = input("ENTER LEAST FAVORITE BRAND: ")


message = "My favorite brand is {} and least favorite is {}." .format(brandName1, brandName2)
print (message)


# Part 3: Legacy % formatting.
country = "Korea"
weatherCelcious = 20
weatherFahrenheit = 85.2


print ("Weather in the %s is %d degrees in celcious and %.1f in fahrenheit." % (country, weatherCelsious, weatherFahrenheit))
