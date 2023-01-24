from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔️"
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    window.after_cancel(timer)      # stop dla globalnej timer
    canvas.itemconfig(timer_text , text='00:00')
    title_label.config(text='TIMER')
    checkmark.config(text='')
    global reps
    reps = 0



# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60  # praca = 25 min
    short_break_sec = SHORT_BREAK_MIN * 60  # 1-7 przerw = po 5 min
    long_break_sec = LONG_BREAK_MIN * 60  # ósma przerwa = 20 min

    if reps % 8 == 0:
        count_down(long_break_sec)
        title_label.config(text='Long break', fg=RED, font=(FONT_NAME, 25, 'bold'))
    elif reps % 2 == 0:
        count_down(short_break_sec)
        title_label.config(text='Short break', fg=PINK, font=(FONT_NAME, 25, 'bold'))
    else:
        count_down(work_sec)
        title_label.config(text='Work', fg=GREEN, font=(FONT_NAME, 25, 'bold'))


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)  # zaokrąglamy na dół
    if count_min < 10:
        count_min = f'0{count_min}'
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f'0{count_sec}'


    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += CHECKMARK
        checkmark.config(text=marks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW, highlightthickness=0)  # ostatni --> usunięcie ramki

# płótno --> canvas
canvas = Canvas(width=200, height=224, bg=YELLOW)
tomato_img = PhotoImage(file='tomato.png')  # tutaj podajemy ścieżkę do pliku
canvas.create_image(102, 112, image=tomato_img)  # w oknie podajemy(x,y,image=, )połowa wartości środek obrazu

timer_text = canvas.create_text(102, 130, text='00:00', fill='white',
                                font=(FONT_NAME, 35, 'bold'))  # x,y,text, wypełnienie, font
canvas.grid(column=1, row=1)

# label
title_label = Label(text='TIMER', fg=GREEN, bg=YELLOW , highlightthickness=0, font=(FONT_NAME, 50, 'bold'))
title_label.grid(column=1, row=0)

start_button = Button(text='Start', command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text='Reset', command=reset_timer)
reset_button.grid(column=2, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

window.mainloop()
