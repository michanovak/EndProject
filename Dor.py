from tkinter import *
from tkinter.ttk import Combobox

def submit():
    user_firstname = user_firstname_text_box.get()
    user_lastname = user_lastname_text_box.get()
    user_email = user_email_text_box.get()
    user_gender = user_gender_combobox.get()
    user_id = user_id_text_box.get()
    user_pass = user_pass_text_box.get()
 #   label1 = Label(root, text=user_firstname, user_lastname, user_email, user_gender, user_id, user_pass)
    label1.pack()


root = Tk()
root.title("Average Speed Checker")
root.geometry("450x165")

user_firstname_label = Label(root, text="First Name:")
user_firstname_label.pack()

user_firstname_text_box = Entry(root, bd=1)
user_firstname_text_box.pack()

user_lastname_label = Label(root, text="Last Name:")
user_lastname_label.pack()

user_lastname_text_box = Entry(root, bd=1)
user_lastname_text_box.pack()

user_email_label = Label(root, text="Email:")
user_email_label.pack()

user_email_text_box = Entry(root, bd=1)
user_email_text_box.pack()

user_gender_label = Label(root, text="Gender:")
user_gender_label.pack()

user_gender_combo = Combobox(root)
user_gender_combo['values'] = ('Male','Female')
user_gender_combo.pack()

user_id_label = Label(root, text="User ID:")
user_id_label.pack()

user_id_text_box = Entry(root, bd=1)
user_id_text_box.pack()

user_pass_label = Label(root, text="User Password:")
user_pass_label.pack()

user_pass_text_box = Entry(root, bd=1)
user_pass_text_box.pack()

enter_button = Button(root, text="Enter", command=submit)
enter_button.pack()

root.mainloop()