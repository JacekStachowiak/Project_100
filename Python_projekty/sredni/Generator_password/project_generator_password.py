from tkinter import *
from tkinter import messagebox
from generator import gen_pass



window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


def generator():
    enter_password.insert(END, gen_pass())


def save():
    website = enter_website.get()
    email = enter_email.get()
    password = enter_password.get()

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Pole website lub password nie może byc puste')
    else:
        msg = messagebox.askokcancel(title=website, message=f'Wprowadziłeś:\n--> website: {website}\n--> email: {email}\n--> password: {password}\nAkceptujesz?')

        if msg:
            with open('data_2.txt', 'a') as data:
                data.write(f'{website} | {email} | {password}\n')
                enter_website.delete(0, END)
                enter_password.delete(0, END)


canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

label_website = Label(text='Website:')
label_website.grid(column=0, row=1)
label_email = Label(text='Email/Username:')
label_email.grid(column=0, row=2)
label_password = Label(text='Password:')
label_password.grid(column=0, row=3)


enter_website = Entry(width=55)
enter_website.grid(column=1, row=1, columnspan=3)
enter_website.focus()


enter_email = Entry(width=55)
enter_email.grid(column=1, row=2, columnspan=3)
enter_email.insert(END, 'jacek_stachowiak57@gmail.com')


enter_password = Entry(width=36)
enter_password.grid(column=1, row=3)



button_gen = Button(text='Generate password', command=generator)
button_gen.grid(column=3, row=3)

add_button = Button(text='Add', width=47, command=save)
add_button.grid(column=1, row=5, columnspan=3)



window.mainloop()