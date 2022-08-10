from src.Repository.grade_repository import GradeRepository
from src.Iterable.iterable_object import IterableObject
import pickle


class GradeRepoBinaryFile(GradeRepository):

    def __init__(self, file_name):
        super(GradeRepoBinaryFile, self).__init__()
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
            IterableObject.sort(self.grade_list, lambda grade1, grade2: grade1.discipline_id_g >=
                                grade2.discipline_id_g)
            pickle.dump(self.grade_list, file)
            file.close()
        except Exception as e:
            print(e)

    def read_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self.grade_list = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eoe:
            print(eoe)

    def add_grade_to_list(self, grade):
        super(GradeRepoBinaryFile, self).add_grade_to_list(grade)
        self.write_binary_file()

    def delete_grade_from_list(self, index):
        super(GradeRepoBinaryFile, self).delete_grade_from_list(index)
        self.write_binary_file()
