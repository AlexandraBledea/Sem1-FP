from src.Console.console import Console
from src.Console.consoleGUI import ConsoleGUI
from src.Repository.discipline_repository import DisciplineRepository
from src.Repository.grade_repository import GradeRepository
from src.Repository.student_repository import StudentRepository
from src.Service.discipline_service import DisciplineService
from src.Service.grade_service import GradeService
from src.Service.student_service import StudentService
from src.Service.undo_service import UndoService

student_repository = StudentRepository()
discipline_repository = DisciplineRepository()
grade_repository = GradeRepository()
undo_service = UndoService()
student_service = StudentService(student_repository, undo_service)
discipline_service = DisciplineService(discipline_repository, undo_service)
grade_service = GradeService(discipline_repository, student_repository, grade_repository, undo_service)


#console_ui = Console(student_service, discipline_service, grade_service, undo_service)
#console_ui.start_command_ui()

console_GUI = ConsoleGUI(student_service, discipline_service, grade_service, undo_service)
console_GUI.start()


