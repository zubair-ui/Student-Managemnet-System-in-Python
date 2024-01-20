from tkinter import *
from tkinter import messagebox
import openpyxl
import welcome


def validate_registration_input(new_value):
    return new_value.isdigit() or new_value == ""


def back_on_click(root):
    welcome.back_to_main_screen(root)


def delete_on_click(registration_no):
    workbook = openpyxl.load_workbook('Student Data.xlsx')
    sheet = workbook.active

    registration_data = [cell.value for cell in sheet['B']]

    if registration_no not in registration_data:
        messagebox.showerror('Error','Student Does Not Exist')
    else:
        student_name_to_delete = sheet['A' + str(registration_data.index(registration_no) + 1)].value
        response = messagebox.askyesno('IMPORTANT',f'Are you sure you want to remove {student_name_to_delete}?')
        if response:
            sheet.delete_rows(registration_data.index(registration_no)+1)
            workbook.save('Student Data.xlsx')
            messagebox.showinfo('Success',f'Student {student_name_to_delete} Has Been Deleted Successfully')


def start_delete_screen(root):
    root.destroy()
    window = Tk()
    window.title("Student Management System-------> Remove Student")

    window.config(background='Sky Blue')

    remove_student_label = Label(window, text='Remove Student',
                              background='Sky Blue', font=('Times New Roman', 30, 'bold', 'underline'))
    remove_student_label.pack(pady=50)

    registration_no_label = Label(window, text='Student Registration No:', background='Sky Blue',
                                  font=('Times New Roman', 15, 'bold'))
    registration_no_label.place(x=187, y=170)

    registration_no_entry = Entry(window, bd=2, insertbackground="red",
                                  font=('Times New Roman', 15), validate='key',
                                  validatecommand=(window.register(validate_registration_input), '%P'))
    registration_no_entry.pack(pady=20)

    delete_button = Button(window,text='Remove',
             font=('Times New Roman',14,'bold'),border=2,
            command=lambda:delete_on_click(registration_no_entry.get()) ,
             activebackground='Light Green',compound='bottom')
    delete_button.pack(pady=40)

    back = Button(window, text='Back',
                  font=('Times New Roman', 14, 'bold'), border=2,
                  command=lambda: back_on_click(window),
                  activebackground='Light Green', compound='bottom')
    back.place(x=10, y=10)

    window.state('zoomed')
    window.mainloop()

