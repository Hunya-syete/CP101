# Part 1: Basic f-string Formatting
name = input("Enter your name: ")
age = int(input("Enter your age: "))
print(f"Hello, my name is {name} and I am {age} years old.")

# Part 2: Using .format()
students = ["Dave", "Inding", "David"]
grades = [85, 90, 78]
for i in range(len(students)):
    print("Student: {}, Grade: {}".format(students[i], grades[i]))

# Part 3: Using String Concatenation
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
print("Hello, my name is " + first_name + " " + last_name + ".")

# Part 4: Using String Interpolation
city = input("Enter your city: ")
country = input("Enter your country: ")
print("I am from %s, %s." % (city, country))
