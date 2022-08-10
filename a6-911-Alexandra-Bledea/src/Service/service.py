"""
We implement the class for the service
"""
from src.Domain.entity import Student, Discipline, Grade, StudentException, DisciplineException
from src.Repository.repository import StudentRepository, DisciplineRepository, GradeRepository
from src.Validation.validate import StudentValidation, DisciplineValidation, GradeValidation
import random
import re


class StudentService:

    def __init__(self):
        self.students = StudentRepository()
        self.generate_random_student()

    def append_student_to_list(self, student):
        """
        With this function, first we check if the student's data is valid and if it is we add it to the list
        :param student: the new student we want to add
        :return: it doesn't return anything
        """
        StudentValidation.validate_student_id(student.student_id)
        StudentValidation.validate_student_name(student.student_name)
        StudentValidation.check_duplicate_id_student(student.student_id, self.students.student_list)
        self.students.add_student_to_list(student)

    def remove_student_from_list(self, student_id):
        """
        With this function we firstly check if the student id given is valid, if it is valid and exits we delete it form
        the students list
        :param student_id: Represents the id for the student we want to remove
        :return: it doesn't return anything
        """
        StudentValidation.validate_student_id(student_id)
        StudentValidation.check_existence_of_student_id(student_id, self.students.student_list)
        i = 0
        while i < len(self.students.student_list):
            s = self.students.student_list[i]
            if s.student_id == student_id:
                self.students.delete_student_from_list(i)
            else:
                i = i + 1

    def generate_random_student(self, cont=10):
        """
        :param cont: it represents how many students we want to random generate
        :return: it doesn't return anything
        """
        done = False
        i = 0
        unique_id_students = ['1433-421', '4325-423', '9836-645', '2451-524', '2451-534', '1231-432', '6473-826',
                              '1682-262', '2519-262', '9982-112']
        students_names = ['Harry Potter', 'Hermione Granger', 'Ron Weasley', 'Luna Lovegood', 'Lord Voldemort',
                          'Ginny Weasley', 'Neville LongBottom', 'Draco Malfoy', 'Fred Weasley', 'George Weasley']
        while not done:
            try:
                while i <= cont:
                    student_id = random.choice(unique_id_students)
                    student_name = random.choice(students_names)
                    self.append_student_to_list(Student(student_id, student_name))
                    i = i + 1
            except StudentException:
                if len(self.students.student_list) != 10:
                    cont = cont + 1
                else:
                    done = True

    def update_student_name(self, student_id, new_name):
        """
        With this function if the conditions are checked we update a student's name with a new one
        :param student_id: the id of the student for which we want to update the name
        :param new_name: the new name we want to give to the specified student
        :return: it doesn't return anything
        """
        StudentValidation.validate_student_id(student_id)
        StudentValidation.validate_student_name(new_name)
        StudentValidation.check_existence_of_student_id(student_id, self.students.student_list)
        for s in self.students.student_list:
            if s.student_id == student_id:
                s.student_name = new_name

    def search_student_by_name(self, name):
        """
        With this function we check if a given substring is part of the name of any student
        :param name: the substring given
        :return: the list of student's ids
        """
        existent = False
        student_id_list = []
        for student in self.students.student_list:
            if re.search(name.lower().strip(), student.student_name.lower()):
                student_id_list.append(student.student_id)
                existent = True
        if not existent:
            raise StudentException("There is no existing student which contains the substring given!")
        else:
            return student_id_list

    def search_student_by_id(self, student_id):
        """
        With this funcion we check if a given substring is part of the id of any student
        :param student_id: the substring given
        :return: the list of student's ids
        """
        existent = False
        student_id_list = []
        for student in self.students.student_list:
            if re.search(student_id.strip(), student.student_id):
                student_id_list.append(student.student_id)
                existent = True
        if not existent:
            raise StudentException("There is no existing student with the provided id!")
        else:
            return student_id_list


