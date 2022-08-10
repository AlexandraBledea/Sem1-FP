

class DisciplineException(Exception):
    def __init__(self, msg):
        self._msg = msg

    def __str__(self):
        return str(self._msg)


class Discipline:

    def __init__(self, id_, name):
        """
        :param id_: the unique id for the discipline
        :param name: the name of the discipline
        """
        self._discipline_id = id_
        self._discipline_name = name

    @property
    def discipline_id(self):
        return self._discipline_id

    @discipline_id.setter
    def discipline_id(self, new_id):
        self._discipline_id = new_id

    @property
    def discipline_name(self):
        return self._discipline_name

    @discipline_name.setter
    def discipline_name(self, new_name):
        self._discipline_name = new_name

    def __str__(self):
        """
        :return: the string form of a discipline
        """
        return str(self.discipline_id).rjust(9) + ' | ' + str(self.discipline_name).rjust(10)
