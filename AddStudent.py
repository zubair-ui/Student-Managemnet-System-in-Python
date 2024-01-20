from tkinter import *
from tkinter import messagebox
import welcome
import openpyxl


def submit_on_click(name,reg_no,email,cgpa):

    workbook = openpyxl.load_workbook('Student Data.xlsx')
    sheet = workbook.active

    registration_data = [cell.value for cell in sheet['B']]

    if name == '' or reg_no == '' or email == '' or cgpa == '':
        messagebox.showerror('Error','fields cannot be empty')
    elif '@' not in email:
        messagebox.showerror('Error','Incorrect Email')
    elif reg_no in registration_data:
        messagebox.showerror('Error','Student with the same Registration Number Already Exists')
    else:
        enter_data_to_excel(name,reg_no,email,cgpa)
        messagebox.showinfo('Success',f'Student {name} has been Added')


def enter_data_to_excel(name,reg_no,email,cgpa):
    workbook = openpyxl.load_workbook('Student Data.xlsx')
    sheet = workbook.active
    i = 1
    while True:
        is_cell_empty = sheet['A' + str(i)].value is None or sheet['A' + str(i)].value == ''
        if is_cell_empty:
            sheet['A' + str(i)] = name
            sheet['B' + str(i)] = reg_no
            sheet['C' + str(i)] = email
            sheet['D' + str(i)] = cgpa
            workbook.save('Student Data.xlsx')
            break
        i += 1


def back_on_click(root):
    welcome.back_to_main_screen(root)


def validate_registration_input(new_value):
    return new_value.isdigit() or new_value == ""


def validate_float(new_value):
    if new_value == "":
        return True
    try:
        float(new_value)
        return True
    except ValueError:
        return False


def start_add_screen(root):
    root.destroy()
    window = Tk()
    window.title("Student Management System-------> Add Student")

    window.config(background='Sky Blue')

    # Add Student Label
    add_student_label = Label(window, text='Add Student',
                         background='Sky Blue', font=('Times New Roman', 30, 'bold', 'underline'))
    add_student_label .pack(pady=50)

    # Student Name
    name_label = Label(window, text='Student Name:',background='Sky Blue',
                       font=('Times New Roman', 15, 'bold'))
    name_label.place(x=270,y=170)

    name_entry = Entry(window,bd=2,insertbackground="red",font=('Times New Roman',15))
    name_entry.pack(pady=20)

    # Student Registration Number
    registration_no_label = Label(window, text='Student Registration No:', background='Sky Blue',
                       font=('Times New Roman', 15, 'bold'))
    registration_no_label.place(x=187, y=240)

    registration_no_entry = Entry(window, bd=2, insertbackground="red",
                                  font=('Times New Roman', 15),validate='key',
                                  validatecommand=(window.register(validate_registration_input), '%P'))
    registration_no_entry.pack(pady=20)

    # Student email
    email_label = Label(window, text='Student Email:', background='Sky Blue',
                       font=('Times New Roman', 15, 'bold'))
    email_label.place(x=270, y=305)

    email_entry = Entry(window, bd=2, insertbackground="red",
                        font=('Times New Roman', 15))
    email_entry.pack(pady=20)# valdiate email if email contains @ when add button is presses

    # Student CGPA
    cgpa_label = Label(window, text='Student CGPA:', background='Sky Blue',
                        font=('Times New Roman', 15, 'bold'))
    cgpa_label.place(x=260, y=375)

    cgpa_entry = Entry(window, bd=2, insertbackground="red",
                        font=('Times New Roman', 15),validate="key",
                       validatecommand=(window.register(validate_float), '%P'))
    cgpa_entry.pack(pady=20)

    # Submit Button
    submit = Button(window,text='Submit',
             font=('Times New Roman',14,'bold'),border=2,
            command=lambda:submit_on_click(name_entry.get(),registration_no_entry.get(),
                                           email_entry.get(),cgpa_entry.get()) ,
             activebackground='Light Green',compound='bottom')
    submit.pack(pady=40)

    # Back Button
    back = Button(window,text='Back',
             font=('Times New Roman',14,'bold'),border=2,
            command=lambda:back_on_click(window),
             activebackground='Light Green',compound='bottom')
    back.place(x=10,y=10)

    window.state('zoomed')
    window.mainloop()

