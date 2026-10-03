students = [
    {"name": "Alice", "grades": [5, 4, 5, 3]},
    {"name": "Bob", "grades": [4, 4, 4, 5]},
    {"name": "Charlie", "grades": [5, 5, 5, 5]},
]
names = []
averages = []

print(*students, end="\n\n")

for student in students:
    name, grades = student["name"], student["grades"]
    average_grade = sum(grades) / len(grades)

    names.append(name)
    averages.append(average_grade)

students_averages = {names[i]: averages[i] for i in range(len(names))}

print(students_averages, end="\n\n")
print("Самый лучший средний балл:", max(students_averages.items(), key=lambda x: x[1]))
