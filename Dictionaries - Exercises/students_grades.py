students_number = int(input())
students_book = {}

for _ in range(students_number):
    name, grade = input().split()
    if name not in students_book.keys():
        students_book[name] = []
    students_book[name].append(float(grade))

for name, grades in students_book.items():
    formatted_grades = ' '.join(f"{grade:.2f}" for grade in grades)
    print(f"{name} -> {formatted_grades} (avg: {(sum(grades) / len(grades)):.2f})")
