"""
    Service class includes functionalities for implementing program features
"""

from random import randint
from src.domain.entity import ComplexNumber
import sys


class Services:

    def __init__(self):
        """
        we initialize the list for the complex numbers
        """
        self.complex_numbers_list = []
        self.generate_complex_numbers()
        # self.test_init()

    @property
    def complex_numbers_list(self):
        """
        getter for the complex numbers list
        :return:it returns the complex numbers list
        """
        return self._complex_numbers_list

    @complex_numbers_list.setter
    def complex_numbers_list(self, new_list):
        """
        setter for the complex numbers list
        :param new_list: it's the list with the new values we want to attribute to the current complex numbers list
        :return: it won't return anything
        """
        self._complex_numbers_list = list(new_list)

    def __len__(self):
        """
        :return: the length of the complex numbers list
        """
        return len(self.complex_numbers_list)

    def append_complex_number_to_list(self, complex_number):
        """
        :param complex_number: the complex number we want to append to the complex numbers list
        :return: it doesn't return anything
        """
        self.complex_numbers_list.append(complex_number)

    def generate_complex_numbers(self):
        """
        it generates randomly 10 complex numbers
        :return: it doesn't return anything
        """
        for i in range(10):
            complex_number = ComplexNumber(randint(-sys.maxsize-1, sys.maxsize), randint(-sys.maxsize-1, sys.maxsize))
            self.append_complex_number_to_list(complex_number)

    def filter_complex_numbers_between_start_and_end(self, start, end):
        """
        With this function we create a new list which keeps the complex numbers between the start index and the end
        index which are given by the user and in the current complex numbers list we copy the new list which was created
        :param start: the start index
        :param end: the end index
        :return: it return True if a change was made, or false otherwise
        """
        new_list = []
        a_change_was_made = False
        for i in range(0, len(self.complex_numbers_list)):
            if start <= i <= end:
                new_list.append(self.complex_numbers_list[i])
                a_change_was_made = True
        self.complex_numbers_list = new_list[:]
        return a_change_was_made


class SplitFunctions:

    @staticmethod
    def split_complex_numbers(complex_number):
        """
        With this function we split the numbers in the form a+bi, we obtain the real part and the imaginary part and
        with them we create the new complex number.
        :param complex_number: the complex number we want to split
        :return: it returns the new complex number created with the ComplexNumbers class
        """
        number_string = complex_number.strip(' \n')  # remove any unnecessary spaces or newline characters
        if not number_string:
            raise ValueError("No number was read")
        if number_string.find('+') != -1:
            if number_string.find('i') == -1:
                raise ValueError("Invalid number format!")
            parts = number_string.split('+')
            if len(parts) == 2:
                real_part_str = parts[0].strip()
                imaginary_part_str_1 = parts[1].strip()
                imaginary_part_str_2 = imaginary_part_str_1.rstrip("i")
                if imaginary_part_str_2 == '':
                    return ComplexNumber(int(real_part_str), 1)
                return ComplexNumber(int(real_part_str), int(imaginary_part_str_2))
            else:
                raise ValueError("Invalid number format!")
        elif number_string.find('-') != -1:
            parts = number_string.split('-')
            if len(parts) == 3:
                del parts[0]
                real_part_str = parts[0].strip()
                imaginary_part_str_1 = parts[1].strip()
                imaginary_part_str_2 = imaginary_part_str_1.rstrip("i")
                return ComplexNumber(-1 * int(real_part_str), -1 * int(imaginary_part_str_2))
            elif len(parts) == 2:
                if number_string.find('-') == 0:
                    del parts[0]
                    if parts[0] == "i":
                        return ComplexNumber(0, -1)
                    elif parts[0].find('i') != -1:
                        imaginary_part = parts[0].rstrip('i')
                        return ComplexNumber(0, -1 * int(imaginary_part))
                    else:
                        return ComplexNumber(-1 * int(parts[0].strip()), 0)
                else:
                    real_part_str = parts[0].strip()
                    imaginary_part_str_1 = parts[1].strip()
                    imaginary_part_str_2 = imaginary_part_str_1.rstrip("i")
                    return ComplexNumber(int(real_part_str), -1 * int(imaginary_part_str_2))
            elif len(parts) == 1:
                imaginary_part_str_1 = parts[0].strip()
                imaginary_part_str_2 = imaginary_part_str_1.rstrip("i")
                return ComplexNumber(0, -1 * int(imaginary_part_str_2))
            else:
                raise ValueError("Invalid number format!")
        else:
            if number_string == 'i':
                return ComplexNumber(0, 1)
            elif number_string.find('i') != -1:
                imaginary_part_str = number_string.rstrip('i')
                return ComplexNumber(0, int(imaginary_part_str))
            return ComplexNumber(int(number_string), 0)


class HistoryList:

    def __init__(self):
        """
        We initialize the list which will keep all the complex numbers list starting with the current one and going on
        with all the other complex numbers list which suffered a change.
        """
        self._history_list = []

    def remove_at_position(self, index):
        """
        With this function we delete the value corresponding to the specified index from the history list
        :param index: it represents the position of the value we want to delete from the history list
        :return: it doesn't return anything
        """
        del self._history_list[index]

    @property
    def history_list(self):
        """
        getter for the history list
        :return:it returns the history list
        """
        return self._history_list

    def append_to_history_list(self, list_of_numbers):
        """
        With this function we append a new list to the history list
        :param list_of_numbers: the new list we want to append to the history list
        :return: it doesn't return anything
        """
        self._history_list.append(list(list_of_numbers))

    def __len__(self):
        """
        :return: the length of the history list
        """
        return len(self._history_list)


