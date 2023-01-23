import tkinter

window = tkinter.Tk()
window.minsize(width=350, height=150)
window.title('Konwersja')

etykieta = tkinter.Label(text='Miles', font=('Arial', 14, 'bold'))
etykieta.grid(column=4, row=1)



window.mainloop()