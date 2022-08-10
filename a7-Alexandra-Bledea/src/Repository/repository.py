"""
We implement the class for each list's entity
"""


class StudentRepository:

    def __init__(self):
        self._student_list = []

    @property
    def student_list(self):
        return self._student_list

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

    def __getitem__(self, item):
        return self.grade_list[item]

