

class StudentException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


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


