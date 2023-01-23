
import random

# new_dict = {new_key:new:value for item in list}
# new_dict = {new_key:new:value for (key, value) in dict.items()}
# new_dict = {new_key:new:value for (key, value) in dict.items() if test}

names = ['Alex', 'Jack', 'Dave', 'Dark', 'Iza', 'John', 'Ela']
students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)  # {'Alex': 75, 'Jack': 6, 'Dave': 47, 'Dark': 44, 'Iza': 67}

passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# dict = {'Alex': 75, 'Jack': 6, 'Dave': 47, 'Dark': 44, 'Iza': 67}
# score = {}
# for k, v in dict.items():
#     if v >= 60:
#         score[k] = v
# print(score)

# zadanie nr 1

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# words_list = sentence.split()
# print(words_list)
result = {word: len(word) for word in sentence.split()}
print(result)

# zadanie 2 --> konwersja z C na F

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}

# 1 C * 9/5 + 32

called_weather = {day: temp_c * 9/5 + 32 for day, temp_c in weather_c.items()}
print(called_weather)