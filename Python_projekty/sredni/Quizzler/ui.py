from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(bg=THEME_COLOR, padx=20, pady=20, highlightthickness=0)

        self.canvas = Canvas(width=300, height=250, bg='white', highlightthickness=0)

        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text='Text',
            fill=THEME_COLOR,
            font=('Arial', 20, 'italic')
        )


        self.true_image = PhotoImage(file='.\images\\true.png')
        self.button_true = Button(image=self.true_image, pady=10, padx=10, highlightthickness=0, command=self.true_button)
        self.button_true.grid(column=0, row=2)

        self.false_image = PhotoImage(file='.\images\\false.png')
        self.button_false = Button(image=self.false_image, padx=10, pady=10, highlightthickness=0, command=self.false_button)
        self.button_false.grid(column=1, row=2)

        self.score = Label(text='Score: 0', fg='white', bg=THEME_COLOR, font=('Ariel', 10, 'bold'))
        self.score.grid(column=1, row=0)

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.score.config(text=f'Score: {self.quiz.score} / {self.quiz.question_number}')
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text='Zakończyłeś quiz')
            self.button_false.config(state='disable')
            self.button_true.config(state='disable')

    def true_button(self):
        is_right = self.quiz.check_answer('True')
        self.feedback(is_right)

    def false_button(self):
        is_right = self.quiz.check_answer('False')
        self.feedback(is_right)

    def feedback(self, is_right):
        if is_right == True:
            self.canvas.config(self.canvas, bg='green')
        else:
            self.canvas.config(self.canvas , bg='red')

        self.window.after(1000, self.get_next_question)







