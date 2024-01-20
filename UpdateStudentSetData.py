from tkinter import *
from tkinter import messagebox
import openpyxl
import UpdateStudentGetData


def back_on_click(root):
    UpdateStudentGetData.start_update_screen_get_data(root)


def validate_float(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False


def update_on_click(root,index,name,reg_no,original_reg_no,email,cgpa,reg_no_entry):
    if reg_no == original_reg_no:
        workbook = openpyxl.load_workbook('Student Data.xlsx')
        sheet = workbook.active

        sheet['A'+str(index)] = name
        sheet['C'+str(index)] = email
        sheet['D'+str(index)] = cgpa

        messagebox.showinfo('Success',f'Student Data has been Updated')
        workbook.save('Student Data.xlsx')
        back_on_click(root)
    else:
        messagebox.showerror('Error','Registration Number cannot be Changed')
        reg_no_entry.delete(0,END)
        reg_no_entry.insert(0,original_reg_no)


def start_update_screen_set_data(root,index,original_name,original_reg_no,original_email,original_cgpa):
    root.destroy()
    window = Tk()
    window.title("Student Management System-------> Update Student")

    window.config(background='Sky Blue')

    update_student_label = Label(window, text='Update Student',
                                 background='Sky Blue', font=('Times New Roman', 30, 'bold', 'underline'))
    update_student_label.pack(pady=50)

    name_label = Label(window, text='Student Name:', background='Sky Blue',
                       font=('Times New Roman', 15, 'bold'))
    name_label.place(x=270, y=170)

    name_entry = Entry(window, bd=2, insertbackground="red", font=('Times New Roman', 15))
    name_entry.pack(pady=20)
    name_entry.insert(0,original_name)

    registration_no_label = Label(window, text='Student Registration No:', background='Sky Blue',
                                  font=('Times New Roman', 15, 'bold'))
    registration_no_label.place(x=187, y=240)

    registration_no_entry = Entry(window, bd=2, insertbackground="red",
                                  font=('Times New Roman', 15))
    registration_no_entry.pack(pady=20)
    registration_no_entry.insert(0,original_reg_no)

    email_label = Label(window, text='Student Email:', background='Sky Blue',
                        font=('Times New Roman', 15, 'bold'))
    email_label.place(x=270, y=305)

    email_entry = Entry(window, bd=2, insertbackground="red",
                        font=('Times New Roman', 15))
    email_entry.pack(pady=20)
    email_entry.insert(0,original_email)

    cgpa_label = Label(window, text='Student CGPA:', background='Sky Blue',
                       font=('Times New Roman', 15, 'bold'))
    cgpa_label.place(x=260, y=375)

    cgpa_entry = Entry(window, bd=2, insertbackground="red",
                       font=('Times New Roman', 15), validate="key",
                       validatecommand=(window.register(validate_float), '%P'))
    cgpa_entry.pack(pady=20)
    cgpa_entry.insert(0,original_cgpa)

    update = Button(window, text='Update',
                    font=('Times New Roman', 14, 'bold'), border=2,
                    command=lambda: update_on_click(window,index,name_entry.get(),
                                                    registration_no_entry.get(),
                                                    original_reg_no,
                                                    email_entry.get(),
                                                    cgpa_entry.get(),registration_no_entry),
                    activebackground='Light Green', compound='bottom')
    update.pack(pady=40)

    back = Button(window, text='Back',
                  font=('Times New Roman', 14, 'bold'), border=2,
                  command=lambda: back_on_click(window),
                  activebackground='Light Green', compound='bottom')
    back.place(x=10, y=10)

    window.state('zoomed')
    window.mainloop()