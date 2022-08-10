

class GradeException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


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
