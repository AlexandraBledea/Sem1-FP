import random
import re

from src.Domain.discipline import Discipline, DisciplineException
from src.Validation.discipline_validation import DisciplineValidation


class DisciplineService:

    def __init__(self, discipline_repository, undo_service, random_generation=True):
        """
        :param discipline_repository: discipline repo which allows us to access the discipline list
        :param undo_service: the service for the operations undo and redo
        :param random_generation: With this variable we set if we want to random generate some entities at the start
        of the program or not
        """
        self.disciplines = discipline_repository
        self._undo_service = undo_service
        if random_generation:
            self.generate_random_discipline()
        self.sort_disciplines_list()

    def append_discipline_to_list(self, discipline):
        """
        With this function if the conditions are checked we add a new discipline to list
        :param discipline: Represents the new discipline we want to add
        :return: It doesn't return anything
        """
        DisciplineValidation.validate_discipline_id(discipline.discipline_id)
        DisciplineValidation.validate_discipline_name(discipline.discipline_name)
        DisciplineValidation.check_duplicate_id_discipline(discipline.discipline_id, self.disciplines.discipline_list)
        DisciplineValidation.check_duplicate_name_discipline(discipline.discipline_name,
                                                             self.disciplines.discipline_list)
        self.disciplines.add_discipline_to_list(discipline)

    def append_discipline_to_list_with_record(self, discipline):
        """
        With this function if the new discipline was added to the list we keep record of the operations for undo and
        redo
        :param discipline: the new discipline we want to add
        :return: it doesn't return anything
        """
        self.append_discipline_to_list(discipline)

        operation = self._undo_service.create_new_add_operation(self.remove_discipline_from_list,
                                                                [discipline.discipline_id],
                                                                self.append_discipline_to_list, [discipline])
        self._undo_service.record(operation)

    def remove_discipline_from_list(self, discipline_id):
        """
        With this function, if the conditions are checked we delete a discipline
        :param discipline_id: represents the id of the discipline we want to delete
        :return: it returns the object discipline, both with its id and its name
        """
        discipline_deleted = False
        DisciplineValidation.validate_discipline_id(discipline_id)
        while not discipline_deleted:
            if DisciplineValidation.check_existence_of_discipline_id(discipline_id, self.disciplines.discipline_list):
                i = 0
                while i < len(self.disciplines.discipline_list):
                    d = self.disciplines.discipline_list[i]
                    if d.discipline_id == discipline_id:
                        self.disciplines.delete_discipline_from_list(i)
                        discipline = d
                        discipline_deleted = True
                    else:
                        i = i + 1
        return discipline

    def remove_discipline_from_list_with_record(self, discipline_id, grade_service):
        """
        With this function after we remove a given discipline, we keep the record of the operation for undo/redo
        :param grade_service:
        :param discipline_id: Represents the id for the discipline we want to remove
        :return: it doesn't return anything
        """
        all_operations = ()

        discipline = self.remove_discipline_from_list(discipline_id)
        discipline_operation = self._undo_service.create_new_remove_operation(self.remove_discipline_from_list,
                                                                              [discipline_id],
                                                                              self.append_discipline_to_list,
                                                                              [discipline])
        grade_operations = grade_service.remove_grade_from_list_with_discipline_id(discipline_id)

        all_operations = all_operations + (discipline_operation,)
        all_operations = all_operations + grade_operations

        self._undo_service.add_new_cascading_operation(*all_operations)

    def generate_random_discipline(self, cont=10):
        """
        :param cont: represents how many disciplines we want to random generate
        :return: it doesn't return anything
        """
        if len(self.disciplines.discipline_list) != 0:
            return

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

    def update_discipline(self, discipline_id, new_name):
        """
        With this function we update the name of a discipline if the conditions are checked
        :param discipline_id: The id of the discipline for which we want to update the name
        :param new_name: The new name we want to give to the specified discipline
        :return: It returns the initial name of the discipline
        """
        DisciplineValidation.validate_discipline_id(discipline_id)
        DisciplineValidation.validate_discipline_name(new_name)
        DisciplineValidation.check_duplicate_name_discipline(new_name, self.disciplines.discipline_list)
        if DisciplineValidation.check_existence_of_discipline_id(discipline_id, self.disciplines.discipline_list):
            for i in range(0, len(self.disciplines.discipline_list)):
                if self.disciplines.discipline_list[i].discipline_id == discipline_id:
                    name = self.disciplines.discipline_list[i].discipline_name
                    self.disciplines.update_discipline(new_name, i)
        return name

    def update_name_discipline_with_record(self, discipline_id, new_name):
        """
        With this function after the name of a discipline was updated we keep record of the operation for undo and redo
        :param discipline_id: the id of the discipline for which we want to change the name
        :param new_name: the new name we want to give to the specified discipline
        :return: it doesn't return anything
        """

        name = self.update_discipline(discipline_id, new_name)

        operation = self._undo_service.create_new_update_operation(self.update_discipline, [discipline_id, name],
                                                                   [discipline_id, new_name])
        self._undo_service.record(operation)

    def search_discipline_by_name(self, name):
        """
        With this function we check if a given substring is part of the name of any discipline
        :param name: the given substring
        :return: it returns the list of disciplines ids if the conditions are checked
        """
        if len(name) == 0:
            raise DisciplineException("A name is required!")
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
        if len(discipline_id) == 0:
            raise DisciplineException("An ID is required!")
        existent = False
        discipline_id_list = []
        for discipline in self.disciplines.discipline_list:
            if re.search(discipline_id.strip(), discipline.discipline_id):
                discipline_id_list.append(discipline.discipline_id)
                existent = True
        if not existent:
            raise DisciplineException("There is no existing discipline with the provided ID")
        else:
            return discipline_id_list

    def sort_disciplines_list(self):
        """
        With this function we sort the disciplines list according to their IDs
        :return: It doesn't return anything
        """
        self.disciplines.discipline_list.sort(reverse=False, key=lambda x: x.discipline_id)

