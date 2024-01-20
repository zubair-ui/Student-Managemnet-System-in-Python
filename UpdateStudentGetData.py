from tkinter import *
from tkinter import messagebox
import openpyxl

import UpdateStudentSetData
import welcome


def back_on_click(root):
    welcome.back_to_main_screen(root)


def validate_registration_input(new_value):
    return new_value.isdigit() or new_value == ""


def get_data_on_click(root,registration_no):
    workbook = openpyxl.load_workbook('Student Data.xlsx')
    sheet = workbook.active

    registration_data = [cell.value for cell in sheet['B']]

    if registration_no not in registration_data:
        messagebox.showerror('Error','Student Does Not Exist')
    else:
        index = str(registration_data.index(registration_no)+1)
        name = sheet['A'+index].value
        email = sheet['C'+index].value
        cgpa = sheet['D'+index].value
        UpdateStudentSetData.start_update_screen_set_data(root,index,name,registration_no,email,cgpa)


def start_update_screen_get_data(root):
    root.destroy()
    window = Tk()
    window.title("Student Management System-------> Update Student")

    window.config(background='Sky Blue')

    update_student_label = Label(window, text='Update Student',
                                 background='Sky Blue', font=('Times New Roman', 30, 'bold', 'underline'))
    update_student_label.pack(pady=50)

    registration_no_label = Label(window, text='Student Registration No:', background='Sky Blue',
                                  font=('Times New Roman', 15, 'bold'))
    registration_no_label.place(x=187, y=170)

    registration_no_entry = Entry(window, bd=2, insertbackground="red",
                                  font=('Times New Roman', 15), validate='key',
                                  validatecommand=(window.register(validate_registration_input), '%P'))
    registration_no_entry.pack(pady=20)

    get_data_button = Button(window, text='Get Data',
                           font=('Times New Roman', 14, 'bold'), border=2,
                           command=lambda: get_data_on_click(window,registration_no_entry.get()),
                           activebackground='Light Green', compound='bottom')
    get_data_button.pack(pady=40)

    back = Button(window, text='Back',
                  font=('Times New Roman', 14, 'bold'), border=2,
                  command=lambda: back_on_click(window),
                  activebackground='Light Green', compound='bottom')
    back.place(x=10, y=10)

    window.state('zoomed')
    window.mainloop()