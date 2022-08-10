

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