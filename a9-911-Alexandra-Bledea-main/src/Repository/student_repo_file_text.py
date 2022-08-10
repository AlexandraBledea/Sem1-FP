from src.Repository.student_repository import StudentRepository
from src.Domain.student import Student


class StudentRepoFileText(StudentRepository):

    def __init__(self, file_name):
        super(StudentRepoFileText, self).__init__()
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
                    student_parameters = line.split(';')
                    super().add_student_to_list(Student(student_parameters[0], student_parameters[1]))
        except Exception as e:
            print(e)

    def __save_file(self):
        try:
            file = open(self.__file_name, 'wt')
            self.student_list.sort(reverse=False, key=lambda x: x.student_id)
            for stud in self.student_list:
                student = str(stud.student_id) + ';' + str(stud.student_name)
                file.write(student)
                file.write('\n')
            file.close()
        except Exception as e:
            print(e)

    def add_student_to_list(self, student):
        super(StudentRepoFileText, self).add_student_to_list(student)
        self.__save_file()

    def delete_student_from_list(self, student_id):
        super(StudentRepoFileText, self).delete_student_from_list(student_id)
        self.__save_file()

    def update_student(self, new_name, index):
        super(StudentRepoFileText, self).update_student(new_name, index)
        self.__save_file()

