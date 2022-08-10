from tkinter import *
from tkinter import messagebox
from src.Domain.discipline import Discipline, DisciplineException
from src.Domain.grade import Grade, GradeException
from src.Domain.student import Student, StudentException
from src.Service.undo_service import UndoException
from PIL import ImageTk, Image


class ConsoleGUI:


    def __init__(self, student_service, discipline_service, grade_service, undo_service):
        self.students_service = student_service
        self.discipline_service = discipline_service
        self.grade_service = grade_service
        self.undo_service = undo_service
        self.frame = None
        self.tk = Tk()
        self.tk.geometry("2000x350")
        self.tk.config(bg='pink')

    def start(self):
        self.tk.title("Graphic user interface for Hogwarts school!")

        image2 = Image.open('C:\\Users\\Alexandra\\Desktop\\bk.jpg')
        image1 = ImageTk.PhotoImage(image2)

        frame1 = Frame(self.tk, bg='pink')
        frame1.pack()
        self.frame = frame1

        label = Label(self.frame, bg='pink', text='Student ID:')
        label.pack(side=LEFT, pady=20)

        self.id_student_to_fill = Entry(self.frame, {})
        self.id_student_to_fill.pack(side=LEFT, padx=5)

        label = Label(self.frame, bg='pink', text='Student name:')
        label.pack(side=LEFT)

        self.name_student_to_fill = Entry(self.frame, {})
        self.name_student_to_fill.pack(side=LEFT, padx=5)

        self.add_student_button = Button(self.frame, text='Add student', bg='#af5dc6', activebackground='#e1ace3',
                                         command=self.add_student)
        self.add_student_button.pack(side=LEFT, padx=5)

        self.display_students_button = Button(self.frame, text='Display students', bg='#af5dc6',
                                              activebackground='#e1ace3',command=self.display_students)
        self.display_students_button.pack(side=LEFT, padx=5)

        self.update_student_button = Button(self.frame, text="Update student's name", bg='#af5dc6',
                                            activebackground='#e1ace3', command=self.update_student_name)
        self.update_student_button.pack(side=LEFT, padx=5)

        self.delete_student_button = Button(self.frame, text='Remove student', bg='#af5dc6',
                                            activebackground='#e1ace3', command=self.delete_student)
        self.delete_student_button.pack(side=LEFT, padx=5)

        self.search_student_by_name_button = Button(self.frame, text='Search student by name', bg='#af5dc6',
                                                    activebackground='#e1ace3',
                                                    command=self.search_student_by_name_gui)
        self.search_student_by_name_button.pack(side=LEFT, padx=5)

        self.search_student_by_id_button = Button(self.frame, text='Search student by id', bg='#af5dc6',
                                                  activebackground='#e1ace3',
                                                  command=self.search_student_by_id_gui)
        self.search_student_by_id_button.pack(side=LEFT, padx=5)

        frame2 = Frame(self.tk, bg='pink')
        frame2.pack()
        self.frame = frame2

        label = Label(self.frame, bg='pink', text='Discipline ID:')
        label.pack(side=LEFT, pady=20)

        self.id_discipline_to_fill = Entry(self.frame, {})
        self.id_discipline_to_fill.pack(side=LEFT, padx=5)

        label = Label(self.frame, bg='pink', text='Discipline name:')
        label.pack(side=LEFT)

        self.name_discipline_to_fill = Entry(self.frame, {})
        self.name_discipline_to_fill.pack(side=LEFT, padx=5)

        self.add_discipline_button = Button(self.frame, text='Add discipline', bg='#af5dc6',
                                            activebackground='#e1ace3',
                                            command=self.add_discipline)
        self.add_discipline_button.pack(side=LEFT, padx=5)

        self.display_disciplines_button = Button(self.frame, text='Display disciplines', bg='#af5dc6',
                                                 activebackground='#e1ace3',
                                                 command=self.display_disciplines)
        self.display_disciplines_button.pack(side=LEFT, padx=5)

        self.delete_discipline_button = Button(self.frame, text='Remove discipline', bg='#af5dc6',
                                               activebackground='#e1ace3',
                                               command=self.delete_discipline)
        self.delete_discipline_button.pack(side=LEFT, padx=5)

        self.update_discipline_button = Button(self.frame, text="Update discipline's name", bg='#af5dc6',
                                               activebackground='#e1ace3',
                                               command=self.update_discipline_name)
        self.update_discipline_button.pack(side=LEFT, padx=5)

        self.search_discipline_by_name_button = Button(self.frame, text='Search discipline by name', bg='#af5dc6',
                                                       activebackground='#e1ace3',
                                                       command=self.search_discipline_by_name_gui)
        self.search_discipline_by_name_button.pack(side=LEFT, padx=5)

        self.search_discipline_by_id_button = Button(self.frame, text='Search discipline by id', bg='#af5dc6',
                                                     activebackground='#e1ace3',
                                                     command=self.search_discipline_by_id_gui)
        self.search_discipline_by_id_button.pack(side=LEFT, padx=5)

        frame3 = Frame(self.tk, bg='pink')
        frame3.pack()
        self.frame = frame3

        label = Label(self.frame, bg='pink', text='Discipline ID:')
        label.pack(side=LEFT, pady=20)

        self.id_discipline_grade_to_fill = Entry(self.frame, {})
        self.id_discipline_grade_to_fill.pack(side=LEFT, padx=5)

        label = Label(self.frame, bg='pink', text='Student ID:')
        label.pack(side=LEFT)

        self.id_student_grade_to_fill = Entry(self.frame, {})
        self.id_student_grade_to_fill.pack(side=LEFT, padx=5)

        label = Label(self.frame, bg='pink', text='Grade:')
        label.pack(side=LEFT)

        self.value_of_grade_to_fill = Entry(self.frame, {})
        self.value_of_grade_to_fill.pack(side=LEFT, padx=5)

        self.grade_a_student_button = Button(self.frame, text='Grade a student', bg='#af5dc6',
                                             activebackground='#e1ace3',
                                             command=self.grade_a_student_gui)
        self.grade_a_student_button.pack(side=LEFT, padx=5)

        self.display_grade_list_button = Button(self.frame, text='Display grades', bg='#af5dc6',
                                                activebackground='#e1ace3',
                                                command=self.display_grade_list_gui)
        self.display_grade_list_button.pack(side=LEFT, padx=5)

        self.display_students_by_average_button = Button(self.frame, text='Display the averages of all students',
                                                         bg='#af5dc6', activebackground='#e1ace3',
                                                         command=self.display_students_by_average_gui)
        self.display_students_by_average_button.pack(side=LEFT, padx=5)

        self.display_all_students_who_failed_button = Button(self.frame, text='Display the students who failed at '
                                                                              'one or more disciplines',
                                                             bg='#af5dc6', activebackground='#e1ace3',
                                                             command=self.display_all_students_who_failed_gui)
        self.display_all_students_who_failed_button.pack(side=LEFT, padx=5)

        self.display_students_by_general_average_button = Button(self.frame, text='Display the students by'
                                                                                  ' their general average',
                                                                 bg='#af5dc6', activebackground='#e1ace3',
                                                                 command=self.display_students_by_general_average_gui)
        self.display_students_by_general_average_button.pack(side=LEFT, padx=5)

        self.display_disciplines_by_general_average_button = Button(self.frame, text='Display the disciplines by'
                                                                                     ' their general average',
                                                                    bg='#af5dc6', activebackground='#e1ace3',
                                                                    command=self.
                                                                    display_disciplines_by_general_average_gui)
        self.display_disciplines_by_general_average_button.pack(side=LEFT, padx=5)

        frame4 = Frame(self.tk, bg='pink')
        frame4.pack()
        self.frame = frame4

        self.undo_button = Button(self.frame, text='UNDO', bg='#af5dc6', activebackground='#e1ace3',
                                  command=self.undo_gui)
        self.undo_button.pack(side=LEFT, padx=5)

        self.redo_button = Button(self.frame, text='REDO', bg='#af5dc6', activebackground='#e1ace3',
                                  command=self.redo_gui)
        self.redo_button.pack(side=LEFT, padx=5)

        frame5 = Frame(self.tk, bg='pink', pady=20)
        frame5.pack()
        self.frame = frame5

        self.menu_button = Button(self.frame, text='~~MENU~~', bg='#af5dc6', activebackground='#e1ace3',
                                  command=self.menu_gui)
        self.menu_button.pack(side=LEFT, padx=5)

        self.exit_button = Button(self.frame, text='~~EXIT~~', bg='#af5dc6', activebackground='#e1ace3',
                                  command=self.frame.quit)
        self.exit_button.pack(side=LEFT, padx=5)

        self.clear_button = Button(self.frame, text='CLEAR ALL FIELDS', bg='#af5dc6', activebackground='#e1ace3',
                                   command=self.clear_fields)
        self.clear_button.pack(side=LEFT, padx=5)

        self.tk.mainloop()

    def add_student(self):
        """
        With this function we read the input given by the user and add a new student
        :return: It doesn't return anything
        """
        try:
            self.students_service.append_student_to_list_with_record(Student(self.id_student_to_fill.get().strip(),
                                                                             self.name_student_to_fill.get().strip()))
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showinfo('Updated!', 'Student added!')
        except StudentException as se:
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showerror('Error', 'Error adding a student - ' + str(se))

    def display_students(self):
        """
        With this function we display the students
        :return: It doesn't return anything
        """
        self.students_service.sort_students_list()
        student_list = ""
        for i in range(0, len(self.students_service.students)):
            student_list += 'Student ID:  ' + str(self.students_service.students[i].student_id).rjust(7) \
                            + '  Student name:  ' + str(self.students_service.students[i].student_name).rjust(15)
            student_list += '\n\n'
        messagebox.showinfo("List of students", student_list)

    def update_student_name(self):
        """
        With this function we update the name of a specified student
        :return: it doesn't return anything
        """
        try:
            self.students_service.update_student_name_with_record(self.id_student_to_fill.get().strip(),
                                                                  self.name_student_to_fill.get().strip())
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showinfo('Updated!', "The name of the student was updated!")
        except StudentException as se:
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showerror('Error!', "Error updating student's name - " + str(se))

    def delete_student(self):
        """
        With this function we delete a student and all the grades related to it
        :return: it doesn't return anything
        """
        if len(self.name_student_to_fill.get()) == 0:
            try:
                self.students_service.remove_student_from_list_with_record(self.id_student_to_fill.get().strip(),
                                                                           self.grade_service)
                self.id_student_to_fill.delete(0, END)
                messagebox.showinfo('Updated!', 'The student was deleted!')
            except StudentException as se:
                self.id_student_to_fill.delete(0, END)
                messagebox.showerror('Error!', "Error deleting the student - " + str(se))
        else:
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showerror('Error!', 'The name field should be empty')

    def search_student_by_name_gui(self):
        """
        With this function we search for students by a specified name
        :return: it doesn't return anything
        """
        if len(self.id_student_to_fill.get()) == 0:
            try:
                ids_list = self.students_service.search_student_by_name(self.name_student_to_fill.get())
                self.name_student_to_fill.delete(0, END)
                student_list = ""
                for student in self.students_service.students.student_list:
                    for i in range(0, len(ids_list)):
                        if student.student_id == ids_list[i]:
                            student_list += 'Student ID:  ' + str(student.student_id).rjust(7) \
                                            + '  Student name:  ' + str(student.student_name).rjust(15)
                            student_list += '\n\n'
                messagebox.showinfo("List of students", student_list)

            except StudentException as se:
                self.name_student_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error searching for the students - " + str(se))
        else:
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showerror("Error!", "The ID field should be empty!")

    def search_student_by_id_gui(self):
        """
        With this function we search for students by a specified id
        :return: it doesn't return anything
        """
        if len(self.name_student_to_fill.get()) == 0:
            try:
                ids_list = self.students_service.search_student_by_id(self.id_student_to_fill.get())
                student_list = ""
                self.id_student_to_fill.delete(0, END)
                for student in self.students_service.students.student_list:
                    for i in range(0, len(ids_list)):
                        if student.student_id == ids_list[i]:
                            student_list += 'Student ID:  ' + str(student.student_id).rjust(7) \
                                            + '  Student name:  ' + str(student.student_name).rjust(15)
                            student_list += '\n\n'
                messagebox.showinfo("List of students", student_list)
            except StudentException as se:
                self.id_student_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error searching for the students - " + str(se))
        else:
            self.id_student_to_fill.delete(0, END)
            self.name_student_to_fill.delete(0, END)
            messagebox.showerror("Error!", "The name field should be empty!")

    def add_discipline(self):
        """
        With this function we read the input given by the user and add a new discipline
        :return: it doesn't return anything
        """
        try:
            self.discipline_service.append_discipline_to_list_with_record(
                Discipline(self.id_discipline_to_fill.get().strip(),
                           self.name_discipline_to_fill.get().strip()))
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showinfo("Updated!", "Discipline added!")
        except DisciplineException as de:
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showerror("Error!", "Error adding a discipline - " + str(de))

    def display_disciplines(self):
        """
        With this function we display the disciplines
        :return: it doesn't return anything
        """
        self.discipline_service.sort_disciplines_list()
        discipline_list = ""
        for i in range(0, len(self.discipline_service.disciplines)):
            discipline_list += 'Discipline ID:  ' + str(self.discipline_service.disciplines[i].discipline_id).rjust(9) \
                               + '  Discipline name:  ' + str(self.discipline_service.disciplines[i].discipline_name). \
                                   rjust(15)
            discipline_list += '\n\n'
        messagebox.showinfo("List of disciplines", discipline_list)

    def delete_discipline(self):
        """
        With this function we delete a discipline and all the grades related to it
        :return: It doesn't return anything
        """
        if len(self.name_discipline_to_fill.get()) == 0:
            try:
                self.discipline_service.remove_discipline_from_list_with_record(self.id_discipline_to_fill.get().strip(),
                                                                                self.grade_service)
                self.id_discipline_to_fill.delete(0, END)
                messagebox.showinfo('Updated!', 'The discipline was deleted!')
            except DisciplineException as de:
                messagebox.showerror('Error!', "Error deleting the discipline - " + str(de))
                self.id_discipline_to_fill.delete(0, END)
        else:
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showerror("Error!", "The name field should be empty!")

    def update_discipline_name(self):
        """
        With this function we update the name of a specified discipline
        :return: it doesn't return anything
        """
        try:
            self.discipline_service.update_name_discipline_with_record(self.id_discipline_to_fill.get().strip(),
                                                                       self.name_discipline_to_fill.get().strip())
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showinfo('Updated!', 'The name of the discipline was updated!')
        except DisciplineException as de:
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showerror('Error!', "Error updating discipline's name - " + str(de))

    def search_discipline_by_name_gui(self):
        """
        With this function we search for disciplines by a specified name
        :return: it doesn't return anything
        """
        if len(self.id_discipline_to_fill.get()) == 0:
            try:
                ids_list = self.discipline_service.search_discipline_by_name(self.name_discipline_to_fill.get())
                self.name_discipline_to_fill.delete(0, END)
                discipline_list = ""
                for discipline in self.discipline_service.disciplines.discipline_list:
                    for i in range(0, len(ids_list)):
                        if discipline.discipline_id == ids_list[i]:
                            discipline_list += 'Discipline ID: ' + str(discipline.discipline_id).rjust(9) \
                                               + '    Discipline name: ' + str(discipline.discipline_name).rjust(10)
                            discipline_list += '\n\n'
                messagebox.showinfo("List of disciplines", discipline_list)
            except DisciplineException as de:
                self.name_discipline_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error searching for the disciplines - " + str(de))
        else:
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showerror("Error!", "The ID field should be empty!")

    def search_discipline_by_id_gui(self):
        """
        With this function we search for disciplines by a specified id
        :return: it doesn't return anything
        """
        if len(self.name_discipline_to_fill.get()) == 0:
            try:
                ids_list = self.discipline_service.search_discipline_by_id(self.id_discipline_to_fill.get())
                self.id_discipline_to_fill.delete(0, END)
                discipline_list = ""
                for discipline in self.discipline_service.disciplines.discipline_list:
                    for i in range(0, len(ids_list)):
                        if discipline.discipline_id == ids_list[i]:
                            discipline_list += 'Discipline ID: ' + str(discipline.discipline_id).rjust(9) \
                                               + '    Discipline name: ' + str(discipline.discipline_name).rjust(10)
                            discipline_list += '\n\n'
                messagebox.showinfo("List of disciplines", discipline_list)
            except DisciplineException as de:
                self.id_discipline_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error searching for the disciplines - " + str(de))
        else:
            self.name_discipline_to_fill.delete(0, END)
            self.id_discipline_to_fill.delete(0, END)
            messagebox.showerror("Error!", "The name field should be empty!")

    def grade_a_student_gui(self):
        """
        With this function we read the input given by the user and add a new grade for a student
        :return: It doesn't return anything
        """
        try:
            int(self.value_of_grade_to_fill.get())
            try:
                self.grade_service.append_grade_to_student_with_record(Grade(self.id_discipline_grade_to_fill.get().
                                                                             strip(),
                                                                             self.id_student_grade_to_fill.get().
                                                                             strip(),
                                                                             int(self.value_of_grade_to_fill.get())))
                self.id_discipline_grade_to_fill.delete(0, END)
                self.id_student_grade_to_fill.delete(0, END)
                self.value_of_grade_to_fill.delete(0, END)
                messagebox.showinfo("Updated", "The student was graded!")
            except GradeException as ge:
                self.id_discipline_grade_to_fill.delete(0, END)
                self.id_student_grade_to_fill.delete(0, END)
                self.value_of_grade_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error at grading the student - " + str(ge))
            except DisciplineException as de:
                self.id_discipline_grade_to_fill.delete(0, END)
                self.id_student_grade_to_fill.delete(0, END)
                self.value_of_grade_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error at grading the student - " + str(de))
            except StudentException as se:
                self.id_discipline_grade_to_fill.delete(0, END)
                self.id_student_grade_to_fill.delete(0, END)
                self.value_of_grade_to_fill.delete(0, END)
                messagebox.showerror("Error!", "Error at grading the student - " + str(se))
        except ValueError as ve:
            self.id_discipline_grade_to_fill.delete(0, END)
            self.id_student_grade_to_fill.delete(0, END)
            self.value_of_grade_to_fill.delete(0, END)
            messagebox.showerror("Error!", "Invalid value for grade - " + str(ve))

    def display_grade_list_gui(self):
        """
        With this function we display the grades
        :return: it doesn't return anything
        """
        self.grade_service.sort_grades_list()
        grade_list = ""
        for i in range(0, len(self.grade_service.grades)):
            grade_list += "Discipline ID:  " + str(self.grade_service.grades[i].discipline_id_g).rjust(7) \
                          + "   Student ID:  " + str(self.grade_service.grades[i].student_id_g).rjust(9) \
                          + "   Grade:  " + str(self.grade_service.grades[i].grade_value).rjust(5)
            grade_list += '\n\n'
        messagebox.showinfo("List of grades", grade_list)

    def display_students_by_average_gui(self):
        """
        With this function we display all students by their average of the disciplines at which they have grades
        :return: it doesn't return anything
        """
        result = self.grade_service.calculate_average()
        result2 = ""
        for i in range(0, len(result)):
            result2 += "Student ID:  " + str(result[i].student_id_a).rjust(7) + "   Student name:  " \
                       + str(result[i].student_name_a).rjust(15) + "   Discipline ID:  " \
                       + str(result[i].discipline_id_a).rjust(9) + "   Discipline name:  " \
                       + str(result[i].discipline_name_a).rjust(10) + "   Average:  " \
                       + str(result[i].average_a).rjust(5)

            result2 += '\n\n'
        messagebox.showinfo("Averages of the students", result2)

    def display_all_students_who_failed_gui(self):
        """
        With this function we display all the students who failed at one or more disciplines
        :return: It doesn't return anything
        """
        result = self.grade_service.calculate_average()
        result2 = ""
        for i in range(0, len(result)):
            if result[i].average_a < 5:
                result2 += "Student ID:  " + str(result[i].student_id_a).rjust(7) + "   Student name:  " \
                           + str(result[i].student_name_a).rjust(15) + "   Discipline ID:  " \
                           + str(result[i].discipline_id_a).rjust(9) + "   Discipline name:  " \
                           + str(result[i].discipline_name_a).rjust(10) + "   Average:  " \
                           + str(result[i].average_a).rjust(5)

                result2 += '\n\n'
        messagebox.showinfo("Averages of the students", result2)

    def display_students_by_general_average_gui(self):
        """
        With this function we display all students by their general average
        :return: it doesn't return anything
        """

        result = self.grade_service.calculate_general_average_for_each_student()
        result2 = ""
        for i in range(0, len(result)):
            result2 += "Student ID:   " + str(result[i].student_id_ga).rjust(7) + "   Student name:  " \
                       + str(result[i].student_name_ga).rjust(15) + "   General average:   " \
                       + str(result[i].average_ga).rjust(5)
            result2 += '\n\n'
        messagebox.showinfo("General average of the students", result2)

    def display_disciplines_by_general_average_gui(self):
        """
        With this function we display all the disciplines by their general average
        :return: it doesn't return anything
        """
        result = self.grade_service.calculate_average_for_each_discipline()
        result2 = ""
        for i in range(0, len(result)):
            result2 += "Discipline ID:   " + str(result[i].discipline_id_a).rjust(9) + "   Discipline name:  " \
                       + str(result[i].discipline_name_a).rjust(10) + "   Average:  " \
                       + str(result[i].average_a).rjust(5)
            result2 += '\n\n'
        messagebox.showinfo("Average of the disciplines", result2)

    def undo_gui(self):
        """
        With this function we can undo an operation which changed something
        :return: it doesn't return anything
        """
        try:
            self.undo_service.undo()
            messagebox.showinfo("Updated!", "The undo operation was succeeded!")
        except UndoException as ue:
            messagebox.showerror("Error!", "Error trying to undo - " + str(ue))

    def redo_gui(self):
        """
        With this function we can redo an operation after the undo operation was called
        :return: it doesn't return anything
        """
        try:
            self.undo_service.redo()
            messagebox.showinfo("Updated!", "The redo operation was succeeded!")
        except UndoException as ue:
            messagebox.showerror("Error!", "Error trying to redo - " + str(ue))

    def clear_fields(self):

        self.name_discipline_to_fill.delete(0, END)
        self.id_discipline_to_fill.delete(0, END)
        self.id_student_to_fill.delete(0, END)
        self.name_student_to_fill.delete(0, END)
        self.id_discipline_grade_to_fill.delete(0, END)
        self.id_student_grade_to_fill.delete(0, END)
        self.value_of_grade_to_fill.delete(0, END)

    @staticmethod
    def menu_gui(self):
        messagebox.showinfo("MENU", "1. Add a student\n"
                                    "2. Add a discipline\n"
                                    "3. Grade a student\n"
                                    "4. Display the students\n"
                                    "5. Display the disciplines\n"
                                    "6. Display the grades\n"
                                    "7. Remove a student\n"
                                    "8. Remove a discipline\n"
                                    "9. Update a student's name\n"
                                    "10. Update a discipline's name\n"
                                    "11. Search students by name\n"
                                    "12. Search discipline by name\n"
                                    "13. Search students by id\n"
                                    "14. Search discipline by id\n"
                                    "15. Display the students who failed at one or more disciplines\n"
                                    "16. Display the students by their general average\n"
                                    "17. Display the disciplines by their general average grade received by all "
                                    "students enrolled at that discipline\n"
                                    "18. Display the averages of all students\n"
                                    "-1. Undo\n"
                                    "+1. Redo")
