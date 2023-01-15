# zadanie --> program do oceniania

students_score = {
    'Harry': 81,
    'Ron': 78,
    'Hermione': 99,
    'Draco': 74,
    'Neville': 62
}

# konwersja 91-100:wybitny, 81-90:przekracza wymagania, 71-80:akceptowalne, poniżej 70:niedostatecznie

student_grades = {}

for student in students_score:
    score = students_score[student]
    if score >= 91 and score <= 100:
        student_grades[student] = 'wybitny'
    elif score >= 81 and score <= 90:
        student_grades[student] = 'przekracza wymagania'
    elif score >= 71 and score <= 80:
        student_grades[student] = 'akceptowalna'
    elif score < 70:
        student_grades[student] = 'niedostatecznie'


print(student_grades)


