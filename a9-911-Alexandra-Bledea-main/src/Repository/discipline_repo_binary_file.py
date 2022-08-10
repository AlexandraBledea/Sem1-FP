from src.Repository.discipline_repository import DisciplineRepository
import pickle


class DisciplineRepoBinaryFile(DisciplineRepository):

    def __init__(self, file_name):
        super(DisciplineRepoBinaryFile, self).__init__()
        self.__file_name = file_name
        self.create_binary_file()
        self.read_binary_file()

    def create_binary_file(self):
        try:
            file = open(self.__file_name, "x")
            file.close()
        except FileExistsError:
            pass

    def write_binary_file(self):
        try:
            file = open(self.__file_name, "wb")
            self.discipline_list.sort(reverse=False, key=lambda x: x.discipline_id)
            pickle.dump(self.discipline_list, file)
            file.close()
        except Exception as e:
            print(e)

    def read_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self.discipline_list = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eoe:
            print(eoe)

    def add_discipline_to_list(self, discipline):
        super(DisciplineRepoBinaryFile, self).add_discipline_to_list(discipline)
        self.write_binary_file()

    def delete_discipline_from_list(self, discipline_id):
        super(DisciplineRepoBinaryFile, self).delete_discipline_from_list(discipline_id)
        self.write_binary_file()

    def update_discipline(self, new_name, index):
        super(DisciplineRepoBinaryFile, self).update_discipline(new_name, index)
        self.write_binary_file()
