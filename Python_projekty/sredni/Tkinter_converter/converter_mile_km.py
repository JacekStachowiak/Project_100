from tkinter import *


def click_calculate():
    miles = float(miles_input.get())
    km = miles * 1.609
    kilometers = round(km, 2)
    km_result_label.config(text=f'{kilometers}')


window = Tk()
window.minsize(width=250, height=125)
window.title('Konwersja')
window.config(padx=20, pady=20)

miles_input = Entry(width=15)
miles_input.grid(column=1, row=0)
miles_input.get()

miles_label = Label(text='Miles')
miles_label.grid(column=2, row=0)
miles_label.config(padx=5, pady=5)

is_equal_label = Label(text='is equal')
is_equal_label.grid(column=0, row=1)
is_equal_label.config(padx=5, pady=5)

km_result_label = Label(text=0)
km_result_label.grid(column=1, row=1)
km_result_label.config(padx=5, pady=5)

km_label = Label(text='km')
km_label.grid(column=2, row=1)
km_label.config(padx=5, pady=5)

calculate_button = Button(text='Calculate', command=click_calculate)
calculate_button.grid(column=1, row=2)
calculate_button.config(padx=5, pady=5)

window.mainloop()