from src.Domain.student import StudentException


class StudentValidation:

    @staticmethod
    def validate_student_id(student_id):
        """
        With this function we check if the given id is a valid one or not
        :param student_id: it represents the id we want to check if it's valid or not
        :return: it doesn't return anything, but if the id is not valid it will raise an error
        """
        if len(student_id) != 8:
            raise StudentException("The ID doesn't have the right format! It should be ****-***!")
        for i in range(0, 8):
            if i == 4:
                if student_id[i] != '-':
                    raise StudentException("The ID doesn't have the right format! It should be ****-***!")
            else:
                if not student_id[i].isdigit():
                    raise StudentException("The ID doesn't have the right format! It should be ****-***!")

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
                raise StudentException("There is already and existing student with the same ID and the ID should be"
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
            raise StudentException("There is no existing student with the given ID!")
        else:
            return existent

