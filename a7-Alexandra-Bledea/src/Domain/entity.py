"""
Here we are going to implement the classes for the entities.
"""


class StudentException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class DisciplineException(Exception):
    def __init__(self, msg):
        self._msg = msg


class GradeException(Exception):
    def __init__(self, msg):
        self._msg = msg


class Student:

    def __init__(self, id_, name):
        """
        :param id_: the unique student id
        :param name: the name of the student
        """

        self._student_id = id_
        self._student_name = name

    @property
    def student_id(self):
        return self._student_id

    @student_id.setter
    def student_id(self, new_id):
        self._student_id = new_id

    @property
    def student_name(self):
        return self._student_name

    @student_name.setter
    def student_name(self, new_name):
        self._student_name = new_name

    def __str__(self):
        """
        :return: returns the string form of a student
        """
        return str(self.student_id).rjust(6) + ' | ' + str(self.student_name).rjust(15)


class Discipline:

    def __init__(self, id_, name):
        """
        :param id_: the unique id for the discipline
        :param name: the name of the discipline
        """
        self._discipline_id = id_
        self._discipline_name = name

    @property
    def discipline_id(self):
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, new_id):
        self._discipline_id = new_id

    @property
    def discipline_name(self):
        return self._discipline_name

    @discipline_name.setter
    def discipline_name(self, new_name):
        self._discipline_name = new_name

    def __str__(self):
        """
        :return: the string form of a discipline
        """
        return str(self.discipline_id).rjust(9) + ' | ' + str(self.discipline_name).rjust(10)


class Grade:

    def __init__(self, discipline_id, student_id, grade):
        """
        :param discipline_id: takes the unique id of the discipline
        :param student_id: takes the unique id of the student
        :param grade: value of the grade
        """
        self._discipline_id_g = discipline_id
        self._student_id_g = student_id
        self._grade_value = grade

    @property
    def grade_value(self):
        return self._grade_value

    @grade_value.setter
    def grade_value(self, new_value):
        self._grade_value = new_value

    @property
    def student_id_g(self):
        return self._student_id_g

    @property
    def discipline_id_g(self):
        return self._discipline_id_g

    def __str__(self):
        """
        :return: the string form of the grade
        """
        return str(self._discipline_id_g).rjust(9) + ' | ' + str(self.student_id_g). \
            rjust(7) + ' | ' + str(self.grade_value).rjust(3)
