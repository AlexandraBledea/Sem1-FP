import random
from src.Domain.grade import Grade
from src.Service.data_transfer_objects import AverageStudentsStatistic, GeneralAverageStudentsStatistic, \
    AverageDisciplineStatistic
from src.Service.discipline_service import DisciplineService
from src.Service.student_service import StudentService
from src.Validation.discipline_validation import DisciplineValidation
from src.Validation.grade_validation import GradeValidation
from src.Validation.student_validation import StudentValidation
from src.Iterable.iterable_object import IterableObject


class GradeService:

    def __init__(self, discipline_repository, student_repository, grade_repository, undo_service,
                 random_generation=True):
        """
        :param discipline_repository: discipline repo which allows us to access the discipline list
        :param student_repository: student repo which allow us to access the student list
        :param grade_repository: grade repo which allows us to access the grade list
        :param undo_service: the service for the operations undo and redo
        :param random_generation: With this variable we set if we want to random generate some entities at the start
        of the program or not
        """
        self.discipline_repo = discipline_repository
        self.students_repo = student_repository
        self.grades = grade_repository
        self._undo_service = undo_service
        if random_generation:
            self.generate_random_grades()
        self.sort_grades_list()

    def append_grade_to_student(self, grade):
        """
        With this function, if the conditions are checked we add a new grade to the list
        :param grade: The grade we want to add
        :return: It doesn't return anything
        """
        DisciplineValidation.validate_discipline_id(grade.discipline_id_g)
        StudentValidation.validate_student_id(grade.student_id_g)
        GradeValidation.validate_grade_value(grade.grade_value)
        if DisciplineValidation.check_existence_of_discipline_id(grade.discipline_id_g, self.discipline_repo.
                                                                 discipline_list):
            if StudentValidation.check_existence_of_student_id(grade.student_id_g, self.students_repo.student_list):
                self.grades.add_grade_to_list(grade)

    def append_grade_to_student_with_record(self, grade):
        """
        With this function after we add a new grade to the list, we keep record of the operation for undo and redo
        :param grade: represents the grade we want to add to the list
        :return: It doesn't return anything
        """
        self.append_grade_to_student(grade)

        index = -1
        operation = self._undo_service.create_new_add_operation(self.reverse_append_grade_to_student, [index],
                                                                self.append_grade_to_student, [grade])
        self._undo_service.record(operation)

    def reverse_append_grade_to_student(self, index):
        """
        With this function we delete a grade based on it's position in list
        :param index: represents the position of the grade in list
        :return: It doesn't return anything
        """
        self.grades.delete_grade_from_list(index)

    def remove_grade_from_list_with_student_id(self, student_id):
        """
        With this function we delete all the grades which are related to a student
        :param student_id: Represents the id of the student for which we want to remove the grades
        :return: it doesn't return anything
        """
        operations = ()
        i = 0
        while i < len(self.grades.grade_list):
            g = self.grades.grade_list[i]
            if g.student_id_g == student_id:
                self.grades.delete_grade_from_list(i)
                operation = self._undo_service.create_new_remove_operation(self.reverse_append_grade_to_student, [i],
                                                                           self.append_grade_to_student, [g])
                operations = operations + (operation,)
            else:
                i = i + 1

        return operations

    def remove_grade_from_list_with_discipline_id(self, discipline_id):
        """
        With this function we delete all the grades which are related to a discipline
        :param discipline_id: Represents the id of the discipline for which we want to remove the grades
        :return: it doesn't return anything
        """
        operations = ()
        i = 0
        while i < len(self.grades.grade_list):
            g = self.grades.grade_list[i]
            if g.discipline_id_g == discipline_id:
                self.grades.delete_grade_from_list(i)
                operation = self._undo_service.create_new_remove_operation(self.reverse_append_grade_to_student, [i],
                                                                           self.append_grade_to_student, [g])
                operations = operations + (operation,)
            else:
                i = i + 1
        return operations

    def generate_random_grades(self, cont=20):
        """
        :param cont: represents the number of random grades we want to generate
        :return:it doesn't return anything
        """
        if len(self.grades.grade_list) != 0:
            return

        student_service = StudentService(self.students_repo, self._undo_service)
        discipline_service = DisciplineService(self.discipline_repo, self._undo_service)
        for i in range(0, cont):
            self.grades.add_grade_to_list(Grade(discipline_service.
                                                disciplines.discipline_list[random.randint(0, len(discipline_service.
                                                                                                  disciplines.
                                                                                                  discipline_list))-1].
                                                discipline_id, student_service.students.student_list[random.
                                                randint(0, len(student_service.students.student_list))-1].student_id,
                                                random.randint(1, 10)))

    def calculate_average(self):
        """
        With this function we calculate the average for each student at disciplines it has grades
        :return: the list with the average grade which a student have at each discipline at which he received grades
        """
        i = 0
        result = []
        while i < len(self.students_repo.student_list):
            for discipline in self.discipline_repo.discipline_list:
                sum_of_grades = 0
                number_of_grades = 0
                average = 0
                for grade in self.grades.grade_list:
                    if self.students_repo.student_list[i].student_id == grade.student_id_g and \
                            discipline.discipline_id == grade.discipline_id_g:
                        sum_of_grades = sum_of_grades + int(grade.grade_value)
                        number_of_grades = number_of_grades + 1
                        average = sum_of_grades / number_of_grades
                if average != 0:
                    result.append(AverageStudentsStatistic(self.students_repo.student_list[i].student_id,
                                                           self.students_repo.student_list[i].student_name,
                                                           discipline.discipline_id, discipline.discipline_name,
                                                           average))
            i = i + 1
        IterableObject.sort(result, lambda average1, average2: average1.average_a <= average2.average_a)
        return result

    def calculate_general_average_for_each_student(self):
        """
        With this function we calculate the general average for each student who had received grades
        :return: the list with the general average for each student who had received grades
        """

        average_list = self.calculate_average()
        result = []
        i = 0
        while i < len(self.students_repo.student_list):
            sum_of_grades = 0
            number_of_grades = 0
            general_average = 0
            for average in average_list:
                if self.students_repo.student_list[i].student_id == average.student_id_a:
                    sum_of_grades = sum_of_grades + average.average_a
                    number_of_grades = number_of_grades + 1
                    general_average = sum_of_grades / number_of_grades
            if general_average != 0:
                result.append(GeneralAverageStudentsStatistic(self.students_repo.student_list[i].student_id,
                                                              self.students_repo.student_list[i].student_name,
                                                              general_average))
            i = i + 1

        IterableObject.sort(result, lambda average1, average2: average1.average_ga <= average2.average_ga)
        return result

    def calculate_average_for_each_discipline(self):
        """
        With this function we calculate the average grade received by the students for each discipline
        :return: the list with the average grade for each discipline
        """
        result = []
        for discipline in self.discipline_repo.discipline_list:
            sum_of_grades = 0
            number_of_grades = 0
            average = 0
            for grade in self.grades.grade_list:
                if discipline.discipline_id == grade.discipline_id_g:
                    sum_of_grades = sum_of_grades + int(grade.grade_value)
                    number_of_grades = number_of_grades + 1
                    average = sum_of_grades / number_of_grades
            if average != 0:
                result.append(AverageDisciplineStatistic(discipline.discipline_id,
                                                         discipline.discipline_name, average))

        IterableObject.sort(result, lambda average1, average2: average1.average_a <= average2.average_a)
        return result

    def sort_grades_list(self):
        """
        With this function we sort the grades list according to the IDs of the disciplines
        :return: It doesn't return anything
        """
        IterableObject.sort(self.grades.grade_list, lambda grade1, grade2: grade1.discipline_id_g >=
                            grade2.discipline_id_g)
