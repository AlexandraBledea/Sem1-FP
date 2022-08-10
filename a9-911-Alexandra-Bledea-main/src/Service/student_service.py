import random
import re
from src.Domain.student import Student, StudentException
from src.Validation.student_validation import StudentValidation


class StudentService:

    def __init__(self, student_repository, undo_service, random_generation=True):
        """
        :param student_repository: student repo which allow us to access the student list
        :param undo_service: the service for the operations undo and redo
        :param random_generation: With this variable we set if we want to random generate some entities at the start
        of the program or not
        """
        self.students = student_repository
        self._undo_service = undo_service
        if random_generation:
            self.generate_random_student()
        self.sort_students_list()

    def append_student_to_list(self, student):
        """
        With this function, after the conditions are checked we add a new student to the list
        :param student: Represents the new student we want to add
        :return: It doesn't return anything
        """
        StudentValidation.validate_student_id(student.student_id)
        StudentValidation.validate_student_name(student.student_name)
        StudentValidation.check_duplicate_id_student(student.student_id, self.students.student_list)
        self.students.add_student_to_list(student)

    def append_student_to_list_with_record(self, student):
        """
        With this function after we add a new student, we keep the record of the operation for undo/redo
        :param student: the new student we want to add
        :return: it doesn't return anything
        """
        self.append_student_to_list(student)

        operation = self._undo_service.create_new_add_operation(self.remove_student_from_list, [student.student_id],
                                                                self.append_student_to_list, [student])
        self._undo_service.record(operation)

    def remove_student_from_list(self, student_id):
        """
        With this function, if the conditions are checked we delete a student from the list
        :param student_id: Represents the id of the student we want to delete
        :return: We return the object student, both with its id and its name
        """
        StudentValidation.validate_student_id(student_id)
        student_deleted = False
        while not student_deleted:
            if StudentValidation.check_existence_of_student_id(student_id, self.students.student_list):
                i = 0
                while i < len(self.students.student_list):
                    s = self.students.student_list[i]
                    if s.student_id == student_id:
                        self.students.delete_student_from_list(i)
                        student = s
                        student_deleted = True
                    else:
                        i = i + 1
        return student

    def remove_student_from_list_with_record(self, student_id, grade_service):
        """
        With this function after we remove a given student, we keep the record of the operation for undo/redo
        :param grade_service: it represents the class which contains the functionalities for handling the grades
        :param student_id: Represents the id for the student we want to remove
        :return: it returns the operation composed of the function undo and redo
        """
        all_operations = ()

        student = self.remove_student_from_list(student_id)
        student_operation = self._undo_service.create_new_remove_operation(self.remove_student_from_list, [student_id],
                                                                           self.append_student_to_list, [student])

        grade_operations = grade_service.remove_grade_from_list_with_student_id(student_id)

        all_operations = all_operations + (student_operation,)
        all_operations = all_operations + grade_operations

        self._undo_service.add_new_cascading_operation(*all_operations)

    def generate_random_student(self, cont=10):
        """
        :param cont: it represents how many students we want to random generate
        :return: it doesn't return anything
        """
        if len(self.students.student_list) != 0:
            return

        done = False
        i = 0

        unique_id_students = ['1433-421', '4325-423', '9836-645', '2451-524', '2451-534', '1231-432', '6473-826',
                              '1682-262', '2519-262', '9982-112']

        students_names = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Luna Lovegood', 'Lord Voldemort',
                          'Ginny Weasley', 'Neville LongBottom', 'Draco Malfoy', 'Fred Weasley', 'George Weasley']
        while not done:
            try:
                while i <= cont:
                    student_id = random.choice(unique_id_students)
                    student_name = random.choice(students_names)
                    self.append_student_to_list(Student(student_id, student_name))
                    i = i + 1
            except StudentException:
                if len(self.students.student_list) != 10:
                    cont = cont + 1
                else:
                    done = True

    def update_student_name(self, student_id, new_name):
        """
        With this function we update the name of a student if the conditions are checked
        :param student_id: The id of the student for which we want to update the name
        :param new_name: The new name we want to give to the specified student
        :return: It returns the initial name of the student
        """
        StudentValidation.validate_student_id(student_id)
        StudentValidation.validate_student_name(new_name)
        if StudentValidation.check_existence_of_student_id(student_id, self.students.student_list):
            for i in range(0, len(self.students.student_list)):
                if self.students.student_list[i].student_id == student_id:
                    name = self.students.student_list[i].student_name
                    self.students.update_student(new_name, i)
        return name

    def update_student_name_with_record(self, student_id, new_name):
        """
        With this function after the name of the student was updated we keep record of the operation for undo and redo
        :param student_id: the id of the student for which we want to update the name
        :param new_name: the new name we want to give to the specified student
        :return: it doesn't return anything
        """
        name = self.update_student_name(student_id, new_name)

        operation = self._undo_service.create_new_update_operation(self.update_student_name, [student_id, name],
                                                                   [student_id, new_name])
        self._undo_service.record(operation)

    def search_student_by_name(self, name):
        """
        With this function we check if a given substring is part of the name of any student
        :param name: the substring given
        :return: the list of student's ids
        """
        if len(name) == 0:
            raise StudentException("A name is required!")
        existent = False
        student_id_list = []
        for student in self.students.student_list:
            if re.search(name.lower().strip(), student.student_name.lower()):
                student_id_list.append(student.student_id)
                existent = True
        if not existent:
            raise StudentException("There is no existing student which contains the substring given!")
        else:
            return student_id_list

    def search_student_by_id(self, student_id):
        """
        With this funcion we check if a given substring is part of the id of any student
        :param student_id: the substring given
        :return: the list of student's ids
        """
        if len(student_id) == 0:
            raise StudentException("An ID is required!")
        existent = False
        student_id_list = []
        for student in self.students.student_list:
            if re.search(student_id.strip(), student.student_id):
                student_id_list.append(student.student_id)
                existent = True
        if not existent:
            raise StudentException("There is no existing student with the provided ID!")
        else:
            return student_id_list

    def sort_students_list(self):
        """
        With this function we sort the students list by the IDs
        :return: it doesn't return anything
        """
        self.students.student_list.sort(reverse=False, key=lambda x: x.student_id)
