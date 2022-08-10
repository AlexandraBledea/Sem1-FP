"""
We implement the class for each list's entity
"""
from src.Domain.entity import Student, Discipline, Grade


class StudentRepository:

    def __init__(self):
        self._student_list = []

    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, new_student_list):
        self._student_list = list(new_student_list)

    def add_student_to_list(self, student):
        """
        With this function we add another student to the list
        :param student: the new student
        :return: it doesn't return anything
        """
        self.student_list.append(student)

    def delete_student_from_list(self, index):
        """
        With this function we delete a student from the list at a specified position
        :param index: represents the position of the student in list
        :return: it doesn't return anything
        """
        del self.student_list[index]

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.student_list)

    def __getitem__(self, item):
        return self.student_list[item]


class DisciplineRepository:

    def __init__(self):
        self._discipline_list = []

    @property
    def discipline_list(self):
        return self._discipline_list

    @discipline_list.setter
    def discipline_list(self, new_discipline_list):
        self._discipline_list = list(new_discipline_list)

    def add_discipline_to_list(self, discipline):
        """
        With this function we add another discipline to the list
        :param discipline: the new discipline
        :return: it doesn't return anything
        """
        self.discipline_list.append(discipline)

    def delete_discipline_from_list(self, index):
        """
        With this function we delete a discipline from the list at a specified position
        :param index: represents the position of the discipline in list
        :return: it doesn't return anything
        """
        del self.discipline_list[index]

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.discipline_list)

    def __getitem__(self, item):
        return self.discipline_list[item]


class GradeRepository:

    def __init__(self):
        self._grade_list = []

    @property
    def grade_list(self):
        return self._grade_list

    @grade_list.setter
    def grade_list(self, new_grade_list):
        self._grade_list = list(new_grade_list)

    def add_grade_to_list(self, grade):
        """
        With this function we add another grade for a student at a specific discipline
        :param grade: it's represents the grade which is going to be added
        :return: it doesn't return anything
        """
        self.grade_list.append(grade)

    def delete_grade_from_list(self, index):
        """
        With this function we delete a grade from the list at a specified position
        :param index: represents the position of the grade in list
        :return: it doesn't return anything
        """
        del self.grade_list[index]

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.grade_list)


