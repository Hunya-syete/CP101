# ( == This is Part 1 of the 3 codes == )

# This declares the information fill up
enter = input("Fill up necessary information? (yes/no): ")
while True:
   name = input("Enter Full Name: ")
   age = input("Enter Age: ")
   hobby = input("Enter Favorite Hobby: ")

# The f-string will be implemented for format
   print(f"Hello! My name is {name}, I am currently {age}, and my favorite hobby is {hobby}.")

# check if the user wants additional input
   add_input = input("Do you want to add more input? (yes/no): ")
   if add_input == "yes":

# This is the addtional line of code if the additional input is needed
      feeling = input("Do you feel good today?: ")
      print(f"Hello! My name is {name}, I am currently {age}, and my favorite hobby is {hobby}. Do I feel good today? {feeling}")
      print("== Additional Inputs Added and Successfully Placed! ==")
      break
   if add_input == "no":
      print("== Inputs Successful! ==")
      break

# ( == This is Part 2 of the 3 codes ==)

# This provides the needed information
item = "iphone 16 Promax"
cost = '32.699'
quantity = "1"
deadline = "2 week"

# The .format() method will be implemented
sentence = "In about {}, I will buy {} of the reliable {} smartphones that will cost {}".format(deadline, quantity, item, cost)
print(sentence)

# ( == This is Part 3 of the 3 codes == )

# This provides the needed information
country = "Manila"
temperature = 42
temperature2 = 24

# The % operator will be implemented
print("In the country of the %s, the average heat index is %d degrees Celsius, and the temp at night is %d degrees Celsius" 
    % (country, temperature, temperature2))
