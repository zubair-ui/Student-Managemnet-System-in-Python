from tkinter import *
import welcome
import openpyxl

def back_on_click(root):
    welcome.back_to_main_screen(root)


def start_view_screen(root):
    root.destroy()
    window = Tk()
    window.title("Student Management System-------> View Student")

    window.config(background='Sky Blue')

    workbook = openpyxl.load_workbook('Student Data.xlsx')
    sheet = workbook.active

    student_data = []

    i = 2
    while True:
        is_cell_empty = sheet['A' + str(i)].value is None or sheet['A' + str(i)].value == ''
        if is_cell_empty:
            break
        student_data.append([sheet['A' + str(i)].value,
                             sheet['B' + str(i)].value,
                             sheet['C' + str(i)].value,
                            sheet['D' + str(i)].value])
        i += 1

    print(student_data)

    name_text = '\nName\t\t\t\n\n'
    registration_number_text = '\nRegistration Number\t\n\n'
    email_text = '\nEmail Address\t\t\n\n'
    cgpa_text = '\nCGPA\t\n\n'

    for student in student_data:
        name_text += student[0] + '\n'
        registration_number_text += student[1] + '\n'
        email_text += student[2] + '\n'
        cgpa_text += student[3] + '\n'

    name = Message(window, text=name_text,font=('Times New Roman', 15, 'bold'))
    name.place(x=120,y=130)

    registration_number = Message(window, text=registration_number_text, font=('Times New Roman', 15, 'bold'))
    registration_number.place(x=300, y=130)

    email = Message(window, text=email_text, font=('Times New Roman', 15, 'bold'))
    email.place(x=520, y=130)

    cgpa = Message(window, text=cgpa_text, font=('Times New Roman', 15, 'bold'))
    cgpa.place(x=740, y=130)

    back = Button(window, text='Back',
                  font=('Times New Roman', 14, 'bold'), border=2,
                  command=lambda: back_on_click(window),
                  activebackground='Light Green', compound='bottom')
    back.place(x=10, y=10)

    window.state('zoomed')
    window.mainloop()

