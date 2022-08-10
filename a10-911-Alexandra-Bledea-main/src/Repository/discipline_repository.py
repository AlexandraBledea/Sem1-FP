from src.Iterable.iterable_object import IterableObject


class DisciplineRepository:

    def __init__(self):
        self._discipline_list = IterableObject()

    @property
    def discipline_list(self):
        return self._discipline_list

    @discipline_list.setter
    def discipline_list(self, new_list):
        self._discipline_list = new_list

    def add_discipline_to_list(self, discipline):
        """
        With this function we add another discipline to the list
        :param discipline: the new discipline
        :return: it doesn't return anything
        """
        self.discipline_list.add_item(discipline)

    def delete_discipline_from_list(self, index):
        """
        With this function we delete a discipline from the list at a specified position
        :param index: represents the position of the discipline in list
        :return: it doesn't return anything
        """
        del self.discipline_list[index]

    def update_discipline(self, new_name, index):
        self._discipline_list[index].discipline_name = new_name

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.discipline_list)
