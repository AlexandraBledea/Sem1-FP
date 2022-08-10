from src.Repository.student_repository import StudentRepository
import pickle


class StudentRepoBinaryFile(StudentRepository):

    def __init__(self, file_name):
        super(StudentRepoBinaryFile, self).__init__()
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
            self.student_list.sort(reverse=False, key=lambda x: x.student_id)
            pickle.dump(self.student_list, file)
            file.close()
        except Exception as e:
            print(e)

    def read_binary_file(self):
        try:
            file = open(self.__file_name, "rb")
            self.student_list = pickle.load(file)
        except IOError as ie:
            print(ie)
        except EOFError as eoe:
            print(eoe)

    def add_student_to_list(self, student):
        super(StudentRepoBinaryFile, self).add_student_to_list(student)
        self.write_binary_file()

    def delete_student_from_list(self, student_id):
        super(StudentRepoBinaryFile, self).delete_student_from_list(student_id)
        self.write_binary_file()

    def update_student(self, new_name, index):
        super(StudentRepoBinaryFile, self).update_student(new_name, index)
        self.write_binary_file()