class DisciplineService:

    def __init__(self):
        self.disciplines = DisciplineRepository()
        self.generate_random_discipline()

    def append_discipline_to_list(self, discipline):
        """
        With this function firstly we check is the discipline's data is valid and if it is then we add it to the list
        :param discipline: the new discipline we want to add
        :return: it doesn't return anything
        """
        DisciplineValidation.validate_discipline_id(discipline.discipline_id)
        DisciplineValidation.validate_discipline_name(discipline.discipline_name)
        DisciplineValidation.check_duplicate_id_discipline(discipline.discipline_id, self.disciplines.discipline_list)
        DisciplineValidation.check_duplicate_name_discipline(discipline.discipline_name,
                                                             self.disciplines.discipline_list)
        self.disciplines.add_discipline_to_list(discipline)

    def remove_discipline_from_list(self, discipline_id):
        """
        With this function we firstly check if the discipline id given is valid, if it is valid and exits we delete
         it form the disciplines list
        :param discipline_id: Represents the id for the discipline we want to remove
        :return: it doesn't return anything
        """
        DisciplineValidation.validate_discipline_id(discipline_id)
        DisciplineValidation.check_existence_of_discipline_id(discipline_id, self.disciplines.discipline_list)
        i = 0
        while i < len(self.disciplines.discipline_list):
            d = self.disciplines.discipline_list[i]
            if d.discipline_id == discipline_id:
                self.disciplines.delete_discipline_from_list(i)
            else:
                i = i + 1

    def generate_random_discipline(self, cont=10):
        """
        :param cont: represents how many disciplines we want to random generate
        :return: it doesn't return anything
        """
        done = False
        i = 0
        unique_id_disciplines = ['12-34-123', '42-23-327', '47-23-847', '21-76-298', '12-98-327', '03-24-473',
                                 '78-12-324', '12-43-436', '98-11-274', '23-11-293']
        disciplines_names = ['Mathematics', 'English', 'Chemistry', 'Physics', 'Geography', 'History', 'Informatics',
                             'Psychology', 'Biology', 'Philosophy']
        while not done:
            try:
                while i <= cont:
                    discipline_id = random.choice(unique_id_disciplines)
                    discipline_name = random.choice(disciplines_names)
                    self.append_discipline_to_list(Discipline(discipline_id, discipline_name))
                    i = i + 1
            except DisciplineException:
                if len(self.disciplines.discipline_list) != 10:
                    cont = cont + 1
                else:
                    done = True

    def update_name_discipline(self, discipline_id, new_name):
        """
        With this function, if all the conditions are checked we update the specified discipline's name with the new one
        :param discipline_id: the id of the discipline for which we want to change the name
        :param new_name: the new name we want to give to the specified discipline
        :return: it doesn't return anything
        """

        DisciplineValidation.validate_discipline_id(discipline_id)
        DisciplineValidation.validate_discipline_name(new_name)
        DisciplineValidation.check_duplicate_name_discipline(new_name, self.disciplines.discipline_list)
        DisciplineValidation.check_existence_of_discipline_id(discipline_id, self.disciplines.discipline_list)
        for d in self.disciplines.discipline_list:
            if d.discipline_id == discipline_id:
                d.discipline_name = new_name

    def search_discipline_by_name(self, name):
        """
        With this function we check if a given substring is part of the name of any discipline
        :param name: the given substring
        :return: it returns the list of disciplines ids if the conditions are checked
        """
        existent = False
        discipline_id_list = []
        for discipline in self.disciplines.discipline_list:
            if re.search(name.lower().strip(), discipline.discipline_name.lower()):
                discipline_id_list.append(discipline.discipline_id)
                existent = True
        if not existent:
            raise DisciplineException("There is no existing discipline which contains the substring given!")
        else:
            return discipline_id_list

    def search_discipline_by_id(self, discipline_id):
        """
        With this function we check if a given substring is part of the id of any student
        :param discipline_id: the given substring
        :return: it returns the list of disciplines ids if the conditions are checked
        """
        existent = False
        discipline_id_list = []
        for discipline in self.disciplines.discipline_list:
            if re.search(discipline_id.strip(), discipline.discipline_id):
                discipline_id_list.append(discipline.discipline_id)
                existent = True
        if not existent:
            raise DisciplineException("There is no existing discipline with the provided id")
        else:
            return discipline_id_list


