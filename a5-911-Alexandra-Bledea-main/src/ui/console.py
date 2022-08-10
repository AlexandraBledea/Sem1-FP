"""
    UI class.

    Calls between program modules
    ui -> service -> entity
    ui -> entity
"""

from src.services.service import Services
from src.services.service import SplitFunctions
from src.services.service import HistoryList


class Console:

    def display_list_ui(self, variable):
        """
        With this function we display the complex numbers from the complex numbers list in their string form
        :param variable: It is the object which we created to access the complex numbers list from the class
        ComplexNumbersList
        :return: It returns always false because it doesn't change in any way the complex numbers list
        """
        print()
        for number in variable.complex_numbers_list:
            print(number)
        return False

    def add_complex_number_ui(self, variable):
        """
        :param variable: It is the object which we created to access the functions for the complex numbers list from
        the class ComplexNumbersList
        :return: It return true if a the complex numbers list was changed and false if otherwise
        """
        complex_number = input('Read the complex number: ')
        try:
            variable.append_complex_number_to_list(SplitFunctions.split_complex_numbers(complex_number))
            a_change_was_made = True
        except ValueError as ve:
            print(ve)
            a_change_was_made = False
        return a_change_was_made

    def filter_the_list_of_complex_number_ui(self, variable):
        """
        :param variable: It is the object which we created to access the functions for the complex numbers list from
        the class ComplexNumbersList
        :return: It returns true if a change was made and false otherwise
        """
        start = int(input('Read the start position: '))
        end = int(input('Read the end position: '))
        if start >= 0 and end <= len(variable.complex_numbers_list):
            return variable.filter_complex_numbers_between_start_and_end(start, end)
        elif start < 0 and end < len(variable.complex_numbers_list):
            raise ValueError("Unknown value for start position")
        elif end > len(variable.complex_numbers_list) and start > 0:
            raise ValueError("Unknown value for end position")
        elif start < 0 and end > len(variable.complex_numbers_list):
            raise ValueError("Unknown values for start and end position")

    def print_menu(self):
        print('\n1. Add a complex number to the list')
        print('2. Display the entire list of complex numbers')
        print('3. Filter the list so that it contains only the numbers between indices start and end,'
              ' where these values are read from the console.')
        print('0. Exit the application.')
        print('-1. Undo the last operation that modified program data. This step can be repeated.')

    def start_command_ui(self):
        """
        It is the start function
        :return: it doesn't return anything, but call other functions if the command given by the user is not invalid
        """
        variable = Services()
        second_variable = HistoryList()
        second_variable.append_to_history_list(list(variable.complex_numbers_list))

        command_dict = {'2': self.display_list_ui, '1': self.add_complex_number_ui, '3':
                        self.filter_the_list_of_complex_number_ui}
        are_we_done_yet = False
        while not are_we_done_yet:
            print('\nMENU')
            self.print_menu()
            command = input('\nWhat would you like to do? Enter command: \n')
            if command in command_dict:
                try:
                    if command_dict[command](variable):
                        variable.complex_numbers_list = list(variable.complex_numbers_list)
                        second_variable.append_to_history_list(list(variable.complex_numbers_list))
                except ValueError as ve:
                    print(ve)
            elif command == '0':
                print("Goodbye!")
                are_we_done_yet = True
            elif command == '-1':
                if len(second_variable.history_list) >= 2:
                    second_variable.remove_at_position(len(second_variable.history_list)-1)
                    variable.complex_numbers_list = list(second_variable.history_list[len(second_variable.
                                                                                         history_list)-1])
                else:
                    print("There are no operations to undo")
            else:
                print("Invalid command")