class TestRepositoryFunctions:

    @staticmethod
    def test_add_student():
        list1 = []
        students = StudentRepository()

        list1.append('1436-384 |   Ariana Grande')
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students.add_student_to_list(s1)
        assert str(students.student_list[0]) == list1[0]

        list1.append('1736-384 |      Mike Perry')
        student_id = '1736-384'
        student_name = 'Mike Perry'
        s2 = Student(student_id, student_name)
        students.add_student_to_list(s2)
        assert str(students.student_list[1]) != list1[0]
        assert str(students.student_list[1]) == list1[1]

        list1.append('1627-478 |    Selena Gomez')
        student_id = '1627-478'
        student_name = 'Selena Gomez'
        s3 = Student(student_id, student_name)
        students.add_student_to_list(s3)
        assert str(students.student_list[2]) != list1[0]
        assert str(students.student_list[2]) != list1[1]
        assert str(students.student_list[2]) == list1[2]

        list1.append('1457-473 |   Martin Garrix')
        student_id = '1457-473'
        student_name = 'Martin Garrix'
        s4 = Student(student_id, student_name)
        students.add_student_to_list(s4)
        assert str(students.student_list[3]) != list1[0]
        assert str(students.student_list[3]) != list1[1]
        assert str(students.student_list[3]) != list1[2]
        assert str(students.student_list[3]) == list1[3]

    @staticmethod
    def test_delete_student_from_list():
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
        assert len(students.student_list) != 4
        assert len(students.student_list) == 3
        assert str(students.student_list[2]) == '1627-478 |    Selena Gomez'

        students.delete_student_from_list(2)
        assert len(students.student_list) != 3
        assert len(students.student_list) == 2
        assert str(students.student_list[1]) == '1736-384 |      Mike Perry'

        students.delete_student_from_list(1)
        assert len(students.student_list) != 2
        assert len(students.student_list) == 1
        assert str(students.student_list[0]) == '1436-384 |   Ariana Grande'

        students.delete_student_from_list(0)
        assert len(students.student_list) != 1
        assert len(students.student_list) == 0

    @staticmethod
    def test_add_discipline():
        list1 = []
        disciplines = DisciplineRepository()

        list1.append('12-43-432 |   Geometry')
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d1)
        assert str(disciplines.discipline_list[0]) == list1[0]

        list1.append('65-32-184 |    Algebra')
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d2)
        assert str(disciplines.discipline_list[1]) != list1[0]
        assert str(disciplines.discipline_list[1]) == list1[1]

        list1.append('43-32-454 |  Chemistry')
        discipline_id = '43-32-454'
        discipline_name = 'Chemistry'
        d3 = Discipline(discipline_id, discipline_name)
        disciplines.add_discipline_to_list(d3)
        assert str(disciplines.discipline_list[2]) != list1[0]
        assert str(disciplines.discipline_list[2]) != list1[1]
        assert str(disciplines.discipline_list[2]) == list1[2]


    @staticmethod
    def test_delete_discipline_from_list():
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
        assert len(disciplines.discipline_list) != 3
        assert len(disciplines.discipline_list) == 2
        assert str(disciplines.discipline_list[1]) == '65-32-184 |    Algebra'

        disciplines.delete_discipline_from_list(1)
        assert len(disciplines.discipline_list) != 2
        assert len(disciplines.discipline_list) == 1
        assert str(disciplines.discipline_list[0]) == '12-43-432 |   Geometry'

        disciplines.delete_discipline_from_list(0)
        assert len(disciplines.discipline_list) != 1
        assert len(disciplines.discipline_list) == 0

    @staticmethod
    def test_add_grade():
        list1 = []
        grades = GradeRepository()

        list1.append('12-43-432 | 1736-384 |  10')
        student_id = '1736-384'
        discipline_id = '12-43-432'
        grade_value = 10
        g1 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g1)
        assert str(grades.grade_list[0]) == list1[0]

        list1.append('76-35-274 | 1236-684 |   1')
        student_id = '1236-684'
        discipline_id = '76-35-274'
        grade_value = 1
        g2 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g2)
        assert str(grades.grade_list[1]) != list1[0]
        assert str(grades.grade_list[1]) == list1[1]

        list1.append('72-09-164 | 2156-856 |   7')
        student_id = '2156-856'
        discipline_id = '72-09-164'
        grade_value = 7
        g3 = Grade(discipline_id, student_id, grade_value)
        grades.add_grade_to_list(g3)
        assert str(grades.grade_list[2]) != list1[0]
        assert str(grades.grade_list[2]) != list1[1]
        assert str(grades.grade_list[2]) == list1[2]

    @staticmethod
    def test_delete_grade_from_list():
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
        assert len(grades.grade_list) != 3
        assert len(grades.grade_list) == 2
        assert str(grades.grade_list[1]) == '76-35-274 | 1236-684 |   1'

        grades.delete_grade_from_list(1)
        assert len(grades.grade_list) != 2
        assert len(grades.grade_list) == 1
        assert str(grades.grade_list[0]) == '12-43-432 | 1736-384 |  10'

        grades.delete_grade_from_list(0)
        assert len(grades.grade_list) != 1
        assert len(grades.grade_list) == 0

    @staticmethod
    def run_all_tests():
        TestRepositoryFunctions.test_add_student()
        TestRepositoryFunctions.test_add_discipline()
        TestRepositoryFunctions.test_add_grade()
        TestRepositoryFunctions.test_delete_student_from_list()
        TestRepositoryFunctions.test_delete_discipline_from_list()
        TestRepositoryFunctions.test_delete_grade_from_list()


TestRepositoryFunctions.run_all_tests()
