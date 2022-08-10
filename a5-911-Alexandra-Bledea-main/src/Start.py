from src.ui.console import Console
from src.domain.entity import TestFunctionsForEntity
from src.services.service import TestFunctionsForService

test_service = TestFunctionsForService()
test_service.run_all_tests()

test_entity = TestFunctionsForEntity()
test_entity.test_the_test_functions()

console_ui = Console()
console_ui.start_command_ui()
