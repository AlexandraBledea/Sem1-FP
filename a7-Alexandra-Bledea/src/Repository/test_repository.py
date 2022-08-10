import unittest
from src.Domain.entity import Student, Discipline, Grade
from src.Repository.repository import StudentRepository, DisciplineRepository, GradeRepository


class StudentRepositoryTest(unittest.TestCase):

    def test_add_student(self):
        list1 = []
        students = StudentRepository()

        list1.append('1436-384 |   Ariana Grande')
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.add_student_to_list(s1)
        self.assertEqual(str(students.student_list[0]), list1[0])

        list1.append('1736-384 |      Mike Perry')
        student_id = '1736-384'
        student_name = 'Mike Perry'
        s2 = Student(student_id, student_name)
        students.add_student_to_list(s2)
        self.assertNotEqual(str(students.student_list[1]), list1[0])
        self.assertEqual(str(students.student_list[1]), list1[1])

        list1.append('1627-478 |    Selena Gomez')
        student_id = '1627-478'
        student_name = 'Selena Gomez'
        s3 = Student(student_id, student_name)
        students.add_student_to_list(s3)
        self.assertNotEqual(str(students.student_list[2]), list1[0])
        self.assertNotEqual(str(students.student_list[2]), list1[1])
        self.assertEqual(str(students.student_list[2]), list1[2])

        list1.append('1457-473 |   Martin Garrix')
        student_id = '1457-473'
        student_name = 'Martin Garrix'
        s4 = Student(student_id, student_name)
        students.add_student_to_list(s4)
        self.assertNotEqual(str(students.student_list[3]), list1[0])
        self.assertNotEqual(str(students.student_list[3]), list1[1])
        self.assertNotEqual(str(students.student_list[3]), list1[2])
        self.assertEqual(str(students.student_list[3]), list1[3])

    def test_delete_student_from_list(self):
        students = StudentRepository()

        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.add_student_to_list(s1)

        student_id = '1736-384'
        student_name = 'Mike Perry'
        s2 = Student(student_id, student_name)
        students.add_student_to_list(s2)

        student_id = '1627-478'
        student_name = 'Selena Gomez'
        s3 = Student(student_id, student_name)
        students.add_student_to_list(s3)

        student_id = '1457-473'
        student_name = 'Martin Garrix'
        s4 = Student(student_id, student_name)
        students.add_student_to_list(s4)

        students.delete_student_from_list(3)
        self.assertNotEqual(len(students.student_list), 4)
        self.assertEqual(len(students.student_list), 3)
        self.assertEqual(str(students.student_list[2]), '1627-478 |    Selena Gomez')

        students.delete_student_from_list(2)
        self.assertNotEqual(len(students.student_list), 3)
        self.assertEqual(len(students.student_list), 2)
        self.assertEqual(str(students.student_list[1]), '1736-384 |      Mike Perry')

        students.delete_student_from_list(1)
        self.assertNotEqual(len(students.student_list), 2)
        self.assertEqual(len(students.student_list), 1)
        self.assertEqual(str(students.student_list[0]), '1436-384 |   Ariana Grande')

        students.delete_student_from_list(0)
        self.assertNotEqual(len(students.student_list), 1)
        self.assertEqual(len(students.student_list), 0)

    def test_get_student(self):
        students = StudentRepository()
        students.add_student_to_list('1436-384 |   Ariana Grande')
        self.assertEqual(students[0], '1436-384 |   Ariana Grande')

    def test_length_students(self):
        students = StudentRepository()
        students.add_student_to_list('1436-384 |   Ariana Grande')
        self.assertEqual(len(students), 1)


