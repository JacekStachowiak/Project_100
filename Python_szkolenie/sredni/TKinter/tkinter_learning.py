from tkinter import *


def button_clicked():
    print('Zostałem kliknięty')
    message = input.get()
    my_label.config(text=message)

window = Tk()
window.title('My GUI Program')
window.minsize(width=800, height=600)
window.config(padx=20, pady=20)

# etykieta
my_label = Label(text='I am label', font=('Arial', 16, 'bold')) # my_label.pack(side='bottom'), my_label.pack(expand=True), my_label.pack(side='left')
my_label['text'] = 'New text'
my_label.config(text='NEW TEXT')
# my_label.place(x=100, y=100)
my_label.grid(column=0, row=1)
my_label.config(pady=5, padx=5)

# buttons
button = Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=2)

button_2 = Button(text='Second button', command=button_clicked)
button_2.grid(column=2, row=2)

# Entry
input = Entry(width=40)
print(input.get())
#Add some text to begin with
input.insert(END, string="Some text to begin with.")
#Gets text in entry
print(input.get())
input.grid(column=2, row=6)


#Text
text = Text(height=5, width=30) # height --> liczba linii text-u
text.focus()    #Puts cursor in textbox.
text.insert(END, "Example of multi-line text entry.")   #Adds some text to begin with.
print(text.get("1.0", END))     #Get's current value in textbox at line 1, character 0
text.grid(column=3, row=1)

#Spinbox
def spinbox_used():
    print(spinbox.get())        #gets the current value in spinbox.
spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.grid(column=1, row=3)

#Scale
#Called with current scale value.
def scale_used(value):
    print(value)
scale = Scale(from_=0, to=100, command=scale_used)
scale.grid(column=2, row=3)

#Checkbutton
def checkbutton_used():
    #Prints 1 if On button checked, otherwise 0.
    print(checked_state.get())
#variable to hold on to checked state, 0 is off, 1 is on.
checked_state = IntVar()
checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.grid(column=3, row=3)

#Radiobutton
def radio_used():
    print(radio_state.get())
#Variable to hold on to which radio button value is checked.
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radiobutton1.grid(column=4, row=3)
radiobutton2.grid(column=4, row=4)

#Listbox
def listbox_used(event):
    # Gets current selection from listbox
    print(listbox.get(listbox.curselection()))

listbox = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana", 'inne', 'inne']
for item in fruits:
    listbox.insert(fruits.index(item), item)
listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.grid(column=0, row=5)


# pack --> uklada domyślnie od góry - left, right, bottom, expand
# place --> x i y - dobre dla kilku widżetów, dla większej ilości nie
# grid --> dzielimy okno na row-s i column's - nie mieszamy z innymi np. z pack-iem



window.mainloop()