from tkinter import *
import random
import tkinter.messagebox
window = Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def passwordGenerator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list += random.choice(symbols)

    for char in range(nr_numbers):
        password_list += random.choice(numbers)

    random.shuffle(password_list)
    password = ""
    for char in password_list:
        password += char
    entry3.delete(0, 'end')
    entry3.insert(0, password)
    window.clipboard_clear()
    window.clipboard_append(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def savePassword():
    website = entry1.get()
    email = entry2.get()
    password = entry3.get()
    if website == "" or email == "" or password == "":
        tkinter.messagebox.showinfo("Error", "Don't leave any of the field empty.")
    else:
        ask = tkinter.messagebox.askokcancel("Added items", f"website: {website}\nemail: {email}\npassword: {password}")
        if ask:
            file = open("database.TXT", "a")
            file.write(f"{website} | {email} | {password}\n")
        entry1.delete(0, 'end')
        entry2.delete(0, 'end')
        entry3.delete(0, 'end')
        entry2.insert(0, "ranjananubhav7@gmail.com")
# ---------------------------- UI SETUP ------------------------------- #


window.title("Password manager")
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
label1 = Label(text="Website:")
label2 = Label(text="Email/Username:")
label3 = Label(text="Password:")
button1 = Button(text="Generate Password", command=passwordGenerator)
button2 = Button(text="Add", width=36, command=savePassword)
entry1 = Entry(width=35)
entry1.focus()
entry2 = Entry(width=35)
entry2.insert(0, "ranjananubhav7@gmail.com")
entry3 = Entry(width=21)
label1.grid(row=1, column=0)
label2.grid(row=2, column=0)
label3.grid(row=3, column=0)
entry1.grid(row=1, column=1, columnspan=2)
entry2.grid(row=2, column=1, columnspan=2)
entry3.grid(row=3, column=1)
button1.grid(row=3, column=2)
button2.grid(row=4, column=1, columnspan=2)
canvas.grid(row=0, column=1)

window.mainloop()
