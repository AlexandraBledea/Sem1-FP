from src.Console.console import Console
from src.Console.consoleGUI import ConsoleGUI
from src.Repository.discipline_repository import DisciplineRepository
from src.Repository.grade_repository import GradeRepository
from src.Repository.student_repository import StudentRepository
from src.Service.discipline_service import DisciplineService
from src.Service.grade_service import GradeService
from src.Service.student_service import StudentService
from src.Service.undo_service import UndoService
from src.Repository.student_repo_file_text import StudentRepoFileText
from src.Repository.discipline_repo_file_text import DisciplineRepoFileText
from src.Repository.grade_repo_file_text import GradeRepoFileText
from src.Repository.student_repo_binary_file import StudentRepoBinaryFile
from src.Repository.discipline_repo_binary_file import DisciplineRepoBinaryFile
from src.Repository.grade_repo_binary_file import GradeRepoBinaryFile
from jproperties import Properties


class Settings:

    def __init__(self, file):
        program_properties = Properties()
        with open(file, 'rb') as configuration_file:
            program_properties.load(configuration_file)
        try:
            self._repository_type = program_properties['repository'].data
            self._student_repository_type = program_properties['students'].data
            self._discipline_repository_type = program_properties['disciplines'].data
            self._grade_repository_type = program_properties['grades'].data
            self._generate = program_properties['generate'].data
            self._ui_type = program_properties['ui'].data
        except KeyError as ke:
            print(ke)
            exit(0)

    @property
    def generate(self):
        return self._generate

    @property
    def repository_type(self):
        return self._repository_type

    @property
    def ui_type(self):
        return self._ui_type

    @property
    def student_repository_type(self):
        return self._student_repository_type

    @property
    def discipline_repository_type(self):
        return self._discipline_repository_type

    @property
    def grade_repository_type(self):
        return self._grade_repository_type


if __name__ == "__main__":
    program_settings = Settings('settings.properties')
    if program_settings.repository_type == 'in_memory':
        student_repository = StudentRepository()
        discipline_repository = DisciplineRepository()
        grade_repository = GradeRepository()

    elif program_settings.repository_type == 'text_files':
        try:
            student_repository = StudentRepoFileText(program_settings.student_repository_type)
            discipline_repository = DisciplineRepoFileText(program_settings.discipline_repository_type)
            grade_repository = GradeRepoFileText(program_settings.grade_repository_type)
        except Exception as e:
            print(e)

    elif program_settings.repository_type == 'binary_files':
        try:
            student_repository = StudentRepoBinaryFile(program_settings.student_repository_type)
            discipline_repository = DisciplineRepoBinaryFile(program_settings.discipline_repository_type)
            grade_repository = GradeRepoBinaryFile(program_settings.grade_repository_type)
        except Exception as e:
            print(e)
    else:
        print("Invalid type for repository! It doesn't exist!")
        exit(0)

    undo_service = UndoService()
    if program_settings.generate == 'True':
        student_service = StudentService(student_repository, undo_service)
        discipline_service = DisciplineService(discipline_repository, undo_service)
        grade_service = GradeService(discipline_repository, student_repository, grade_repository, undo_service)
    else:
        student_service = StudentService(student_repository, undo_service, False)
        discipline_service = DisciplineService(discipline_repository, undo_service, False)
        grade_service = GradeService(discipline_repository, student_repository, grade_repository, undo_service, False)

    if program_settings.ui_type == 'ui':
        console_ui = Console(student_service, discipline_service, grade_service, undo_service)
        console_ui.start_command_ui()
    elif program_settings.ui_type == 'gui':
        console_GUI = ConsoleGUI(student_service, discipline_service, grade_service, undo_service)
        console_GUI.start()


"""

repository = binary_files
students = students.pickle
disciplines = discipline.pickle
grades = grade.pickle
generate = False
ui = gui


repository = text_files
students = students.txt
disciplines = disciplines.txt
grades = grades.txt
generate = True
ui = ui


"""