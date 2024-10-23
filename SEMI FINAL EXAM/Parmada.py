print("=================================")
print("       -Record Keeping App-      ")
print("=================================")
print("Available operators")
print("A) Add Data")
print("B) Delete Data")
print("C) End")
print()
selection = str(input("Select an option[A. Add Data, B. Delete Data, C. End]: "))

try:
    file = open("data.text", "a")
except FileNotFoundError:
    file = open("data.text", "x")
    
if selection.upper() == "A":
    var1 = str(input("Enter Key: "))
    var2 = str(input("Enter Value: "))
    file = open("data.text", "a")   
print("== Store Information")
print("In Dictionary ==")

key = ["Lastname"]
value = ["Doe"]

info_dict = dict(zip(key, value))
print(info_dict)
file.close()
   
if selection.upper() == "B":
    var1 = str(input("Enter Key: "))
    file = open("data.text", "a")
print("== Delete Data")
print("From The Dictionary ==")

key = ["Lastname"]
value = ["Doe"]

info_dict = {"Lastname":"Doe" }

del info_dict["Lastname"]
print(info_dict)
file.close()
    
if selection.upper() == "C":
    print("THANK YOU")
