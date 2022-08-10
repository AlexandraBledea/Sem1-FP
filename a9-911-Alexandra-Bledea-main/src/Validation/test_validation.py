import unittest
from src.Domain.discipline import Discipline, DisciplineException
from src.Domain.grade import Grade, GradeException
from src.Domain.student import Student, StudentException
from src.Validation.discipline_validation import DisciplineValidation
from src.Validation.grade_validation import GradeValidation
from src.Validation.student_validation import StudentValidation


class StudentValidationTest(unittest.TestCase):

    def test_validate_student_id(self):
        id_student = ['12345674', '1234-saf', 'asghjsahja', '2152167821', '2158@674', 'a152-257', '', '12343-123',
                      'f123-234', '1234-sa4']
        for i in range(0, len(id_student)):
            with self.assertRaises(StudentException):
                StudentValidation.validate_student_id(id_student[i])

    def test_validate_student_name(self):
        student_name = ['', 'Voldemort', 'saha1 216', '1413', 'asbdjk 12h', '126721 3167', '12 sagsa']
        for i in range(0, len(student_name)):
            with self.assertRaises(StudentException):
                StudentValidation.validate_student_name(student_name[i])

    def test_check_duplicate_student_id(self):
        students = []
        ids = ['1736-384', '1432-384']
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.append(s1)
        student_id = '1432-384'
        student_name = 'Selena Gomez'
        s1 = Student(student_id, student_name)
        students.append(s1)
        for i in range(0, len(ids)):
            with self.assertRaises(StudentException):
                StudentValidation.check_duplicate_id_student(ids[i], students)

    def test_check_existence_of_student_id(self):
        students = []
        ids = ['1234-324', '2167-234', '9128-467', '8126-736']
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.append(s1)
        student_id = '1432-384'
        student_name = 'Selena Gomez'
        s1 = Student(student_id, student_name)
        students.append(s1)
        for i in range(0, len(ids)):
            with self.assertRaises(StudentException):
                StudentValidation.check_existence_of_student_id(ids[i], students)

        students = []
        ids = ['1736-384']
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.append(s1)
        return_value = StudentValidation.check_existence_of_student_id(ids[0], students)
        self.assertEqual(return_value, True)


class DisciplineValidationTest(unittest.TestCase):

    def test_validate_discipline_id(self):
        id_discipline = ['safghasj', '', '12-32-32k', '22-32-ags', '23@63-261', 'sa-12-saj', 'as-ds-shj', '12-21@368']
        for i in range(0, len(id_discipline)):
            with self.assertRaises(DisciplineException):
                DisciplineValidation.validate_discipline_id(id_discipline[i])

    def test_validate_discipline_name(self):
        discipline_name = ['', 'ash21', 'GAhdsya sagh21saj sahjsa', 'sagh12sa', '2678', 'asg217sa', 'sagh-saghsa']
        for i in range(0, len(discipline_name)):
            with self.assertRaises(DisciplineException):
                DisciplineValidation.validate_discipline_name(discipline_name[i])

    def test_check_duplicate_discipline_id(self):
        disciplines = []
        ids = ['12-43-432', '65-32-184']
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.append(d1)
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.append(d2)
        for i in range(0, len(ids)):
            with self.assertRaises(DisciplineException):
                DisciplineValidation.check_duplicate_id_discipline(ids[i], disciplines)

    def test_check_duplicate_discipline_name(self):
        disciplines = []
        names = ['Geometry', 'Algebra']
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.append(d1)
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.append(d2)
        for i in range(0, len(names)):
            with self.assertRaises(DisciplineException):
                DisciplineValidation.check_duplicate_name_discipline(names[i], disciplines)

    def test_check_existence_of_discipline_id(self):
        disciplines = []
        ids = ['92-43-123', '09-26-237', '87-23-431', '98-23-234']
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.append(d1)
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.append(d2)
        for i in range(0, len(ids)):
            with self.assertRaises(DisciplineException):
                DisciplineValidation.check_existence_of_discipline_id(ids[i], disciplines)

        disciplines = []
        ids = ['12-43-432']
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.append(d1)
        self.assertEqual(DisciplineValidation.check_existence_of_discipline_id(ids[0], disciplines), True)


class GradeValidationTest(unittest.TestCase):

    def test_validate_grade_value(self):
        grade_value = [-7, -111, -3, -4, 1120, 40]
        for i in range(0, len(grade_value)):
            with self.assertRaises(GradeException):
                GradeValidation.validate_grade_value(grade_value[i])

    def test_check_existence_of_grade_student(self):
        grades = []
        ids = ['8216-324', '1242-123', '3214-234']
        student_id1 = '1736-384'
        discipline_id1 = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades.append(g1)
        student_id2 = '1236-684'
        discipline_id2 = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades.append(g2)
        for i in range(0, len(ids)):
            with self.assertRaises(GradeException):
                GradeValidation.check_existence_of_grade_student(ids[i], grades)

        grades = []
        ids = ['1736-384']
        student_id1 = '1736-384'
        discipline_id1 = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades.append(g1)
        self.assertEqual(GradeValidation.check_existence_of_grade_student(ids[0], grades), True)

    def test_check_existence_of_grade_discipline(self):
        grades = []
        ids = ['16-78-274', '22-55-432', '82-16-324']
        student_id1 = '1736-384'
        discipline_id1 = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades.append(g1)
        student_id2 = '1236-684'
        discipline_id2 = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades.append(g2)
        for i in range(0, len(ids)):
            with self.assertRaises(GradeException):
                GradeValidation.check_the_existence_of_grade_discipline(ids[i], grades)

        grades = []
        ids = ['12-43-432']
        student_id1 = '1736-384'
        discipline_id1 = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades.append(g1)
        self.assertEqual(GradeValidation.check_the_existence_of_grade_discipline(ids[0], grades), True)
