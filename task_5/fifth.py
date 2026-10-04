data = [
    {"student": "Alice", "subject": "Math", "grade": 5},
    {"student": "Bob", "subject": "Math", "grade": 4},
    {"student": "Alice", "subject": "History", "grade": 3},
    {"student": "Bob", "subject": "History", "grade": 5},
]
data_dict = {}

print(data, "\n")

for student in data:
    name, subject, grade = student["student"], student["subject"], student["grade"]

    if subject not in data_dict.keys():
        data_dict[subject] = {name: grade}
    else:
        data_dict[subject][name] = grade

print(data_dict)
