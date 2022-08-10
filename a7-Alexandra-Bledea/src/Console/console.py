from src.Domain.entity import Student, Discipline, Grade
from src.Domain.entity import GradeException, StudentException, DisciplineException


class Console:

    def __init__(self, student_service, discipline_service, grade_service):
        self.students_service = student_service
        self.discipline_service = discipline_service
        self.grade_service = grade_service

    def grade_a_student_ui(self):
        """
        With this function we read the input given by the user and add a new grade for a student
        :return: It doesn't return anything
        """
        discipline_id = input('Enter the id of the discipline: ').strip()
        student_id = input('Enter the id of the student: ').strip()
        grade_value = int(input('Add the grade: '))
        self.grade_service.append_grade_to_student(Grade(discipline_id, student_id, grade_value))

    def display_students_by_average_ui(self):
        """
        With this function we display all students by their average of the disciplines at which they have grades
        :return: it doesn't return anything
        """
        result = self.grade_service.calculate_average()
        for average in result:
            print(average)

    def display_students_by_general_average_ui(self):
        """
        With this function we display all students by their general average
        :return: it doesn't return anything
        """

        result = self.grade_service.calculate_general_average_for_each_student()
        for average in result:
            print(average)

    def display_all_students_who_failed_ui(self):
        """
        With this function we display all the students who failed at one or more disciplines
        :return: It doesn't return anything
        """
        result = self.grade_service.calculate_average()
        for average in result:
            if average.average_a < 5:
                print(average)

    def display_disciplines_by_general_average_ui(self):
        """
        With this function we display all the disciplines by their general average
        :return: it doesn't return anything
        """
        result = self.grade_service.calculate_average_for_each_discipline()
        for average in result:
            print(average)

    def display_grade_list_ui(self):
        """
        With this function we display the grades
        :return: it doesn't return anything
        """
        for grade in self.grade_service.grades.grade_list:
            print(grade)

    def add_student_ui(self):
        """
        With this function we read the input given by the user and add a new student
        :return: It doesn't return anything
        """
        student_id = input('Add student id: ').strip()
        student_name = input('Add student name: ').strip()
        self.students_service.append_student_to_list(Student(student_id, student_name))

    def display_student_list_ui(self):
        """
        With this function we display the students
        :return: It doesn't return anything
        """
        for student in self.students_service.students.student_list:
            print(str(student))

    def delete_student_ui(self):
        """
        With this function we delete a student and all the grades related to it
        :return: it doesn't return anything
        """
        student_id = input("Enter the student's id you want to delete: ").strip()
        self.students_service.remove_student_from_list(student_id)
        self.grade_service.remove_grade_from_list_with_student_id(student_id)

    def update_student_name_ui(self):
        """
        With this function we update the name of a specified student
        :return: it doesn't return anything
        """
        student_id = input("Enter the id for the student you want to update the name: ").strip()
        new_name = input("Enter the new name for the student: ").strip()
        self.students_service.update_student_name(student_id, new_name)

    def search_student_by_name_ui(self):
        """
        With this function we search for students by a specified name
        :return: it doesn't return anything
        """
        name = input("Enter the name: ")
        ids_list = self.students_service.search_student_by_name(name)
        for student in self.students_service.students.student_list:
            for i in range(0, len(ids_list)):
                if student.student_id == ids_list[i]:
                    print(student)

    def search_student_by_id_ui(self):
        """
        With this function we search for students by a specified id
        :return: it doesn't return anything
        """
        student_id = input("Enter the id: ")
        ids_list = self.students_service.search_student_by_id(student_id)
        for student in self.students_service.students.student_list:
            for i in range(0, len(ids_list)):
                if student.student_id == ids_list[i]:
                    print(student)

    def add_discipline_ui(self):
        """
        With this function we read the input given by the user and add a new discipline
        :return: it doesn't return anything
        """
        discipline_id = input('Add discipline id: ').strip()
        discipline_name = input('Add discipline name: ').strip()
        self.discipline_service.append_discipline_to_list(Discipline(discipline_id, discipline_name))

    def display_discipline_list_ui(self):
        """
        With this function we display the disciplines
        :return: it doesn't return anything
        """
        for discipline in self.discipline_service.disciplines.discipline_list:
            print(discipline)

    def delete_discipline_ui(self):
        """
        With this function we delete a discipline and all the grades related to it
        :return: It doesn't return anything
        """
        discipline_id = input("Enter the discipline's id you want to delete: ").strip()
        self.discipline_service.remove_discipline_from_list(discipline_id)
        self.grade_service.remove_grade_from_list_with_discipline_id(discipline_id)

    def update_discipline_name_ui(self):
        """
        With this function we update the name of a specified discipline
        :return: it doesn't return anything
        """
        discipline_id = input("Enter the id for the discipline you want to update the name: ").strip()
        new_name = input("Enter the new name for the discipline: ").strip()
        self.discipline_service.update_name_discipline(discipline_id, new_name)

    def search_discipline_by_name_ui(self):
        """
        With this function we search for disciplines by a specified name
        :return: it doesn't return anything
        """
        name = input("Enter the name: ")
        ids_list = self.discipline_service.search_discipline_by_name(name)
        for discipline in self.discipline_service.disciplines.discipline_list:
            for i in range(0, len(ids_list)):
                if discipline.discipline_id == ids_list[i]:
                    print(discipline)

    def search_discipline_by_id_ui(self):
        """
        With this function we search for disciplines by a specified id
        :return: it doesn't return anything
        """
        discipline_id = input("Enter the id: ")
        ids_list = self.discipline_service.search_discipline_by_id(discipline_id)
        for discipline in self.discipline_service.disciplines.discipline_list:
            for i in range(0, len(ids_list)):
                if discipline.discipline_id == ids_list[i]:
                    print(discipline)

    @staticmethod
    def print_menu():
        print("1. Add a student")
        print("2. Add a discipline")
        print("3. Grade a student")
        print("4. Display the students")
        print("5. Display the disciplines")
        print("6. Display the grades")
        print("7. Remove a student")
        print("8. Remove a discipline")
        print("9. Update a student's name")
        print("10. Update a discipline's name")
        print("11. Search students by name")
        print("12. Search discipline by name")
        print("13. Search students by id")
        print("14. Search discipline by id")
        print("15. Display the students who failed at one or more disciplines")
        print("16. Display the students by their general average")
        print("17. Display the disciplines by their general average grade received by all students enrolled at "
              "that discipline")
        print("18. Display the averages of all students")

    def start_command_ui(self):
        """
        It is the start function
        :return: it doesn't return anything, but call other functions if the command given by the user is not invalid
        """

        command_dict = {'1': self.add_student_ui, '2': self.add_discipline_ui, '3': self.grade_a_student_ui,
                        '4': self.display_student_list_ui, '5': self.display_discipline_list_ui,
                        '6': self.display_grade_list_ui, '7': self.delete_student_ui, '8': self.delete_discipline_ui,
                        '9': self.update_student_name_ui, '10': self.update_discipline_name_ui,
                        '11': self.search_student_by_name_ui, '12': self.search_discipline_by_name_ui,
                        '13': self.search_student_by_id_ui, '14': self.search_discipline_by_id_ui,
                        '15': self.display_all_students_who_failed_ui, '16': self.display_students_by_general_average_ui
                        , '17': self.display_disciplines_by_general_average_ui,
                        '18': self.display_students_by_average_ui}
        are_we_done_yet = False
        print('\nMENU')
        print('Welcome to Hogwarts School of Witchcraft & Wizardry!!!')
        print('For the commands menu write 0')
        while not are_we_done_yet:
            command = input('\nWhat would you like to do? Enter command: \n')
            if command in command_dict:
                try:
                    command_dict[command]()
                except ValueError as ve:
                    print(ve)
                except GradeException as ge:
                    print(ge)
                except DisciplineException as de:
                    print(de)
                except StudentException as se:
                    print(se)
            elif command == '0':
                self.print_menu()
            elif command == 'x':
                print("Goodbye!")
                are_we_done_yet = True
            else:
                print("Invalid command")
