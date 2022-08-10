from src.Domain.discipline import DisciplineException


class DisciplineValidation:

    @staticmethod
    def validate_discipline_id(discipline_id):
        """
        With this function we want to check if the given id for the discipline is valid or not
        :param discipline_id: It's the given id we want to check if it's valid or not
        :return: it doesn't return anything, but if the id is not valid it will raise an error
        """
        if len(discipline_id) != 9:
            raise DisciplineException("The ID doesn't have the right format! It should be **-**-***!")
        for i in range(0, 9):
            if i == 2:
                if discipline_id[i] != '-':
                    raise DisciplineException("The ID doesn't have the right format! It should be **-**-***!")
            elif i == 5:
                if discipline_id[i] != '-':
                    raise DisciplineException("The ID doesn't have the right format! It should be **-**-***!")
            elif not discipline_id[i].isdigit():
                raise DisciplineException("The ID doesn't have the right format! It should be **-**-***!")

    @staticmethod
    def validate_discipline_name(discipline_name):
        """
        With this function we want to check if the given name for the discipline is valid or not
        :param discipline_name: It's the given name we want to check if it's valid or not
        :return: it doesn't return anything, but if the name is not valid it will raise an error
        """
        tokens = discipline_name.split(' ')
        if len(tokens) != 1:
            raise DisciplineException("The entered name is invalid!")
        if not discipline_name.isalpha():
            raise DisciplineException("The entered name is invalid!")

    @staticmethod
    def check_duplicate_id_discipline(discipline_id, discipline_list):
        """
        With this function we check if a given id for a discipline already exists
        :param discipline_id: the id we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        for d in discipline_list:
            if d.discipline_id == discipline_id:
                raise DisciplineException("There is already a discipline with the given ID and the ID should be"
                                          " unique!")

    @staticmethod
    def check_duplicate_name_discipline(discipline_name, discipline_list):
        """
        With this function we check if a given name for a discipline already exists
        :param discipline_name: the name we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        for d in discipline_list:
            if d.discipline_name == discipline_name:
                raise DisciplineException("There is already the given discipline name and each discipline should"
                                          " have unique name!")

    @staticmethod
    def check_existence_of_discipline_id(discipline_id, discipline_list):
        """
        With this function we check if a give discipline id exists
        :param discipline_id: the id we want to check
        :param discipline_list: the list of disciplines
        :return: it doesn't return anything
        """
        existent = False
        for d in discipline_list:
            if d.discipline_id == discipline_id:
                existent = True
        if not existent:
            raise DisciplineException("There is no existing discipline with the given ID!")
        else:
            return existent


'''

class GeneralValidation:

    @staticmethod
    def is_in_list_validation(list, object):
        if object in list:
            return True
        return False
'''
