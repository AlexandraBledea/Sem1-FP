from src.Console.console import Console
from src.Console.consoleGUI import ConsoleGUI
from src.Repository.repository import StudentRepository, DisciplineRepository, GradeRepository
from src.Service.service import StudentService, DisciplineService, GradeService


student_repository = StudentRepository()
discipline_repository = DisciplineRepository()
grade_repository = GradeRepository()
student_service = StudentService(student_repository)
discipline_service = DisciplineService(discipline_repository)
grade_service = GradeService(discipline_repository, student_repository, grade_repository)

console_ui = Console(student_service, discipline_service, grade_service)
console_ui.start_command_ui()

#console_GUI = ConsoleGUI(student_service, discipline_service, grade_service)
#console_GUI.start()
