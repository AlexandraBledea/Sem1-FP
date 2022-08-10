from src.Domain.grade import GradeException


class GradeValidation:

    @staticmethod
    def validate_grade_value(grade_value):
        """
        With this function we want to check if a given grade is valid or not
        :param grade_value: It's the given grade we want to check if it's valid or not
        :return: it doesn't return anything, but if the value for the grade is not valid it will raise an error
        """
        if 1 > int(grade_value) or int(grade_value) > 10:
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
        else:
            return existent

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
            raise GradeException("There are no grades registered for the given discipline ID but the discipline"
                                 " was deleted!")
        else:
            return existent
