subjects = {
    "Math": float(input(" Math grade: ")),
    "Science": float(input(" Science grade: ")),
    "English": float(input(" English grade: "))
}
average = sum(subjects.values()) / len(subjects)

print("The average grade is: ", average)
