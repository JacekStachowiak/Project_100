from question_model import Question
from data import question_data
from quiz_brain import QuizBrain


question_bank = []

for x in question_data:
    x_text = x['question']
    x_answer = x['correct_answer']
    new_question = Question(x_text, x_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)


while quiz.still_has_question():    # is True
    quiz.next_question()

print('You have completed the quiz')
print(f'Your final score was: {quiz.score}/{quiz.question_number}')




