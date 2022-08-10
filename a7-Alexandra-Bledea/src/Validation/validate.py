"""
Here we implement the classes which will check if the data introduced is correct
"""
from src.Domain.entity import StudentException, DisciplineException, GradeException


class StudentValidation:

    @staticmethod
    def validate_student_id(student_id):
        """
        With this function we check if the given id is a valid one or not
        :param student_id: it represents the id we want to check if it's valid or not
        :return: it doesn't return anything, but if the id is not valid it will raise an error
        """
        if len(student_id) != 8:
            raise StudentException("The id doesn't have the right format! It should be ****-***!")
        for i in range(0, 8):
            if i == 4:
                if student_id[i] != '-':
                    raise StudentException("The id doesn't have the right format! It should be ****-***!")
            else:
                if not student_id[i].isdigit():
                    raise StudentException("The id doesn't have the right format! It should be ****-***!")

    @staticmethod
    def validate_student_name(student_name):
        """
        With this function we check if the name given for the student is valid or not
        :param student_name: it's the given name we want to check if it's valid or not
        :return: it doesn't return anything, but if the name is not valid it will raise an error
        """
        if len(student_name) == 0:
            raise StudentException("The entered name is invalid!")
        tokens = student_name.strip().split(' ')
        if len(tokens) != 2:
            raise StudentException("The name should be composed of one firstname and one lastname!")
        if not tokens[0].isalpha():
            raise StudentException("The entered name is invalid!")
        if not tokens[1].isalpha():
            raise StudentException("The entered name is invalid!")

    @staticmethod
    def check_duplicate_id_student(student_id, student_list):
        """
        With this function we check is there is already a student with the entered id
        :param student_id: the id we check if already exists
        :param student_list: the list of students
        :return: it doesn't return anything
        """
        for s in student_list:
            if s.student_id == student_id:
                raise StudentException("There is already and existing student with the same id and the id should be"
                                       " unique!")

    @staticmethod
    def check_existence_of_student_id(student_id, student_list):
        """
        With this function we check if the student with the given id exists
        :param student_id: the id for which we check the existence
        :param student_list: the list of students
        :return: it doesn't return anything
        """
        existent = False
        for s in student_list:
            if s.student_id == student_id:
                existent = True
        if not existent:
            raise StudentException("There is no existing student with the given id!")


class DisciplineValidation:

    @staticmethod
    def validate_discipline_id(discipline_id):
        """
        With this function we want to check if the given id for the discipline is valid or not
        :param discipline_id: It's the given id we want to check if it's valid or not
        :return: it doesn't return anything, but if the id is not valid it will raise an error
        """
        if len(discipline_id) != 9:
            raise DisciplineException("The id doesn't have the right format! It should be **-**-***!")
        for i in range(0, 9):
            if i == 2:
                if discipline_id[i] != '-':
                    raise DisciplineException("The id doesn't have the right format! It should be **-**-***!")
            elif i == 5:
                if discipline_id[i] != '-':
                    raise DisciplineException("The id doesn't have the right format! It should be **-**-***!")
            elif not discipline_id[i].isdigit():
                raise DisciplineException("The id doesn't have the right format! It should be **-**-***!")

    @staticmethod
    def validate_discipline_name(discipline_name):
        """
        With this function we want to check if the given name for the discipline is valid or not
        :param discipline_name: It's the given name we want to check if it's valid or not
        :return: it doesn't return anything, but if the name is not valid it will raise an error
        """
        tokens = discipline_name.split(' ')
        if len(tokens) != 1:
            raise DisciplineException("The entered name is invalid!")
        if not discipline_name.isalpha():
            raise DisciplineException("The entered name is invalid!")

    @staticmethod
    def check_duplicate_id_discipline(discipline_id, discipline_list):
        """
        With this function we check if a given id for a discipline already exists
        :param discipline_id: the id we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        for d in discipline_list:
            if d.discipline_id == discipline_id:
                raise DisciplineException("There is already a discipline with the given id and the id should be"
                                          " unique!")

    @staticmethod
    def check_duplicate_name_discipline(discipline_name, discipline_list):
        """
        With this function we check if a given name for a discipline already exists
        :param discipline_name: the name we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        for d in discipline_list:
            if d.discipline_name == discipline_name:
                raise DisciplineException("There is already the given discipline name and each discipline should"
                                          " have unique name!")

    @staticmethod
    def check_existence_of_discipline_id(discipline_id, discipline_list):
        """
        With this function we check if a give discipline id exists
        :param discipline_id: the id we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        existent = False
        for d in discipline_list:
            if d.discipline_id == discipline_id:
                existent = True
        if not existent:
            raise DisciplineException("There is no existing discipline with the given id!")


class GradeValidation:

    @staticmethod
    def validate_grade_value(grade_value):
        """
        With this function we want to check if a given grade is valid or not
        :param grade_value: It's the given grade we want to check if it's valid or not
        :return: it doesn't return anything, but if the value for the grade is not valid it will raise an error
        """
        if 1 > grade_value or grade_value > 10:
            raise GradeException("Invalid value for the grade. It should be a number from 0 to 10!")

    @staticmethod
    def check_existence_of_grade_student(student_id, grade_list):
        """
        With this function we check if a specified students have any grades
        :param student_id: the id for the student we want to check the existence of the grades
        :param grade_list: the list of grades
        :return: it doesn't return anything
        """
        existent = False
        for g in grade_list:
            if g.student_id_g == student_id:
                existent = True
        if not existent:
            raise GradeException("There are no grades registered for the given student id but the student was deleted!")

    @staticmethod
    def check_the_existence_of_grade_discipline(discipline_id, grade_list):
        """
        With this function we check if a specified discipline have any grades
        :param discipline_id: the id for the discipline we want to check the existence of the grades
        :param grade_list: the list of grades
        :return: it doesn't return anything
        """
        existent = False
        for g in grade_list:
            if g.discipline_id_g == discipline_id:
                existent = True
        if not existent:
            raise GradeException("There are no grades registered for the given discipline id but the discipline"
                                 " was deleted!")


'''

class GeneralValidation:

    @staticmethod
    def is_in_list_validation(list, object):
        if object in list:
            return True
        return False
'''
