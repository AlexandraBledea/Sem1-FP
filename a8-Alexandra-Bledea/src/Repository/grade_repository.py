

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

