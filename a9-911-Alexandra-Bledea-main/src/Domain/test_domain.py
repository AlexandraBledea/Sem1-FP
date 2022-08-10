import unittest
from src.Domain.discipline import Discipline, DisciplineException
from src.Domain.grade import Grade, GradeException
from src.Domain.student import Student, StudentException


class StudentTest(unittest.TestCase):

    def test_student(self):
        student_id = 'MM8432'
        student_name = 'Marina Adelina'
        s1 = Student(student_id, student_name)
        self.assertEqual(student_id, s1.student_id)
        self.assertEqual(student_name, s1.student_name)

        student_id2 = 'MM2843'
        student_name2 = 'Ariana Grande'
        s2 = Student(student_id2, student_name2)
        self.assertNotEqual(student_id, s2.student_id)
        self.assertNotEqual(student_name, s2.student_name)
        self.assertEqual(student_id2, s2.student_id)
        self.assertEqual(student_name2, s2.student_name)

    def test_student_string_form(self):
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        student = '1436-384 |   Ariana Grande'
        s1 = Student(student_id, student_name)
        self.assertEqual(student, str(s1))
        student_id = '1736-384'
        student_name = 'Mike Perry'
        student = '1736-384  |      Mike Perry'
        s2 = Student(student_id, student_name)
        self.assertNotEqual(student, str(s2))

    def test_student_exception(self):
        exception = StudentException("Incorrect id!")
        self.assertEqual(str(exception), "Incorrect id!")

    def test_student_id_setter(self):
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)

        s1.student_id = '9999-999'
        self.assertEqual(s1.student_id, '9999-999')

    def test_student_name_setter(self):
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)

        s1.student_name = 'Harry Potter'
        self.assertEqual(s1.student_name, 'Harry Potter')


class DisciplineTest(unittest.TestCase):
    def test_discipline(self):
        discipline_id = 'X123'
        discipline_name = 'Mathematics'
        d1 = Discipline(discipline_id, discipline_name)
        self.assertEqual(discipline_id, d1.discipline_id)
        self.assertEqual(discipline_name, d1.discipline_name)

        discipline_id2 = 'X476'
        discipline_name2 = 'Physics'
        d2 = Discipline(discipline_id2, discipline_name2)
        self.assertNotEqual(discipline_id2, d1.discipline_id)
        self.assertNotEqual(discipline_name2, d1.discipline_name)
        self.assertEqual(discipline_id2, d2.discipline_id)
        self.assertEqual(discipline_name2, d2.discipline_name)

    def test_discipline_string_form(self):
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        self.assertEqual(str(d1), '12-43-432 |   Geometry')
        discipline_id2 = '65-32-184'
        discipline_name2 = 'Algebra'
        d2 = Discipline(discipline_id2, discipline_name2)
        self.assertEqual(str(d2), '65-32-184 |    Algebra')
        self.assertNotEqual(str(d2), '12-43-432 |   Geometry')
        self.assertNotEqual(str(d1), ' 65-32-184 |    Algebra')

    def test_discipline_exception(self):
        exception = DisciplineException("Incorrect discipline!")
        self.assertEqual(str(exception), "Incorrect discipline!")

    def test_discipline_id_setter(self):
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)

        d1.discipline_id = '99-99-999'
        self.assertEqual(d1.discipline_id, '99-99-999')

    def test_discipline_name_setter(self):
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)

        d1.discipline_name = 'Music'
        self.assertEqual(d1.discipline_name, 'Music')


class GradeTest(unittest.TestCase):

    def test_grade(self):

        student_id = 'MM8432'
        student_name = 'Marina Adelina'
        s1 = Student(student_id, student_name)
        discipline_id = 'X123'
        discipline_name = 'Mathematics'
        d1 = Discipline(discipline_id, discipline_name)
        grade = 10
        g1 = Grade(d1.discipline_id, s1.student_id, grade)
        self.assertEqual(g1.student_id_g, s1.student_id)
        self.assertEqual(g1.discipline_id_g, d1.discipline_id)
        self.assertEqual(g1.grade_value, grade)

    def test_grade_string_form(self):

        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        self.assertEqual(str(g1), '12-43-432 | 1736-384 |  10')
        student_id = '1236-684'
        discipline_id = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        self.assertNotEqual(str(g2), '76-35-274 |   1236-684 |   1')

    def test_grade_exception(self):
        exception = GradeException("Invalid data for grade!")
        self.assertEqual(str(exception), "Invalid data for grade!")


    def test_grade_value_setter(self):
        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)

        g1.grade_value = 1
        self.assertEqual(g1.grade_value, 1)
