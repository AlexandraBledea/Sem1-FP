from tkinter import *
from tkinter import messagebox
from src.Domain.entity import Student, Discipline, Grade, StudentException, DisciplineException, GradeException


class ConsoleGUI:

    def __init__(self, student_service, discipline_service, grade_service):
        self.students_service = student_service
        self.discipline_service = discipline_service
        self.grade_service = grade_service
        self.frame = None
        self.tk = Tk()

    def start(self):
        self.tk.title("Graphic user interface for Hogwarts school!")

        frame1 = Frame(self.tk)
        frame1.pack()
        self.frame = frame1

        label = Label(self.frame, text='Student ID:')
        label.pack(side=LEFT)

        self.id_student_to_fill = Entry(self.frame, {})
        self.id_student_to_fill.pack(side=LEFT)

        label = Label(self.frame, text='Student name:')
        label.pack(side=LEFT)

        self.name_student_to_fill = Entry(self.frame, {})
        self.name_student_to_fill.pack(side=LEFT)

        self.add_student_button = Button(self.frame, text='Add student', command=self.add_student)
        self.add_student_button.pack(side=LEFT)

        self.display_students_button = Button(self.frame, text='Display students', command=self.display_students)
        self.display_students_button.pack(side=LEFT)

        self.update_student_button = Button(self.frame, text='Update student', command=self.update_student)
        self.update_student_button.pack(side=LEFT)

        self.delete_student_button = Button(self.frame, text='Remove student', command=self.delete_student)
        self.delete_student_button.pack(side=LEFT)

        self.search_student_by_name_button = Button(self.frame, text='Search student by name',
                                                 command=self.search_student_by_name_gui)
        self.search_student_by_name_button.pack(side=LEFT)

        self.search_student_by_id_button = Button(self.frame, text='Search student by id',
                                               command=self.search_student_by_id_gui)
        self.search_student_by_id_button.pack(side=LEFT)

        frame2 = Frame(self.tk)
        frame2.pack()
        self.frame = frame2

        label = Label(self.frame, text='Discipline id:')
        label.pack(side=LEFT)

        self.id_discipline_to_fill = Entry(self.frame, {})
        self.id_discipline_to_fill.pack(side=LEFT)

        label = Label(self.frame, text='Discipline name:')
        label.pack(side=LEFT)

        self.name_discipline_to_fill = Entry(self.frame, {})
        self.name_student_to_fill.pack(side=LEFT)



        self.tk.mainloop()

    def add_student(self):
        """
        With this function we read the input given by the user and add a new student
        :return: It doesn't return anything
        """
        try:
            self.students_service.append_student_to_list(Student(self.id_student_to_fill.get(),
                                                                 self.name_student_to_fill.get()))
            messagebox.showinfo('Updated!', 'Student added!')
        except StudentException as se:
            messagebox.showinfo('Error', 'Error adding a student - ' + str(se))

    def display_students(self):
        """
        With this function we display the students
        :return: It doesn't return anything
        """
        student_list = ""
        for i in range(0, len(self.students_service.students)):
            student_list += 'Student id:  ' + str(self.students_service.students[i].student_id).rjust(7)\
                            + '  Student name:  ' + str(self.students_service.students[i].student_name).rjust(15)
            student_list += '\n'
        messagebox.showinfo("List of students", student_list)

    def update_student(self):
        """
        With this function we update the name of a specified student
        :return: it doesn't return anything
        """
        try:
            self.students_service.update_student_name(self.id_student_to_fill.get(), self.name_student_to_fill.get())
            messagebox.showinfo('Updated!', "The name of the student was updated!")
        except StudentException as se:
            messagebox.showinfo('Error!', "Error updating student's name - " + str(se))

    def delete_student(self):
        """
        With this function we delete a student and all the grades related to it
        :return: it doesn't return anything
        """
        try:
            self.students_service.remove_student_from_list(self.id_student_to_fill.get())
            self.grade_service.remove_grade_from_list_with_student_id(self.id_student_to_fill.get())
            messagebox.showinfo('Updated!', 'The student was deleted!')
        except StudentException as se:
            messagebox.showinfo('Error!', "Error deleting the student - " + str(se))

    def search_student_by_name_gui(self):
        """
        With this function we search for students by a specified name
        :return: it doesn't return anything
        """
        try:
            ids_list = self.students_service.search_student_by_name(self.name_student_to_fill.get())
            student_list = ""
            for student in self.students_service.students.student_list:
                for i in range(0, len(ids_list)):
                    if student.student_id == ids_list[i]:
                        student_list += 'Student id:  ' + str(student.student_id).rjust(7) \
                                        + '  Student name:  ' + str(student.student_name).rjust(15)
                        student_list += '\n'
            messagebox.showinfo("List of students", student_list)

        except StudentException as se:
            messagebox.showinfo("Error!", "Error searching for the students - " + str(se))

    def search_student_by_id_gui(self):
        """
        With this function we search for students by a specified id
        :return: it doesn't return anything
        """
        try:
            ids_list = self.students_service.search_student_by_id(self.id_student_to_fill.get())
            student_list = ""
            for student in self.students_service.students.student_list:
                for i in range(0, len(ids_list)):
                    if student.student_id == ids_list[i]:
                        student_list += 'Student id:  ' + str(student.student_id).rjust(7) \
                                        + '  Student name:  ' + str(student.student_name).rjust(15)
                        student_list += '\n'
            messagebox.showinfo("List of students", student_list)
        except StudentException as se:
            messagebox.showinfo("Error!", "Error searching for the students - " + str(se))

    def add_discipline(self):
        """
        With this function we read the input given by the user and add a new discipline
        :return: it doesn't return anything
        """
        try:
            self.discipline_service.append_discipline_to_list(self.id_discipline_to_fill.get(),
                                                                         self.name_discipline_to_fill.get())
            messagebox.showinfo("Updated!", "Discipline added!")
        except DisciplineException as de:
            messagebox.showinfo("Error!", "Error adding a discipline - " + str(de))

