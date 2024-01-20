from tkinter import *
from tkinter import messagebox
import AddStudent
import DeleteStudent
import ViewStudent
import UpdateStudentGetData


def exit_on_click(root):
    response = messagebox.askyesno('Warning','Are you sure you want Exit?')
    if response:
        root.destroy()


def add_student_screen(root):
    AddStudent.start_add_screen(root)


def delete_student_screen(root):
    DeleteStudent.start_delete_screen(root)


def view_student_screen(root):
    ViewStudent.start_view_screen(root)


def update_student_screen(root):
    UpdateStudentGetData.start_update_screen_get_data(root)


def back_to_main_screen(root):
    root.destroy()
    start_main_screen()


def start_main_screen():
    window = Tk()
    window.title("Student Management System")

    icon = PhotoImage(file='icon.png')
    window.iconphoto(True, icon)

    window.config(background='Sky Blue')

    welcomeLabel = Label(window, text='Welcome to Student Management System',
                         background='Sky Blue', font=('Times New Roman', 25, 'bold', 'underline'))
    welcomeLabel.pack(pady=50)

    addIcon = PhotoImage(file='Add Student Icon.png')
    add = Button(window, text='   Add Student    ', command=lambda: add_student_screen(window),
                 font=('Times New Roman', 14, 'bold'), border=2,
                 activebackground='Light Green',
                 image=addIcon, compound='bottom')
    add.pack(pady=40)

    deleteIcon = PhotoImage(file='Delete Student Icon.png')
    delete = Button(window, text='Remove Student', command=lambda: delete_student_screen(window),
                    font=('Times New Roman', 14, 'bold'), border=2,
                    activebackground='Light Green',
                    image=deleteIcon, compound='bottom')
    delete.pack(pady=30)

    view_icon = PhotoImage(file='View Student Icon.png')
    view = Button(window, text='   View Student   ', command=lambda: view_student_screen(window),
                  font=('Times New Roman', 14, 'bold'), border=2,
                  activebackground='Light Green',
                  image=view_icon, compound='bottom')
    view.pack(pady=30)

    update_icon = PhotoImage(file='Update Student.png')
    update = Button(window, text='  Update Student  ', command=lambda: update_student_screen(window),
                  font=('Times New Roman', 14, 'bold'), border=2,
                  activebackground='Light Green',
                  image=update_icon, compound='bottom')
    update.pack(pady=30)

    exit = Button(window, text='Exit',
                  font=('Times New Roman', 14, 'bold'), border=2,
                  command=lambda: exit_on_click(window),
                  activebackground='Red', compound='bottom')
    exit.place(x=10, y=10)


    window.state('zoomed')
    window.mainloop()


if __name__ == '__main__':
    start_main_screen()
