from src.Iterable.iterable_object import IterableObject


class GradeRepository:

    def __init__(self):
        self._grade_list = IterableObject()

    @property
    def grade_list(self):
        return self._grade_list

    @grade_list.setter
    def grade_list(self, new_list):
        self._grade_list = new_list

    def add_grade_to_list(self, grade):
        """
        With this function we add another grade for a student at a specific discipline
        :param grade: it's represents the grade which is going to be added
        :return: it doesn't return anything
        """
        self.grade_list.add_item(grade)

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
