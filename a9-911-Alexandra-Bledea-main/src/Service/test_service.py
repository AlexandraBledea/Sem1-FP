import unittest
from src.Domain.discipline import Discipline, DisciplineException
from src.Domain.grade import Grade
from src.Domain.student import Student, StudentException
from src.Repository.discipline_repository import DisciplineRepository
from src.Repository.grade_repository import GradeRepository
from src.Repository.student_repository import StudentRepository
from src.Service.data_transfer_objects import AverageStudentsStatistic, AverageDisciplineStatistic, \
    GeneralAverageStudentsStatistic
from src.Service.discipline_service import DisciplineService
from src.Service.grade_service import GradeService
from src.Service.student_service import StudentService
from src.Service.undo_service import UndoService, UndoException, FunctionCall, CascadedOperation, Operation


class StudentServiceTest(unittest.TestCase):

    def test_append_student_to_list(self):
        students_repo = StudentRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)

        list1 = list(students_service.students.student_list)

        list1.append('1436-384 |   Ariana Grande')
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s1)
        self.assertEqual(str(students_service.students.student_list[10]), list1[10])

        list1.append('1736-384 |      Mike Perry')
        student_id = '1736-384'
        student_name = 'Mike Perry'
        s2 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s2)
        self.assertNotEqual(str(students_service.students.student_list[11]), list1[10])
        self.assertEqual(str(students_service.students.student_list[11]), list1[11])

        list1.append('1627-478 |    Selena Gomez')
        student_id = '1627-478'
        student_name = 'Selena Gomez'
        s3 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s3)
        self.assertNotEqual(str(students_service.students.student_list[12]), list1[10])
        self.assertNotEqual(str(students_service.students.student_list[12]), list1[11])
        self.assertEqual(str(students_service.students.student_list[12]), list1[12])

        list1.append('1457-473 |   Martin Garrix')
        student_id = '1457-473'
        student_name = 'Martin Garrix'
        s4 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s4)
        self.assertNotEqual(str(students_service.students.student_list[13]), list1[10])
        self.assertNotEqual(str(students_service.students.student_list[13]), list1[11])
        self.assertNotEqual(str(students_service.students.student_list[13]), list1[12])
        self.assertEqual(str(students_service.students.student_list[13]), list1[13])

        student_id = '1457-473'
        student_name = 'Dua Lipa'
        s5 = Student(student_id, student_name)
        with self.assertRaises(StudentException):
            students_service.append_student_to_list_with_record(s5)

        student_id = 'sfaghja'
        student_name = 'Dua Lipa'
        s6 = Student(student_id, student_name)
        with self.assertRaises(StudentException):
            students_service.append_student_to_list_with_record(s6)

        student_id = '1234-213'
        student_name = 'Andreea'
        s7 = Student(student_id, student_name)
        with self.assertRaises(StudentException):
            students_service.append_student_to_list_with_record(s7)

        student_id = '1234-213'
        student_name = ''
        s8 = Student(student_id, student_name)
        with self.assertRaises(StudentException):
            students_service.append_student_to_list_with_record(s8)

    def test_remove_student_from_list(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        students_service = StudentService(students_repo, undo_service)

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list_with_record(s1)

        student_id2 = '1736-384'
        student_name2 = 'Mike Perry'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list_with_record(s2)

        student_id3 = '1627-478'
        student_name3 = 'Selena Gomez'
        s3 = Student(student_id3, student_name3)
        students_service.append_student_to_list_with_record(s3)

        student_id4 = '1457-473'
        student_name4 = 'Martin Garrix'
        s4 = Student(student_id4, student_name4)
        students_service.append_student_to_list_with_record(s4)

        students_service.remove_student_from_list_with_record(student_id4, grades_service)
        self.assertNotEqual(len(students_service.students.student_list), 14)
        self.assertEqual(len(students_service.students.student_list), 13)
        self.assertEqual(str(students_service.students.student_list[12]), '1627-478 |    Selena Gomez')

        students_service.remove_student_from_list_with_record(student_id3, grades_service)
        self.assertNotEqual(len(students_service.students.student_list), 13)
        self.assertEqual(len(students_service.students.student_list), 12)
        self.assertEqual(str(students_service.students.student_list[11]), '1736-384 |      Mike Perry')

        students_service.remove_student_from_list_with_record(student_id2, grades_service)
        self.assertNotEqual(len(students_service.students.student_list), 12)
        self.assertEqual(len(students_service.students.student_list), 11)
        self.assertEqual(str(students_service.students.student_list[10]), '1436-384 |   Ariana Grande')

    def test_update_student_name(self):
        students_repo = StudentRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        new_name1 = 'Justin Bieber'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        self.assertEqual(str(students_service.students.student_list[10]), '1436-384 |   Ariana Grande')
        students_service.update_student_name_with_record(student_id1, new_name1)
        self.assertEqual(str(students_service.students.student_list[10]), '1436-384 |   Justin Bieber')

        student_id2 = '1736-384'
        student_name2 = 'Mike Perry'
        s2 = Student(student_id2, student_name2)
        new_name2 = 'Ariana Grande'
        students_service.append_student_to_list(s2)
        self.assertEqual(str(students_service.students.student_list[11]), '1736-384 |      Mike Perry')
        students_service.update_student_name_with_record(student_id2, new_name2)
        self.assertEqual(str(students_service.students.student_list[11]), '1736-384 |   Ariana Grande')

        student_id3 = '1627-478'
        student_name3 = 'Selena Gomez'
        new_name3 = 'Martin Garrix'
        s3 = Student(student_id3, student_name3)
        students_service.append_student_to_list(s3)
        self.assertEqual(str(students_service.students.student_list[12]), '1627-478 |    Selena Gomez')
        students_service.update_student_name_with_record(student_id3, new_name3)
        self.assertEqual(str(students_service.students.student_list[12]), '1627-478 |   Martin Garrix')

    def test_search_student_by_name(self):
        students_repo = StudentRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        substring1 = 'Ari'
        substring2 = 'GranD'
        substring3 = 'Ariana '
        substring4 = ' Grande'
        substring5 = 'ArIaNA'
        substring6 = 'Ariana Grandeeee'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        list1 = students_service.search_student_by_name(substring1)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_name(substring2)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_name(substring3)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_name(substring4)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_name(substring5)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        with self.assertRaises(StudentException):
            students_service.search_student_by_name(substring6)

    def test_search_student_by_id(self):
        students_repo = StudentRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        substring1 = '    1436'
        substring2 = '436-      '
        substring3 = '-384'
        substring4 = '384        '
        substring5 = '1436-384'
        substring6 = '9999-999'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        list1 = students_service.search_student_by_id(substring1)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_id(substring2)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_id(substring3)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_id(substring4)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        list1 = students_service.search_student_by_id(substring5)
        self.assertEqual(students_service.students.student_list[10].student_id, list1[0])
        with self.assertRaises(StudentException):
            students_service.search_student_by_id(substring6)


class DisciplineServiceTest(unittest.TestCase):

    def test_append_discipline_to_list(self):
        disciplines_repo = DisciplineRepository()
        undo_service = UndoService()
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        list1 = list(disciplines_service.disciplines.discipline_list)

        list1.append('12-43-432 |   Geometry')
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d1)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[10]), list1[10])

        list1.append('65-32-184 |    Algebra')
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d2)
        self.assertNotEqual(str(disciplines_service.disciplines.discipline_list[11]), list1[10])

        list1.append('43-32-454 | Basketball')
        discipline_id = '43-32-454'
        discipline_name = 'Basketball'
        d3 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d3)
        self.assertNotEqual(str(disciplines_service.disciplines.discipline_list[12]), list1[10])
        self.assertNotEqual(str(disciplines_service.disciplines.discipline_list[12]), list1[11])
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[12]), list1[12])

        discipline_id = '43-32-454'
        discipline_name = 'Basketball'
        d4 = Discipline(discipline_id, discipline_name)
        with self.assertRaises(DisciplineException):
            disciplines_service.append_discipline_to_list_with_record(d4)

        discipline_id = '43-32-454'
        discipline_name = 'Football'
        d5 = Discipline(discipline_id, discipline_name)
        with self.assertRaises(DisciplineException):
            disciplines_service.append_discipline_to_list_with_record(d5)

        discipline_id = '54-32-123'
        discipline_name = 'Chemistry'
        d6 = Discipline(discipline_id, discipline_name)
        with self.assertRaises(DisciplineException):
            disciplines_service.append_discipline_to_list_with_record(d6)

        discipline_id = '431232-454'
        discipline_name = 'Magic'
        d4 = Discipline(discipline_id, discipline_name)
        with self.assertRaises(DisciplineException):
            disciplines_service.append_discipline_to_list_with_record(d4)

        discipline_id = '43-12-454'
        discipline_name = '123'
        d4 = Discipline(discipline_id, discipline_name)
        with self.assertRaises(DisciplineException):
            disciplines_service.append_discipline_to_list_with_record(d4)

    def test_remove_discipline_from_list(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)

        discipline_id1 = '12-43-432'
        discipline_name1 = 'Geometry'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)

        discipline_id2 = '65-32-184'
        discipline_name2 = 'Algebra'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)

        discipline_id3 = '43-32-454'
        discipline_name3 = 'Basketball'
        d3 = Discipline(discipline_id3, discipline_name3)
        disciplines_service.append_discipline_to_list(d3)

        disciplines_service.remove_discipline_from_list_with_record(discipline_id3, grades_service)
        self.assertNotEqual(len(disciplines_service.disciplines.discipline_list), 13)
        self.assertEqual(len(disciplines_service.disciplines.discipline_list), 12)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[11]), '65-32-184 |    Algebra')

        disciplines_service.remove_discipline_from_list_with_record(discipline_id2, grades_service)
        self.assertNotEqual(len(disciplines_service.disciplines.discipline_list), 12)
        self.assertEqual(len(disciplines_service.disciplines.discipline_list), 11)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[10]), '12-43-432 |   Geometry')

    def test_update_discipline_name(self):
        disciplines_repo = DisciplineRepository()
        undo_service = UndoService()
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        list1 = list(disciplines_service.disciplines.discipline_list)

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        new_name1 = 'Football'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[10]), '12-41-432 |   Geometry')
        disciplines_service.update_name_discipline_with_record(discipline_id1, new_name1)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[10]), '12-41-432 |   Football')

        discipline_id2 = '65-32-184'
        discipline_name2 = 'Algebra'
        new_name2 = 'Tennis'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[11]), '65-32-184 |    Algebra')
        disciplines_service.update_name_discipline_with_record(discipline_id2, new_name2)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[11]), '65-32-184 |     Tennis')

        list1.append('43-32-454 | Basketball')
        discipline_id3 = '43-32-454'
        discipline_name3 = 'Basketball'
        new_name3 = 'Magic'
        d3 = Discipline(discipline_id3, discipline_name3)
        disciplines_service.append_discipline_to_list(d3)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[12]), '43-32-454 | Basketball')
        disciplines_service.update_name_discipline_with_record(discipline_id3, new_name3)
        self.assertEqual(str(disciplines_service.disciplines.discipline_list[12]), '43-32-454 |      Magic')

    def test_search_discipline_by_name(self):
        disciplines_repo = DisciplineRepository()
        undo_service = UndoService()
        disciplines_service = DisciplineService(disciplines_repo, undo_service)

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        substring1 = '   metry'
        substring2 = 'EtRY'
        substring3 = 'GEOM'
        substring4 = '   GeoMEtRY       '
        substring5 = 'geom'
        substring6 = 'geometryahs'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        list1 = disciplines_service.search_discipline_by_name(substring1)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_name(substring2)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_name(substring3)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_name(substring4)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_name(substring5)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        with self.assertRaises(DisciplineException):
            disciplines_service.search_discipline_by_name(substring6)

    def test_search_discipline_by_id(self):
        disciplines_repo = DisciplineRepository()
        undo_service = UndoService()
        disciplines_service = DisciplineService(disciplines_repo, undo_service)

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        substring1 = '   -41-   '
        substring2 = ' -432   '
        substring3 = '12-41-432'
        substring4 = '12-41    '
        substring5 = '        41-432'
        substring6 = '99-99-999'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        list1 = disciplines_service.search_discipline_by_id(substring1)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_id(substring2)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_id(substring3)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_id(substring4)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        list1 = disciplines_service.search_discipline_by_id(substring5)
        self.assertEqual(disciplines_service.disciplines.discipline_list[10].discipline_id, list1[0])
        with self.assertRaises(DisciplineException):
            disciplines_service.search_discipline_by_id(substring6)


