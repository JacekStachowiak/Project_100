from tkinter import *
from tkinter import messagebox
from generator_pass import gen_pass
import json


window = Tk()
window.title('Password Manager')
window.config(padx=20, pady=20)


def generator():
    enter_password.insert(END, gen_pass())


def save():
    website = enter_website.get()
    email = enter_email.get()
    password = enter_password.get()
    new_data = {
        website: {
            'email': email,
            'password': password
        }
    }

    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Oops', message='Pole website lub password nie może byc puste')
    else:
        try:
            with open('data.json', 'r') as data_file:
                data = json.load(data_file)
        except FileNotFoundError:
            print('Brak pliku --> tworzę nowy plik')
            with open('data.json', 'w') as data_file:
                json.dump(new_data, data_file, indent=4)
        else:
            data.update(new_data)
            with open('data.json', 'w') as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            enter_website.delete(0, END)
            enter_password.delete(0, END)

def find_password():
    web_text = enter_website.get().title()
    try:
        with open('data.json', 'r') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=Error, message='Nie znaleziono pliku' )
    else:
        if web_text in data:
            email = data[web_text]["email"]
            password = data[web_text]["password"]
            messagebox.showinfo(title='Web', message=f'Twoje dane dla {web_text}:\nemail: {email}\npassword: {password}')
        else:
            messagebox.showinfo(title='Error', message='Nie znaleziono stronki')


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


enter_website = Entry(width=36)
enter_website.grid(column=1, row=1, columnspan=2)
enter_website.focus()


enter_email = Entry(width=56)
enter_email.grid(column=1, row=2, columnspan=3)
enter_email.insert(END, 'jacek_stachowiak57@gmail.com')


enter_password = Entry(width=36)
enter_password.grid(column=1, row=3)


button_gen = Button(text='Generate password', font=('Arial', 8,'bold'), bg='yellow', command=generator)
button_gen.grid(column=3, row=3)

add_button = Button(text='Add', width=47, font=('Arial', 8,'bold'), bg='blue', fg='white', command=save)
add_button.grid(column=1, row=5, columnspan=3)

search_button = Button(text='Search', width=15, font=('Arial', 8, 'bold'), bg='green', fg='white', command=find_password)
search_button.grid(column=3, row=1)



window.mainloop()