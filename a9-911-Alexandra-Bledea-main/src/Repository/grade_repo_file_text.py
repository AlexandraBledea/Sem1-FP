from src.Repository.grade_repository import GradeRepository
from src.Domain.grade import Grade


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
            self.grade_list.sort(reverse=False, key=lambda x: x.discipline_id_g)
            for g in self.grade_list:
                grade = str(g.discipline_id_g) + ';' + str(g.student_id_g) + ';' + str(g.grade_value)
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