class GradeServiceTest(unittest.TestCase):

    def test_append_grade_to_student(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        list1 = list(grades_service.grades.grade_list)

        list1.append('12-43-432 | 1736-384 |  10')
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s1)
        discipline_id = '12-43-432'
        discipline_name = 'Basketball'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d1)
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        grades_service.append_grade_to_student_with_record(g1)
        self.assertEqual(str(grades_service.grades.grade_list[20]), list1[20])

        list1.append('76-35-274 | 1236-684 |   1')
        student_id = '1236-684'
        student_name = 'Justin Bieber'
        s2 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s2)
        discipline_id = '76-35-274'
        discipline_name = 'Sports'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d2)
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        grades_service.append_grade_to_student_with_record(g2)

        self.assertNotEqual(str(grades_service.grades.grade_list[21]), list1[20])
        self.assertEqual(str(grades_service.grades.grade_list[21]), list1[21])

    def test_remove_grade_from_list_with_student_id(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        list1 = list(grades_service.grades.grade_list)

        list1.append('12-43-432 | 1736-384 |  10')
        student_id1 = '1736-384'
        student_name1 = 'Ariana Grande'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        discipline_id1 = '12-43-432'
        discipline_name1 = 'Basketball'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades_service.append_grade_to_student(g1)

        list1.append('76-35-274 | 1236-684 |   1')
        student_id2 = '1236-684'
        student_name2 = 'Justin Bieber'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list(s2)
        discipline_id2 = '76-35-274'
        discipline_name2 = 'Sports'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        grade_value = 1
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades_service.append_grade_to_student(g2)
        grades_service.remove_grade_from_list_with_student_id(student_id2)

        self.assertEqual(str(grades_service.grades.grade_list[20]), list1[20])
        self.assertEqual(len(grades_service.grades.grade_list), 21)
        self.assertNotEqual(len(grades_service.grades.grade_list), 22)

        grades_service.remove_grade_from_list_with_student_id(student_id1)
        self.assertEqual(len(grades_service.grades.grade_list), 20)
        self.assertNotEqual(len(grades_service.grades.grade_list), 21)

    def test_remove_grade_from_list_with_discipline_id(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        list1 = list(grades_service.grades.grade_list)

        list1.append('12-43-432 | 1736-384 |  10')
        student_id1 = '1736-384'
        student_name1 = 'Ariana Grande'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        discipline_id1 = '12-43-432'
        discipline_name1 = 'Basketball'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        grade_value = 10
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades_service.append_grade_to_student(g1)

        list1.append('76-35-274 | 1236-684 |   1')
        student_id2 = '1236-684'
        student_name2 = 'Justin Bieber'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list(s2)
        discipline_id2 = '76-35-274'
        discipline_name2 = 'Sports'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        grade_value = 1
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades_service.append_grade_to_student(g2)
        grades_service.remove_grade_from_list_with_discipline_id(discipline_id2)

        self.assertEqual(str(grades_service.grades.grade_list[20]), list1[20])
        self.assertEqual(len(grades_service.grades.grade_list), 21)
        self.assertNotEqual(len(grades_service.grades.grade_list), 22)

        grades_service.remove_grade_from_list_with_discipline_id(discipline_id1)
        self.assertEqual(len(grades_service.grades.grade_list), 20)
        self.assertNotEqual(len(grades_service.grades.grade_list), 21)

    def test_calculate_average(self):
        student_repo = StudentRepository()
        discipline_repo = DisciplineRepository()
        grade_repo = GradeRepository()
        undo_service = UndoService()
        student_service = StudentService(student_repo, undo_service, False)
        discipline_service = DisciplineService(discipline_repo, undo_service,  False)
        grade_service = GradeService(discipline_repo, student_repo, grade_repo, undo_service, False)

        self.assertEqual(len(student_service.students), 0)
        self.assertEqual(len(discipline_service.disciplines), 0)
        self.assertEqual(len(grade_service.grades), 0)

        student_service.append_student_to_list(Student('1254-234', 'Harry Potter'))
        student_service.append_student_to_list(Student('5643-245', 'Hermione Granger'))
        student_service.append_student_to_list(Student('7643-234', 'Ron Weasley'))
        student_service.append_student_to_list(Student('9348-124', 'Draco Malfoy'))

        discipline_service.append_discipline_to_list(Discipline('12-43-345', 'Physics'))
        discipline_service.append_discipline_to_list(Discipline('54-34-345', 'Mathematics'))
        discipline_service.append_discipline_to_list(Discipline('54-24-112', 'Chemistry'))
        discipline_service.append_discipline_to_list(Discipline('56-43-115', 'History'))

        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 10))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 9))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 8))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 3))
        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 3))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 8))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 1))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 2))

        result = grade_service.calculate_average()
        self.assertEqual(str(result[0]), '5643-245 |     Hermione Granger | 54-34-345 |          Mathematics | 8.500')
        self.assertEqual(str(result[1]), '1254-234 |         Harry Potter | 12-43-345 |              Physics | 6.500')
        self.assertEqual(str(result[2]), '7643-234 |          Ron Weasley | 54-24-112 |            Chemistry | 4.500')
        self.assertEqual(str(result[3]), '9348-124 |         Draco Malfoy | 56-43-115 |              History | 2.500')
        self.assertEqual(len(result), 4)

    def test_calculate_general_average_for_each_student(self):

        student_repo = StudentRepository()
        discipline_repo = DisciplineRepository()
        grade_repo = GradeRepository()
        undo_service = UndoService()
        student_service = StudentService(student_repo, undo_service, False)
        discipline_service = DisciplineService(discipline_repo, undo_service,  False)
        grade_service = GradeService(discipline_repo, student_repo, grade_repo, undo_service, False)

        self.assertEqual(len(student_service.students), 0)
        self.assertEqual(len(discipline_service.disciplines), 0)
        self.assertEqual(len(grade_service.grades), 0)

        student_service.append_student_to_list(Student('1254-234', 'Harry Potter'))
        student_service.append_student_to_list(Student('5643-245', 'Hermione Granger'))
        student_service.append_student_to_list(Student('7643-234', 'Ron Weasley'))
        student_service.append_student_to_list(Student('9348-124', 'Draco Malfoy'))

        discipline_service.append_discipline_to_list(Discipline('12-43-345', 'Physics'))
        discipline_service.append_discipline_to_list(Discipline('54-34-345', 'Mathematics'))
        discipline_service.append_discipline_to_list(Discipline('54-24-112', 'Chemistry'))
        discipline_service.append_discipline_to_list(Discipline('56-43-115', 'History'))

        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 10))
        grade_service.append_grade_to_student(Grade('54-24-112', '1254-234', 9))
        grade_service.append_grade_to_student(Grade('54-24-112', '1254-234', 3))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 9))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 8))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 3))
        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 3))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 8))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 1))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 2))
        grade_service.append_grade_to_student(Grade('12-43-345', '7643-234', 1))
        grade_service.append_grade_to_student(Grade('12-43-345', '7643-234', 9))

        result = grade_service.calculate_general_average_for_each_student()
        self.assertEqual(str(result[0]), '5643-245 |     Hermione Granger | 8.500')
        self.assertEqual(str(result[1]), '1254-234 |         Harry Potter | 6.250')
        self.assertEqual(str(result[2]), '7643-234 |          Ron Weasley | 4.750')
        self.assertEqual(str(result[3]), '9348-124 |         Draco Malfoy | 2.500')
        self.assertEqual(len(result), 4)

    def test_calculate_average_for_each_discipline(self):
        student_repo = StudentRepository()
        discipline_repo = DisciplineRepository()
        grade_repo = GradeRepository()
        undo_service = UndoService()
        student_service = StudentService(student_repo, undo_service, False)
        discipline_service = DisciplineService(discipline_repo, undo_service,  False)
        grade_service = GradeService(discipline_repo, student_repo, grade_repo, undo_service, False)

        self.assertEqual(len(student_service.students), 0)
        self.assertEqual(len(discipline_service.disciplines), 0)
        self.assertEqual(len(grade_service.grades), 0)

        student_service.append_student_to_list(Student('1254-234', 'Harry Potter'))
        student_service.append_student_to_list(Student('5643-245', 'Hermione Granger'))
        student_service.append_student_to_list(Student('7643-234', 'Ron Weasley'))
        student_service.append_student_to_list(Student('9348-124', 'Draco Malfoy'))

        discipline_service.append_discipline_to_list(Discipline('12-43-345', 'Physics'))
        discipline_service.append_discipline_to_list(Discipline('54-34-345', 'Mathematics'))
        discipline_service.append_discipline_to_list(Discipline('54-24-112', 'Chemistry'))
        discipline_service.append_discipline_to_list(Discipline('56-43-115', 'History'))

        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 10))
        grade_service.append_grade_to_student(Grade('54-24-112', '1254-234', 9))
        grade_service.append_grade_to_student(Grade('54-24-112', '1254-234', 3))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 9))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 8))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 3))
        grade_service.append_grade_to_student(Grade('12-43-345', '1254-234', 3))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 8))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 1))
        grade_service.append_grade_to_student(Grade('54-34-345', '5643-245', 8))
        grade_service.append_grade_to_student(Grade('56-43-115', '9348-124', 2))
        grade_service.append_grade_to_student(Grade('54-24-112', '7643-234', 9))
        grade_service.append_grade_to_student(Grade('12-43-345', '7643-234', 1))
        grade_service.append_grade_to_student(Grade('12-43-345', '7643-234', 9))

        result = grade_service.calculate_average_for_each_discipline()
        self.assertEqual(str(result[0]), '54-34-345 |          Mathematics | 8.333')
        self.assertEqual(str(result[1]), '54-24-112 |            Chemistry | 6.000')
        self.assertEqual(str(result[2]), '12-43-345 |              Physics | 5.750')
        self.assertEqual(str(result[3]), '56-43-115 |              History | 2.500')
        self.assertEqual(len(result), 4)

    def test_reverse_append_grade_to_student(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        students_service = StudentService(students_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        list1 = list(grades_service.grades.grade_list)

        list1.append('12-43-432 | 1736-384 |  10')
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students_service.append_student_to_list_with_record(s1)
        discipline_id = '12-43-432'
        discipline_name = 'Basketball'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list_with_record(d1)
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        grades_service.append_grade_to_student_with_record(g1)
        grades_service.reverse_append_grade_to_student(0)
        self.assertEqual(len(grades_service.grades.grade_list), 20)


class AverageStudentsStatisticTest(unittest.TestCase):

    def test_average_student_statistic(self):
        student_id1 = '1234-244'
        student_name1 = 'Alexandra Bledea'
        discipline_id1 = '12-34-123'
        discipline_name1 = 'Physics'
        average1 = 9

        a1 = AverageStudentsStatistic(student_id1, student_name1, discipline_id1, discipline_name1, average1)
        self.assertEqual(student_id1, a1.student_id_a)
        self.assertEqual(student_name1, a1.student_name_a)
        self.assertEqual(discipline_id1, a1.discipline_id_a)
        self.assertEqual(discipline_name1, a1.discipline_name_a)
        self.assertEqual(average1, a1.average_a)

        student_id2 = '1235-247'
        student_name2 = 'Andreea Orza'
        discipline_id2 = '12-32-543'
        discipline_name2 = 'Romanian'
        average2 = 10

        self.assertNotEqual(student_id2, a1.student_id_a)
        self.assertNotEqual(student_name2, a1.student_name_a)
        self.assertNotEqual(discipline_id2, a1.discipline_id_a)
        self.assertNotEqual(discipline_name2, a1.discipline_name_a)
        self.assertNotEqual(average2, a1.average_a)

    def test_average_student_statistic_string_form(self):
        student_id1 = '1234-244'
        student_name1 = 'Alexandra Bledea'
        discipline_id1 = '12-34-123'
        discipline_name1 = 'Physics'
        average1 = 9

        a1 = AverageStudentsStatistic(student_id1, student_name1, discipline_id1, discipline_name1, average1)
        self.assertEqual(str(a1), '1234-244 |     Alexandra Bledea | 12-34-123 |              Physics | 9.000')


class AverageDisciplineStatisticTest(unittest.TestCase):

    def test_average_discipline_statistic(self):
        discipline_id1 = '12-34-123'
        discipline_name1 = 'Physics'
        average1 = 9
        d1 = AverageDisciplineStatistic(discipline_id1, discipline_name1, average1)
        discipline_id2 = '12-32-543'
        discipline_name2 = 'Romanian'
        average2 = 10
        d2 = AverageDisciplineStatistic(discipline_id2, discipline_name2, average2)

        self.assertEqual(discipline_id1, d1.discipline_id_a)
        self.assertEqual(discipline_name1, d1.discipline_name_a)
        self.assertEqual(average1, d1.average_a)

        self.assertEqual(discipline_id2, d2.discipline_id_a)
        self.assertEqual(discipline_name2, d2.discipline_name_a)
        self.assertEqual(average2, d2.average_a)

    def test_average_discipline_statistic_string_form(self):
        discipline_id1 = '12-34-123'
        discipline_name1 = 'Physics'
        average1 = 9
        d1 = AverageDisciplineStatistic(discipline_id1, discipline_name1, average1)
        self.assertEqual(str(d1), '12-34-123 |              Physics | 9.000')

        discipline_id2 = '12-32-543'
        discipline_name2 = 'Romanian'
        average2 = 10
        d2 = AverageDisciplineStatistic(discipline_id2, discipline_name2, average2)
        self.assertEqual(str(d2), '12-32-543 |             Romanian | 10.000')


class GeneralAverageStudentsStatisticTest(unittest.TestCase):

    def test_general_average_students_statistic(self):
        student_id1 = '1234-244'
        student_name1 = 'Alexandra Bledea'
        average1 = 9
        s1 = GeneralAverageStudentsStatistic(student_id1, student_name1, average1)

        student_id2 = '1235-247'
        student_name2 = 'Harry Potter'
        average2 = 'English'
        s2 = GeneralAverageStudentsStatistic(student_id2, student_name2, average2)

        self.assertEqual(student_id1, s1.student_id_ga)
        self.assertEqual(student_name1, s1.student_name_ga)
        self.assertEqual(average1, s1.average_ga)

        self.assertEqual(student_id2, s2.student_id_ga)
        self.assertEqual(student_name2, s2.student_name_ga)
        self.assertEqual(average2, s2.average_ga)

    def test_general_average_students_statistic_string_form(self):
        student_id1 = '1234-244'
        student_name1 = 'Alexandra Bledea'
        average1 = 9
        s1 = GeneralAverageStudentsStatistic(student_id1, student_name1, average1)

        student_id2 = '1235-247'
        student_name2 = 'Harry Potter'
        average2 = 10
        s2 = GeneralAverageStudentsStatistic(student_id2, student_name2, average2)

        self.assertEqual(str(s1), '1234-244 |     Alexandra Bledea | 9.000')
        self.assertEqual(str(s2), '1235-247 |         Harry Potter | 10.000')


class UndoExceptionTest(unittest.TestCase):

    def test_undo_exception(self):
        undo_exception = UndoException("There is no operation to undo!")
        self.assertEqual(str(undo_exception), "There is no operation to undo!")


class UndoServiceTest(unittest.TestCase):

    def test_undo_redo(self):
        students_repo = StudentRepository()
        disciplines_repo = DisciplineRepository()
        grades_repo = GradeRepository()
        undo_service = UndoService()
        grades_service = GradeService(disciplines_repo, students_repo, grades_repo, undo_service)
        disciplines_service = DisciplineService(disciplines_repo, undo_service)

        discipline_id1 = '12-43-432'
        discipline_name1 = 'Geometry'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)

        disciplines_service.remove_discipline_from_list_with_record(discipline_id1, grades_service)
        undo_service.undo()
        with self.assertRaises(UndoException):
            undo_service.undo()
        undo_service.redo()
        with self.assertRaises(UndoException):
            undo_service.redo()