class GradeService:

    def __init__(self):
        self.grades = GradeRepository()
        self.generate_random_grades()

    def append_grade_to_student(self, grade, student_list, discipline_list):
        """
        With this function we firstly check if the discipline_id and the student_id for which the grade is added
        do already exist. If not an error will be raised, otherwise we add that grade to the list
        :param grade: represents the new grade we want to add to the list
        :param student_list: represents the list of all the students
        :param discipline_list: represents the list of all the disciplines
        :return: it doesn't return anything
        """
        DisciplineValidation.validate_discipline_id(grade.discipline_id_g)
        StudentValidation.validate_student_id(grade.student_id_g)
        GradeValidation.validate_grade_value(grade.grade_value)
        DisciplineValidation.check_existence_of_discipline_id(grade.discipline_id_g, discipline_list)
        StudentValidation.check_existence_of_student_id(grade.student_id_g, student_list)
        self.grades.add_grade_to_list(grade)

    def remove_grade_from_list_with_student_id(self, student_id):
        """
        With this function we delete all the grades which are related to a student
        :param student_id: Represents the id of the student for which we want to remove the grades
        :return: it doesn't return anything
        """
        GradeValidation.check_existence_of_grade_student(student_id, self.grades.grade_list)
        i = 0
        while i < len(self.grades.grade_list):
            g = self.grades.grade_list[i]
            if g.student_id_g == student_id:
                self.grades.delete_grade_from_list(i)
            else:
                i = i + 1

    def remove_grade_from_list_with_discipline_id(self, discipline_id):
        """
        With this function we delete all the grades which are related to a discipline
        :param discipline_id: Represents the id of the discipline for which we want to remove the grades
        :return: it doesn't return anything
        """
        GradeValidation.check_the_existence_of_grade_discipline(discipline_id, self.grades.grade_list)
        i = 0
        while i < len(self.grades.grade_list):
            g = self.grades.grade_list[i]
            if g.discipline_id_g == discipline_id:
                self.grades.delete_grade_from_list(i)
            else:
                i = i + 1

    def generate_random_grades(self, cont=20):
        """
        :param cont: represents the number of random grades we want to generate
        :return:it doesn't return anything
        """
        student_service = StudentService()
        discipline_service = DisciplineService()
        for i in range(0, cont):
            self.grades.add_grade_to_list(Grade(discipline_service.disciplines.discipline_list[random.randint(0, 9)].
                                          discipline_id, student_service.students.student_list[random.
                                          randint(0, 9)].student_id, random.randint(1, 10)))

    '''
    def statistic_students_who_failed(self, student_list, discipline_list):
        sum_of_grades = 0
        number_of_grades = 0
        i = 0
        while i < len(student_list):
            for discipline in discipline_list:
                for grade in self.grades.grade_list:
                    if grade.student_id_g == student.student_id:
                        sum_of_grades = sum_of_grades + grade.grade_value
                        number_of_grades = number_of_grades + 1
        pass
    '''

