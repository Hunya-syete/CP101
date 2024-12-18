describe = input("How do you describe yourself?: ")
characteristic = input("Describe yourself again: ")
name = input("What is your name?: ")
age = input("what is your age?: ")
# Use an f-string to format the output
print(f"Hello,the very {describe} and {characteristic} person in the world, {name}, You are {age} years old.")

friend = "rey"
time = 2 
place = "boulevard"
game = "basketball"
# Use the .format() method
sentence = "I saw my friend {} today, {}pm at the {}, playing {}. ".format(friend, time, place, game)
print(sentence)

 
band = "Enhypen"
member = 7
lover = "engene"
# Use the % operator
print("The famous band %s is a %d member group who loves %s. " % (band, member, lover))
