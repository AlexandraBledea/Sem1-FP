from src.Repository.grade_repository import GradeRepository
from src.Domain.grade import Grade
from src.Iterable.iterable_object import IterableObject


class GradeRepoFileText(GradeRepository):

    def __init__(self, file_name):
        super(GradeRepoFileText, self).__init__()
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
                    grade_parameters = line.split(';')
                    super().add_grade_to_list(Grade(grade_parameters[0], grade_parameters[1], grade_parameters[2]))
        except Exception as e:
            print(e)

    def __save_file(self):
        try:
            file = open(self.__file_name, 'wt')
            IterableObject.sort(self.grade_list, lambda grade1, grade2: grade1.discipline_id_g >=
                                grade2.discipline_id_g)
            for index in range(len(self.grade_list)):
                grade = str(self.grade_list[index].discipline_id_g) + ';' + str(self.grade_list[index].student_id_g) +\
                        ';' + str(self.grade_list[index].grade_value)
                file.write(grade)
                file.write('\n')
            file.close()
        except Exception as e:
            print(e)

    def add_grade_to_list(self, grade):
        super(GradeRepoFileText, self).add_grade_to_list(grade)
        self.__save_file()

    def delete_grade_from_list(self, index):
        super(GradeRepoFileText, self).delete_grade_from_list(index)
        self.__save_file()
