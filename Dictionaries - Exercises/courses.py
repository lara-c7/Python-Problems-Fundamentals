courses_book = {}

command = input()
while command != 'end':
    course_name, student_name = command.split(' : ')
    if course_name not in courses_book.keys():
        courses_book[course_name] = []
    courses_book[course_name].append(student_name)
    command = input()

for course, names in courses_book.items():
    print(f'{course}: {len(names)}')
    for name in names:
        print(f'-- {name}')