class DisciplineRepositoryTest(unittest.TestCase):

    def test_add_discipline(self):
        list1 = []
        disciplines = DisciplineRepository()

        list1.append('12-43-432 |   Geometry')
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d1)
        self.assertEqual(str(disciplines.discipline_list[0]), list1[0])

        list1.append('65-32-184 |    Algebra')
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d2)
        self.assertNotEqual(str(disciplines.discipline_list[1]), list1[0])
        self.assertEqual(str(disciplines.discipline_list[1]), list1[1])

        list1.append('43-32-454 |  Chemistry')
        discipline_id = '43-32-454'
        discipline_name = 'Chemistry'
        d3 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d3)
        self.assertNotEqual(str(disciplines.discipline_list[2]), list1[0])
        self.assertNotEqual(str(disciplines.discipline_list[2]),list1[1])
        self.assertEqual(str(disciplines.discipline_list[2]), list1[2])

    def test_delete_discipline_from_list(self):
        disciplines = DisciplineRepository()

        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d1)

        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d2)

        discipline_id = '43-32-454'
        discipline_name = 'Chemistry'
        d3 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d3)

        disciplines.delete_discipline_from_list(2)
        self.assertNotEqual(len(disciplines.discipline_list), 3)
        self.assertEqual(len(disciplines.discipline_list), 2)
        self.assertEqual(str(disciplines.discipline_list[1]), '65-32-184 |    Algebra')

        disciplines.delete_discipline_from_list(1)
        self.assertNotEqual(len(disciplines.discipline_list), 2)
        self.assertEqual(len(disciplines.discipline_list), 1)
        self.assertEqual(str(disciplines.discipline_list[0]), '12-43-432 |   Geometry')

        disciplines.delete_discipline_from_list(0)
        self.assertNotEqual(len(disciplines.discipline_list), 1)
        self.assertEqual(len(disciplines.discipline_list), 0)

    def test_get_discipline(self):
        disciplines = DisciplineRepository()
        disciplines.add_discipline_to_list('12-43-432 |   Geometry')
        self.assertEqual(disciplines[0], '12-43-432 |   Geometry')

    def test_length_discipline(self):
        disciplines = DisciplineRepository()
        disciplines.add_discipline_to_list('12-43-432 |   Geometry')
        self.assertEqual(len(disciplines), 1)


class GradeRepositoryTest(unittest.TestCase):

    def test_add_grade(self):
        list1 = []
        grades = GradeRepository()

        list1.append('12-43-432 | 1736-384 |  10')
        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g1)
        self.assertEqual(str(grades.grade_list[0]), list1[0])

        list1.append('76-35-274 | 1236-684 |   1')
        student_id = '1236-684'
        discipline_id = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g2)
        self.assertNotEqual(str(grades.grade_list[1]), list1[0])
        self.assertEqual(str(grades.grade_list[1]), list1[1])

        list1.append('72-09-164 | 2156-856 |   7')
        student_id = '2156-856'
        discipline_id = '72-09-164'
        grade_value = 7
        g3 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g3)
        self.assertNotEqual(str(grades.grade_list[2]), list1[0])
        self.assertNotEqual(str(grades.grade_list[2]), list1[1])
        self.assertEqual(str(grades.grade_list[2]), list1[2])

    def test_delete_grade_from_list(self):
        grades = GradeRepository()

        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g1)

        student_id = '1236-684'
        discipline_id = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g2)

        student_id = '2156-856'
        discipline_id = '72-09-164'
        grade_value = 7
        g3 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g3)

        grades.delete_grade_from_list(2)
        self.assertNotEqual(len(grades.grade_list), 3)
        self.assertEqual(len(grades.grade_list), 2)
        self.assertEqual(str(grades.grade_list[1]), '76-35-274 | 1236-684 |   1')

        grades.delete_grade_from_list(1)
        self.assertNotEqual(len(grades.grade_list), 2)
        self.assertEqual(len(grades.grade_list), 1)
        self.assertEqual(str(grades.grade_list[0]), '12-43-432 | 1736-384 |  10')

        grades.delete_grade_from_list(0)
        self.assertNotEqual(len(grades.grade_list), 1)
        self.assertEqual(len(grades.grade_list), 0)

    def test_get_grade(self):
        grades = GradeRepository()
        grades.add_grade_to_list('12-43-432 | 1736-384 |  10')
        self.assertEqual(grades[0], '12-43-432 | 1736-384 |  10')

    def test_length_grade(self):
        grades = GradeRepository()
        grades.add_grade_to_list('12-43-432 | 1736-384 |  10')
        self.assertEqual(len(grades), 1)