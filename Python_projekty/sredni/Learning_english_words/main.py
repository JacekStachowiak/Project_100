from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
polish = {}


try:
    data = pd.read_csv('.\data\\words_to_learn.csv')
except FileNotFoundError:
    oryginal_data = pd.read_csv('.\data\polish_words_2.csv')
    polish = oryginal_data.to_dict(orient='records')
else:
    polish = data.to_dict(orient='records')  # tworzenie pary {french:english}

def data_word():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(polish)
    canvas.itemconfig(title_text, text='English', fill='black')
    canvas.itemconfig(word_text, text=current_card['English'], fill='black')
    canvas.itemconfig(card_front_image, image=card_front)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(title_text, text='Polish', fill='white')
    canvas.itemconfig(word_text, text=current_card['Polish'], fill='white')
    canvas.itemconfig(card_front_image, image=card_back)


def is_know():
    polish.remove(current_card)
    print(len(polish))
    data_learn = pd.DataFrame(polish)
    data_learn.to_csv('.\data\\words_to_learn.csv', index=False)
    data_word()


window = Tk()
window.title('Words')
window.config(padx=30 , pady=30, bg=BACKGROUND_COLOR, highlightthickness=0)

flip_timer = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
card_front = PhotoImage(file='.\images\\card_front.png')
card_back = PhotoImage(file='.\images\\card_back.png')

card_front_image = canvas.create_image(400, 263, image=card_front)

title_text = canvas.create_text(400, 150, text='', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='', font=('Ariel', 50, 'bold'))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

right_image = PhotoImage(file='.\images\\right.png')
button_right = Button(image=right_image , highlightthickness=0 , command=is_know)
button_right.grid(column=0, row=1)

wrong_image = PhotoImage(file='.\images\\wrong.png')
button_wrong = Button(image=wrong_image, highlightthickness=0, command=data_word)
button_wrong.grid(column=1, row=1)

data_word()

canvas.grid(column=0, row=0, columnspan=2)
window.mainloop()
