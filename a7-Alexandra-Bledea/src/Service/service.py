"""
We implement the class for the service
"""
from src.Domain.entity import Student, Discipline, Grade, StudentException, DisciplineException
from src.Validation.validate import StudentValidation, DisciplineValidation, GradeValidation
import random
import re


class StudentService:

    def __init__(self, student_repository, random_generation=True):
        self.students = student_repository
        if random_generation:
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

    def __init__(self, discipline_repository, random_generation=True):
        self.disciplines = discipline_repository
        if random_generation:
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

    def __init__(self, discipline_repository, student_repository, grade_repository, random_generation=True):
        self.discipline_repo = discipline_repository
        self.students_repo = student_repository
        self.grades = grade_repository
        if random_generation:
            self.generate_random_grades()

    def append_grade_to_student(self, grade):
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
        DisciplineValidation.check_existence_of_discipline_id(grade.discipline_id_g, self.discipline_repo)
        StudentValidation.check_existence_of_student_id(grade.student_id_g, self.students_repo)
        self.grades.add_grade_to_list(grade)

    def remove_grade_from_list_with_student_id(self, student_id):
        """
        With this function we delete all the grades which are related to a student
        :param student_id: Represents the id of the student for which we want to remove the grades
        :return: it doesn't return anything
        """
        # GradeValidation.check_existence_of_grade_student(student_id, self.grades.grade_list)
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
        student_service = StudentService(self.students_repo)
        discipline_service = DisciplineService(self.discipline_repo)
        for i in range(0, cont):
            self.grades.add_grade_to_list(Grade(discipline_service.disciplines.discipline_list[random.randint(0, 9)].
                                                discipline_id, student_service.students.student_list[random.
                                                randint(0, 9)].student_id, random.randint(1, 10)))

    def calculate_average(self):
        """
        With this function we calculate the average for each student at disciplines it has grades
        :return: the list with the average grade which a student have at each discipline at which he received grades
        """
        i = 0
        result = []
        while i < len(self.students_repo):
            for d in self.discipline_repo:
                sum_of_grades = 0
                number_of_grades = 0
                average = 0
                for g in self.grades.grade_list:
                    if self.students_repo[i].student_id == g.student_id_g and d.discipline_id == g.discipline_id_g:
                        sum_of_grades = sum_of_grades + g.grade_value
                        number_of_grades = number_of_grades + 1
                        average = sum_of_grades / number_of_grades
                if average != 0:
                    result.append(AverageStudentsStatistic(self.students_repo[i].student_id,
                                                           self.students_repo[i].student_name,
                                                           d.discipline_id, d.discipline_name, average))
            i = i + 1
        result.sort(reverse=True, key=lambda x: x.average_a)
        return result

    def calculate_general_average_for_each_student(self):
        """
        With this function we calculate the general average for each student who had received grades
        :return: the list with the general average for each student who had received grades
        """

        average_list = self.calculate_average()
        result = []
        i = 0
        while i < len(self.students_repo):
            sum_of_grades = 0
            number_of_grades = 0
            general_average = 0
            for average in average_list:
                if self.students_repo[i].student_id == average.student_id_a:
                    sum_of_grades = sum_of_grades + average.average_a
                    number_of_grades = number_of_grades + 1
                    general_average = sum_of_grades / number_of_grades
            if general_average != 0:
                result.append(GeneralAverageStudentsStatistic(self.students_repo[i].student_id,
                                                              self.students_repo[i].student_name, general_average))
            i = i + 1
        result.sort(reverse=True, key=lambda x: x.average_ga)
        return result

    def calculate_average_for_each_discipline(self):
        """
        With this function we calculate the average grade received by the students for each discipline
        :return: the list with the average grade for each discipline
        """
        result = []
        for d in self.discipline_repo:
            sum_of_grades = 0
            number_of_grades = 0
            average = 0
            for g in self.grades.grade_list:
                if d.discipline_id == g.discipline_id_g:
                    sum_of_grades = sum_of_grades + g.grade_value
                    number_of_grades = number_of_grades + 1
                    average = sum_of_grades / number_of_grades
            if average != 0:
                result.append(AverageDisciplineStatistic(d.discipline_id, d.discipline_name, average))

        result.sort(reverse=True, key=lambda x: x.average_a)
        return result


class AverageStudentsStatistic:

    def __init__(self, student_id_a, student_name_a, discipline_id_a, discipline_name_a, average_a):
        """
        :param student_id_a: the id of the student
        :param student_name_a: the name of the student
        :param discipline_id_a: the id of the discipline
        :param discipline_name_a: the name of the discipline
        :param average_a: the average grade which a student have at each discipline at which he received grades
        """
        self._student_id_a = student_id_a
        self._student_name_a = student_name_a
        self._discipline_id_a = discipline_id_a
        self._discipline_name_a = discipline_name_a
        self._average_a = average_a

    @property
    def student_id_a(self):
        return self._student_id_a

    @property
    def student_name_a(self):
        return self._student_name_a

    @property
    def discipline_id_a(self):
        return self._discipline_id_a

    @property
    def discipline_name_a(self):
        return self._discipline_name_a

    @property
    def average_a(self):
        return self._average_a

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.student_id_a).rjust(7) + ' | ' + str(self.student_name_a).rjust(20) + ' | ' \
               + str(self.discipline_id_a).rjust(9) + ' | ' + str(self.discipline_name_a).rjust(20) + ' | ' \
               + str(format(self.average_a, ".3f")).rjust(5)


class AverageDisciplineStatistic:

    def __init__(self, discipline_id_a, discipline_name_a, average_a):
        """
        :param discipline_id_a: represents the id of the discipline
        :param discipline_name_a: represents the name of the discipline
        :param average_a: average grade
        """
        self._discipline_id_a = discipline_id_a
        self._discipline_name_a = discipline_name_a
        self._average_a = average_a

    @property
    def discipline_id_a(self):
        return self._discipline_id_a

    @property
    def discipline_name_a(self):
        return self._discipline_name_a

    @property
    def average_a(self):
        return self._average_a

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.discipline_id_a).rjust(9) + ' | ' + str(self.discipline_name_a).rjust(20) + ' | ' \
               + str(format(self.average_a, ".3f")).rjust(5)


class GeneralAverageStudentsStatistic:

    def __init__(self, student_id_ga, student_name_ga, average_ga):
        """
        :param student_id_ga: the id of the student
        :param student_name_ga: the student's name
        :param average_ga: general average of the student
        """
        self._student_id_ga = student_id_ga
        self._student_name_ga = student_name_ga
        self._average_ga = average_ga

    @property
    def student_id_ga(self):
        return self._student_id_ga

    @property
    def student_name_ga(self):
        return self._student_name_ga

    @property
    def average_ga(self):
        return self._average_ga

    def __str__(self):
        """
        :return: the string form of the statistic
        """
        return str(self.student_id_ga).rjust(7) + ' | ' + str(self.student_name_ga).rjust(20) + ' | ' \
               + str(format(self.average_ga, ".3f")).rjust(5)