class TestService:

    @staticmethod
    def test_append_student_to_list():
        students_service = StudentService()

        list1 = list(students_service.students.student_list)

        list1.append('1436-384 |   Ariana Grande')
        student_id = '1436-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students_service.append_student_to_list(s1)
        assert str(students_service.students.student_list[10]) == list1[10]

        list1.append('1736-384 |      Mike Perry')
        student_id = '1736-384'
        student_name = 'Mike Perry'
        s2 = Student(student_id, student_name)
        students_service.append_student_to_list(s2)
        assert str(students_service.students.student_list[11]) != list1[10]
        assert str(students_service.students.student_list[11]) == list1[11]

        list1.append('1627-478 |    Selena Gomez')
        student_id = '1627-478'
        student_name = 'Selena Gomez'
        s3 = Student(student_id, student_name)
        students_service.append_student_to_list(s3)
        assert str(students_service.students.student_list[12]) != list1[10]
        assert str(students_service.students.student_list[12]) != list1[11]
        assert str(students_service.students.student_list[12]) == list1[12]

        list1.append('1457-473 |   Martin Garrix')
        student_id = '1457-473'
        student_name = 'Martin Garrix'
        s4 = Student(student_id, student_name)
        students_service.append_student_to_list(s4)
        assert str(students_service.students.student_list[13]) != list1[10]
        assert str(students_service.students.student_list[13]) != list1[11]
        assert str(students_service.students.student_list[13]) != list1[12]
        assert str(students_service.students.student_list[13]) == list1[13]

        '''
        Optional for the case with duplicate id!!!
        '''

        '''
        student_id = '1457-473'
        student_name = 'Dua Lipa'
        s5 = Student(student_id, student_name)

        try:
            students_service.append_student_to_list(s5)
        except StudentException as se:
            print(se)
            print()

        student_id = 'sfaghja'
        student_name = 'Dua Lipa'
        s6 = Student(student_id, student_name)

        try:
            students_service.append_student_to_list(s6)
        except StudentException as se:
            print(se)
            print()

        student_id = '1234-213'
        student_name = 'Andreea'
        s7 = Student(student_id, student_name)

        try:
            students_service.append_student_to_list(s7)
        except StudentException as se:
            print(se)
            print()

        student_id = '1234-213'
        student_name = ''
        s8 = Student(student_id, student_name)

        try:
            students_service.append_student_to_list(s8)
        except StudentException as se:
            print(se)
            print()
        '''

    @staticmethod
    def test_remove_student_from_list():
        students_service = StudentService()

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)

        student_id2 = '1736-384'
        student_name2 = 'Mike Perry'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list(s2)

        student_id3 = '1627-478'
        student_name3 = 'Selena Gomez'
        s3 = Student(student_id3, student_name3)
        students_service.append_student_to_list(s3)

        student_id4 = '1457-473'
        student_name4 = 'Martin Garrix'
        s4 = Student(student_id4, student_name4)
        students_service.append_student_to_list(s4)

        students_service.remove_student_from_list(student_id4)
        assert len(students_service.students.student_list) != 14
        assert len(students_service.students.student_list) == 13
        assert str(students_service.students.student_list[12]) == '1627-478 |    Selena Gomez'

        students_service.remove_student_from_list(student_id3)
        assert len(students_service.students.student_list) != 13
        assert len(students_service.students.student_list) == 12
        assert str(students_service.students.student_list[11]) == '1736-384 |      Mike Perry'

        students_service.remove_student_from_list(student_id2)
        assert len(students_service.students.student_list) != 12
        assert len(students_service.students.student_list) == 11
        assert str(students_service.students.student_list[10]) == '1436-384 |   Ariana Grande'

    @staticmethod
    def test_append_discipline_to_list():

        disciplines_service = DisciplineService()
        list1 = list(disciplines_service.disciplines.discipline_list)

        list1.append('12-43-432 |   Geometry')
        discipline_id = '12-43-432'
        discipline_name = 'Geometry'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list(d1)
        assert str(disciplines_service.disciplines.discipline_list[10]) == list1[10]

        list1.append('65-32-184 |    Algebra')
        discipline_id = '65-32-184'
        discipline_name = 'Algebra'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list(d2)
        assert str(disciplines_service.disciplines.discipline_list[11]) != list1[10]
        assert str(disciplines_service.disciplines.discipline_list[11]) == list1[11]

        list1.append('43-32-454 | Basketball')
        discipline_id = '43-32-454'
        discipline_name = 'Basketball'
        d3 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list(d3)
        assert str(disciplines_service.disciplines.discipline_list[12]) != list1[10]
        assert str(disciplines_service.disciplines.discipline_list[12]) != list1[11]
        assert str(disciplines_service.disciplines.discipline_list[12]) == list1[12]

        '''
        Optional for the case with duplicate id and name, only duplicate id or only duplicate name!!!
        '''

        '''
        discipline_id = '43-32-454'
        discipline_name = 'Basketball'
        d4 = Discipline(discipline_id, discipline_name)
        try:
            disciplines_service.append_discipline_to_list(d4)
        except DisciplineException as de:
            print(de)
            print()

        discipline_id = '43-32-454'
        discipline_name = 'Football'
        d5 = Discipline(discipline_id, discipline_name)
        try:
            disciplines_service.append_discipline_to_list(d5)
        except DisciplineException as de:
            print(de)
            print()

        discipline_id = '54-32-123'
        discipline_name = 'Chemistry'
        d6 = Discipline(discipline_id, discipline_name)
        try:
            disciplines_service.append_discipline_to_list(d6)
        except DisciplineException as de:
            print(de)
            print()

        discipline_id = '431232-454'
        discipline_name = 'Magic'
        d4 = Discipline(discipline_id, discipline_name)
        try:
            disciplines_service.append_discipline_to_list(d4)
        except DisciplineException as de:
            print(de)
            print()

        discipline_id = '43-12-454'
        discipline_name = '123'
        d4 = Discipline(discipline_id, discipline_name)
        try:
            disciplines_service.append_discipline_to_list(d4)
        except DisciplineException as de:
            print(de)
            print()
        '''

    @staticmethod
    def test_remove_discipline_from_list():
        disciplines_service = DisciplineService()

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

        disciplines_service.remove_discipline_from_list(discipline_id3)
        assert len(disciplines_service.disciplines.discipline_list) != 13
        assert len(disciplines_service.disciplines.discipline_list) == 12
        assert str(disciplines_service.disciplines.discipline_list[11]) == '65-32-184 |    Algebra'

        disciplines_service.remove_discipline_from_list(discipline_id2)
        assert len(disciplines_service.disciplines.discipline_list) != 12
        assert len(disciplines_service.disciplines.discipline_list) == 11
        assert str(disciplines_service.disciplines.discipline_list[10]) == '12-43-432 |   Geometry'

    @staticmethod
    def test_append_grade_to_student():
        students_service = StudentService()
        disciplines_service = DisciplineService()
        grades_service = GradeService()
        list1 = list(grades_service.grades.grade_list)

        list1.append('12-43-432 | 1736-384 |  10')
        student_id = '1736-384'
        student_name = 'Ariana Grande'
        s1 = Student(student_id, student_name)
        students_service.append_student_to_list(s1)
        discipline_id = '12-43-432'
        discipline_name = 'Basketball'
        d1 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list(d1)
        grade_value = '10'
        g1 = Grade(discipline_id, student_id, grade_value)
        grades_service.append_grade_to_student(g1, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)
        assert str(grades_service.grades.grade_list[20]) == list1[20]

        list1.append('76-35-274 | 1236-684 |   1')
        student_id = '1236-684'
        student_name = 'Justin Bieber'
        s2 = Student(student_id, student_name)
        students_service.append_student_to_list(s2)
        discipline_id = '76-35-274'
        discipline_name = 'Sports'
        d2 = Discipline(discipline_id, discipline_name)
        disciplines_service.append_discipline_to_list(d2)
        grade_value = '1'
        g2 = Grade(discipline_id, student_id, grade_value)
        grades_service.append_grade_to_student(g2, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)
        assert str(grades_service.grades.grade_list[21]) != list1[20]
        assert str(grades_service.grades.grade_list[21]) == list1[21]

    @staticmethod
    def test_remove_grade_from_list_with_student_id():
        students_service = StudentService()
        disciplines_service = DisciplineService()
        grades_service = GradeService()
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
        grade_value = '10'
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades_service.append_grade_to_student(g1, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)

        list1.append('76-35-274 | 1236-684 |   1')
        student_id2 = '1236-684'
        student_name2 = 'Justin Bieber'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list(s2)
        discipline_id2 = '76-35-274'
        discipline_name2 = 'Sports'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        grade_value = '1'
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades_service.append_grade_to_student(g2, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)
        grades_service.remove_grade_from_list_with_student_id(student_id2)
        assert str(grades_service.grades.grade_list[20]) == list1[20]
        assert len(grades_service.grades.grade_list) == 21
        assert len(grades_service.grades.grade_list) != 22

        grades_service.remove_grade_from_list_with_student_id(student_id1)
        assert len(grades_service.grades.grade_list) == 20
        assert len(grades_service.grades.grade_list) != 21

    @staticmethod
    def test_remove_grade_from_list_with_discipline_id():
        students_service = StudentService()
        disciplines_service = DisciplineService()
        grades_service = GradeService()
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
        grade_value = '10'
        g1 = Grade(discipline_id1, student_id1, grade_value)
        grades_service.append_grade_to_student(g1, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)

        list1.append('76-35-274 | 1236-684 |   1')
        student_id2 = '1236-684'
        student_name2 = 'Justin Bieber'
        s2 = Student(student_id2, student_name2)
        students_service.append_student_to_list(s2)
        discipline_id2 = '76-35-274'
        discipline_name2 = 'Sports'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        grade_value = '1'
        g2 = Grade(discipline_id2, student_id2, grade_value)
        grades_service.append_grade_to_student(g2, students_service.students.student_list, disciplines_service.
                                               disciplines.discipline_list)
        grades_service.remove_grade_from_list_with_discipline_id(discipline_id2)
        assert str(grades_service.grades.grade_list[20]) == list1[20]
        assert len(grades_service.grades.grade_list) == 21
        assert len(grades_service.grades.grade_list) != 22

        grades_service.remove_grade_from_list_with_discipline_id(discipline_id1)
        assert len(grades_service.grades.grade_list) == 20
        assert len(grades_service.grades.grade_list) != 21

    @staticmethod
    def test_update_student_name():

        students_service = StudentService()

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        new_name1 = 'Justin Bieber'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        assert str(students_service.students.student_list[10]) == '1436-384 |   Ariana Grande'
        students_service.update_student_name(student_id1, new_name1)
        assert str(students_service.students.student_list[10]) == '1436-384 |   Justin Bieber'

        student_id2 = '1736-384'
        student_name2 = 'Mike Perry'
        s2 = Student(student_id2, student_name2)
        new_name2 = 'Ariana Grande'
        students_service.append_student_to_list(s2)
        assert str(students_service.students.student_list[11]) == '1736-384 |      Mike Perry'
        students_service.update_student_name(student_id2, new_name2)
        assert str(students_service.students.student_list[11]) == '1736-384 |   Ariana Grande'

        student_id3 = '1627-478'
        student_name3 = 'Selena Gomez'
        new_name3 = 'Martin Garrix'
        s3 = Student(student_id3, student_name3)
        students_service.append_student_to_list(s3)
        assert str(students_service.students.student_list[12]) == '1627-478 |    Selena Gomez'
        students_service.update_student_name(student_id3, new_name3)
        assert str(students_service.students.student_list[12]) == '1627-478 |   Martin Garrix'

    @staticmethod
    def test_update_discipline_name():

        disciplines_service = DisciplineService()
        list1 = list(disciplines_service.disciplines.discipline_list)

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        new_name1 = 'Football'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        assert str(disciplines_service.disciplines.discipline_list[10]) == '12-41-432 |   Geometry'
        disciplines_service.update_name_discipline(discipline_id1, new_name1)
        assert str(disciplines_service.disciplines.discipline_list[10]) == '12-41-432 |   Football'

        discipline_id2 = '65-32-184'
        discipline_name2 = 'Algebra'
        new_name2 = 'Tennis'
        d2 = Discipline(discipline_id2, discipline_name2)
        disciplines_service.append_discipline_to_list(d2)
        assert str(disciplines_service.disciplines.discipline_list[11]) == '65-32-184 |    Algebra'
        disciplines_service.update_name_discipline(discipline_id2, new_name2)
        assert str(disciplines_service.disciplines.discipline_list[11]) == '65-32-184 |     Tennis'

        list1.append('43-32-454 | Basketball')
        discipline_id3 = '43-32-454'
        discipline_name3 = 'Basketball'
        new_name3 = 'Magic'
        d3 = Discipline(discipline_id3, discipline_name3)
        disciplines_service.append_discipline_to_list(d3)
        assert str(disciplines_service.disciplines.discipline_list[12]) == '43-32-454 | Basketball'
        disciplines_service.update_name_discipline(discipline_id3, new_name3)
        assert str(disciplines_service.disciplines.discipline_list[12]) == '43-32-454 |      Magic'

    @staticmethod
    def test_search_student_by_name():
        students_service = StudentService()

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        substring1 = 'Ari'
        substring2 = 'GranD'
        substring3 = 'Ariana '
        substring4 = ' Grande'
        substring5 = 'ArIaNA'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        list1 = students_service.search_student_by_name(substring1)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_name(substring2)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_name(substring3)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_name(substring4)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_name(substring5)
        assert students_service.students.student_list[10].student_id == list1[0]

    @staticmethod
    def test_search_student_by_id():
        students_service = StudentService()

        student_id1 = '1436-384'
        student_name1 = 'Ariana Grande'
        substring1 = '    1436'
        substring2 = '436-      '
        substring3 = '-384'
        substring4 = '384        '
        substring5 = '1436-384'
        s1 = Student(student_id1, student_name1)
        students_service.append_student_to_list(s1)
        list1 = students_service.search_student_by_id(substring1)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_id(substring2)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_id(substring3)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_id(substring4)
        assert students_service.students.student_list[10].student_id == list1[0]
        list1 = students_service.search_student_by_id(substring5)
        assert students_service.students.student_list[10].student_id == list1[0]

    @staticmethod
    def test_search_discipline_by_name():
        disciplines_service = DisciplineService()

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        substring1 = '   metry'
        substring2 = 'EtRY'
        substring3 = 'GEOM'
        substring4 = '   GeoMEtRY       '
        substring5 = 'geom'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        list1 = disciplines_service.search_discipline_by_name(substring1)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_name(substring2)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_name(substring3)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_name(substring4)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_name(substring5)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]

    @staticmethod
    def test_search_discipline_by_id():
        disciplines_service = DisciplineService()

        discipline_id1 = '12-41-432'
        discipline_name1 = 'Geometry'
        substring1 = '   -41-   '
        substring2 = ' -432   '
        substring3 = '12-41-432'
        substring4 = '12-41    '
        substring5 = '        41-432'
        d1 = Discipline(discipline_id1, discipline_name1)
        disciplines_service.append_discipline_to_list(d1)
        list1 = disciplines_service.search_discipline_by_id(substring1)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_id(substring2)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_id(substring3)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_id(substring4)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]
        list1 = disciplines_service.search_discipline_by_id(substring5)
        assert disciplines_service.disciplines.discipline_list[10].discipline_id == list1[0]

    @staticmethod
    def run_all_tests():
        TestService.test_append_student_to_list()
        TestService.test_remove_student_from_list()
        TestService.test_append_discipline_to_list()
        TestService.test_remove_discipline_from_list()
        TestService.test_append_grade_to_student()
        TestService.test_remove_grade_from_list_with_student_id()
        TestService.test_remove_grade_from_list_with_discipline_id()
        TestService.test_update_student_name()
        TestService.test_update_discipline_name()
        TestService.test_search_student_by_name()
        TestService.test_search_student_by_id()
        TestService.test_search_discipline_by_name()
        TestService.test_search_discipline_by_id()


TestService.run_all_tests()
