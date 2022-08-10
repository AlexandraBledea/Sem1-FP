"""
Here we are going to implement the classes for the entities.
"""


class StudentException(Exception):
    def __init__(self, msg):
        self._msg = msg


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
        return str(self._discipline_id_g).rjust(9) + ' | ' + str(self.student_id_g).\
            rjust(7) + ' | ' + str(self.grade_value).rjust(3)


class FailedDisciplines:

    def __init__(self, discipline_id, number_of_students, student_id):
        self._discipline = discipline_id
        self._number_of_students = number_of_students
        self._list_of_students = []

    @property
    def get_id(self):
        return self._discipline

    @get_id.setter
    def get_id(self, value):
        self._discipline = value

    @property
    def get_number_of_students(self):
        return self._number_of_students

    @get_number_of_students.setter
    def get_number_of_students(self, value):
        self._number_of_students = value


class TestEntity:

    @staticmethod
    def test_student():
        student_id = 'MM8432'
        student_name = 'Marina Adelina'
        s1 = Student(student_id, student_name)
        assert student_id == s1.student_id
        assert student_name == s1.student_name

    @staticmethod
    def test_student_string_form():
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        student = '1436-384 |   Ariana Grande'
        s1 = Student(student_id, student_name)
        assert student == str(s1)
        student_id = '1736-384'
        student_name = 'Mike Perry'
        student = '1736-384  |      Mike Perry'
        s2 = Student(student_id, student_name)
        assert student != str(s2)

    @staticmethod
    def test_discipline():
        discipline_id = 'X123'
        discipline_name = 'Mathematics'
        d1 = Discipline(discipline_id, discipline_name)
        assert discipline_id == d1.discipline_id
        assert discipline_name == d1.discipline_name

    @staticmethod
    def test_discipline_string_form():
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        assert str(d1) == '12-43-432 |   Geometry'
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        assert str(d2) != ' 65-32-184 |    Algebra'

    @staticmethod
    def test_grade():
        student_id = 'MM8432'
        student_name = 'Marina Adelina'
        s1 = Student(student_id, student_name)
        discipline_id = 'X123'
        discipline_name = 'Mathematics'
        d1 = Discipline(discipline_id, discipline_name)
        grade = 10
        g1 = Grade(d1.discipline_id, s1.student_id, grade)
        assert g1.student_id_g == s1.student_id
        assert g1.discipline_id_g == d1.discipline_id
        assert g1.grade_value == grade

    @staticmethod
    def test_grade_string_form():
        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        assert str(g1) == '12-43-432 | 1736-384 |  10'
        student_id = '1236-684'
        discipline_id = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        assert str(g2) != '76-35-274 |   1236-684 |   1'

    @staticmethod
    def run_all_tests():
        TestEntity.test_student()
        TestEntity.test_discipline()
        TestEntity.test_grade()
        TestEntity.test_student_string_form()
        TestEntity.test_discipline_string_form()
        TestEntity.test_grade_string_form()


TestEntity.run_all_tests()
