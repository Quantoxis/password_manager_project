import hashlib
import getpass
from tkinter import *
import tkinter as tk

#logic to run login
def login_click(event=NONE):
    print('login button has been pressed')
    username = user_entry.get()
    password = password_entry.get()
    print(username)
    print(password)

#logic to run keyfile loading
def keyfile_click(event=NONE):
    print('keyfile loading button has been pressed')

#logic to create a new account
def create_account_click(even=NONE):
    print('create new account')


#create window
window = tk.Tk()  #instantiate window
window.geometry("600x400") #set window size
window.title("vault") #give window a title
icon = PhotoImage(file='images/ar_logo.png')
window.iconphoto(True, icon)
window.config(background="#B81414") #set background colour




#create labels
#user_label = Label(window, text="username", font=('Tahoma', 12, 'bold'), relief=RAISED, bd=10, padx=5, pady=5) #add username label
#password_label = Label(window, text="password", font=('Tahoma', 12, 'bold'), relief=RAISED, bd=10, padx=5, pady=5) #add password label

#create style for labels
label_style = {
    "font": ("Tahoma", 14, "bold"),
    "relief": GROOVE,
    "bd": 3,
    "padx": 10,
    "pady": 5,
    "bg": "#FFFFFF",  
    "fg": "#B81414", 
}

#create style for buttons
button_style = {
    "font": ("Tahoma", 12, "bold"),
    "bg": "#FFFFFF",
    "fg": "#B81414",
    "activebackground": "#FFE5E5",
    "activeforeground": "#B81414",
    "bd": 3,
    "relief": RAISED,
    "padx": 10,
    "pady": 5,
}

#create style for text entry fields
entry_style = {
    "font": ("Tahoma", 12, "bold"),
    "bg": "#FFFFFF", 
    "fg": "#B81414",
    "insertbackground": "#B81414",#blinking cursor
    "relief": SUNKEN,
    "bd": 3,
    "width": 25,
}



user_label = Label(window, text="Username: ", **label_style)


password_label = Label(window, text="Password: ", **label_style)

#text entry
user_entry = Entry(window, **entry_style)
password_entry = Entry(window, **entry_style, show="*")

#create buttons
login_button = Button(text="login", **button_style) #add login button
#login_button = Button(text="login", font=('Tahoma', 12, 'bold'), relief=RAISED, bd=10, padx=5, pady=5) #add login button
login_button.config(command=login_click) #make login button work when clicked
window.bind('<Return>', login_click) #run login function when enter key is pressed
load_keyfile_button = Button(text="load key", **button_style)
load_keyfile_button.config(command=keyfile_click)
window.bind('<Control-k>', keyfile_click)
create_account_button = Button(text="create new account", **button_style)
create_account_button.config(command=create_account_click)
window.bind('<Control-n>', create_account_click)
    
#use a grid layout
user_label.grid(row=0, column=0, padx=20, pady=20, sticky=E)
user_entry.grid(row=0, column=1, padx=20, pady=20)

password_label.grid(row=1, column=0, padx=20, pady=20, sticky=E)
password_entry.grid(row=1, column=1, padx=20, pady=20)

load_keyfile_button.grid(row=2, column=0, columnspan=2, padx=20, pady=20)

#remember_login_checkbox.grid(row=3, column=0, columnspan=2, pady=30)
login_button.grid(row=3, column=0, columnspan=1, pady=30)
create_account_button.grid(row=3, column=1, columnspan=1, pady=30)






window.mainloop() #draw window and listen for events