class TestFunctionsForService:

    @staticmethod
    def test_append_function_for_list_of_complex_numbers():
        variable = Services()
        _new_list = list(variable.complex_numbers_list)
        z1 = '2+2i'
        variable.append_complex_number_to_list(z1)
        _new_list.append(z1)
        assert _new_list == variable.complex_numbers_list

    @staticmethod
    def test_length_for_the_list():
        variable = Services()
        assert len(variable.complex_numbers_list) == 10
        assert len(variable.complex_numbers_list) != 12

    @staticmethod
    def test_filter_function():
        variable = Services()
        _new_list = []
        start = 0
        end = 3
        for i in range(start, end+1):
            _new_list.append(variable.complex_numbers_list[i])
        variable.filter_complex_numbers_between_start_and_end(start, end)
        assert _new_list == variable.complex_numbers_list

    @staticmethod
    def test_split_number():
        variable = SplitFunctions
        num_str_1 = ""
        try:
            variable.split_complex_numbers(num_str_1)
        except ValueError:
            assert True

        num_str_2 = '    15 + 4i   '
        complex_number = variable.split_complex_numbers(num_str_2)
        assert complex_number.real == 15
        assert complex_number.imaginary == 4

        num_str_3 = '   /15 + 4i'
        try:
            variable.split_complex_numbers(num_str_3)
        except ValueError:
            assert True

        num_str_4 = '   15 + 4i/  '
        try:
            variable.split_complex_numbers(num_str_4)
        except ValueError:
            assert True

        num_str_5 = '-5 - 4i  '
        complex_number = variable.split_complex_numbers(num_str_5)
        assert complex_number.real == -5
        assert complex_number.imaginary == -4

        num_str_6 = '-5 + 4i'
        complex_number = variable.split_complex_numbers(num_str_6)
        assert complex_number.real == -5
        assert complex_number.imaginary == 4

        num_str_7 = '5 - 4i'
        complex_number = variable.split_complex_numbers(num_str_7)
        assert complex_number.real == 5
        assert complex_number.imaginary == -4

        num_str_8 = 'i'
        complex_number = variable.split_complex_numbers(num_str_8)
        assert complex_number.real == 0
        assert complex_number.imaginary == 1

        num_str_9 = '4i'
        complex_number = variable.split_complex_numbers(num_str_9)
        assert complex_number.real == 0
        assert complex_number.imaginary == 4

        num_str_10 = '-i'
        complex_number = variable.split_complex_numbers(num_str_10)
        assert complex_number.real == 0
        assert complex_number.imaginary == -1

        num_str_11 = '-4i'
        complex_number = variable.split_complex_numbers(num_str_11)
        assert complex_number.real == 0
        assert complex_number.imaginary == -4

        num_str_12 = '10'
        complex_number = variable.split_complex_numbers(num_str_12)
        assert complex_number.real == 10
        assert complex_number.imaginary == 0

        num_str_13 = '0'
        complex_number = variable.split_complex_numbers(num_str_13)
        assert complex_number.real == 0
        assert complex_number.imaginary == 0

        num_str_14 = '-11'
        complex_number = variable.split_complex_numbers(num_str_14)
        assert complex_number.real == -11
        assert complex_number.imaginary == 0

    @staticmethod
    def append_to_history_list_test():
        variable = HistoryList()
        new_list = [1]
        new_list2 = [2]
        new_list3 = [3]
        variable.append_to_history_list(new_list)
        assert variable._history_list[len(variable._history_list)-1] == new_list
        variable.append_to_history_list(new_list2)
        assert variable._history_list[len(variable._history_list)-1] == new_list2
        assert variable._history_list[len(variable._history_list)-1] != new_list3

    @staticmethod
    def test_length_for_history_list():
        variable = HistoryList()
        new_list = [1]
        new_list2 = [2]
        new_list3 = [3]
        assert len(variable._history_list) == 0
        variable.append_to_history_list(new_list)
        assert len(variable._history_list) != 0
        assert len(variable._history_list) == 1
        variable.append_to_history_list(new_list2)
        assert len(variable._history_list) != 1
        assert len(variable._history_list) == 2
        variable.append_to_history_list(new_list3)
        assert len(variable._history_list) != 2
        assert len(variable._history_list) == 3

    @staticmethod
    def test_remove_at_position():
        variable = HistoryList()
        new_list1 = [1]
        new_list2 = [2]
        new_list3 = [3, 4]
        variable.append_to_history_list(new_list1)
        variable.append_to_history_list(new_list2)
        variable.append_to_history_list(new_list3)
        assert len(variable._history_list) == 3
        variable.remove_at_position(2)
        assert len(variable._history_list) == 2
        assert variable._history_list[len(variable._history_list) - 1] == new_list2
        assert variable._history_list[len(variable._history_list) - 1] != new_list3
        variable.remove_at_position(1)
        assert len(variable._history_list) == 1
        assert variable._history_list[len(variable._history_list) - 1] == new_list1
        assert variable._history_list[len(variable._history_list) - 1] != new_list2
        variable.remove_at_position(0)
        assert len(variable._history_list) == 0

    @staticmethod
    def run_all_tests():
        TestFunctionsForService.test_append_function_for_list_of_complex_numbers()
        TestFunctionsForService.test_length_for_the_list()
        TestFunctionsForService.test_filter_function()
        TestFunctionsForService.test_split_number()
        TestFunctionsForService.append_to_history_list_test()
        TestFunctionsForService.test_length_for_history_list()
        TestFunctionsForService.test_remove_at_position()
