from src.Repository.discipline_repository import DisciplineRepository
from src.Domain.discipline import Discipline


class DisciplineRepoFileText(DisciplineRepository):

    def __init__(self, file_name):
        super(DisciplineRepoFileText, self).__init__()
        self.__file_name = file_name
        self.create_text_file()
        self.__load_file()

    def create_text_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def __load_file(self):
        try:
            file = open(self.__file_name, 'rt')
            lines = file.readlines()
            file.close()

            for line in lines:
                line = line.strip('\n')
                if line == '':
                    continue
                else:
                    discipline_parameters = line.split(';')
                    super().add_discipline_to_list(Discipline(discipline_parameters[0], discipline_parameters[1]))
        except Exception as e:
            print(e)

    def __save_file(self):
        try:
            file = open(self.__file_name, 'wt')
            self.discipline_list.sort(reverse=False, key=lambda x: x.discipline_id)
            for disc in self.discipline_list:
                discipline = str(disc.discipline_id) + ';' + str(disc.discipline_name)
                file.write(discipline)
                file.write('\n')
            file.close()
        except Exception as e:
            print(e)

    def add_discipline_to_list(self, discipline):
        super(DisciplineRepoFileText, self).add_discipline_to_list(discipline)
        self.__save_file()

    def delete_discipline_from_list(self, discipline_id):
        super(DisciplineRepoFileText, self).delete_discipline_from_list(discipline_id)
        self.__save_file()

    def update_discipline(self, new_name, index):
        super(DisciplineRepoFileText, self).update_discipline(new_name, index)
        self.__save_file()
