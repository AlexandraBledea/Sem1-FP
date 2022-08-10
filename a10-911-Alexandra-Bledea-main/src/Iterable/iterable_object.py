from src.Domain.student import Student
import functools
import unittest


class IterableObject:

    def __init__(self):
        self.index = -1
        self._iterable_data = []

    def __iter__(self):
        """
        :return: It returns an iterator
        It creates an object which can be accessed one element at a time using next
        """
        self.index = -1
        return self

    def __next__(self):
        """
        With this function we can access an iterable object by one element at a time
        :return: It returns the index of the current element
        """

        self.index = self.index + 1
        try:
            item = self._iterable_data[self.index]
        except IndexError:
            self.index = -1
            raise StopIteration()
        return item

    def __getitem__(self, item):
        return self._iterable_data[item]

    def __setitem__(self, key, value):
        self._iterable_data[key] = value

    def __delitem__(self, key):
        del self._iterable_data[key]

    def add_item(self, item):
        self._iterable_data.append(item)

    def __len__(self):
        return len(self._iterable_data)

    @staticmethod
    def sort(list_,  relation):
        """
        :param list_: represents the iterable object we want to sort
        :param relation: represents the criteria after which we proceed the sort
        :return: it doesn't return anything
        """

        """
        With this sort we take two consecutive elements from the list, starting from the first element and we compare
        them, if the condition is checked then we go to the next two elements, the index being increased by one
        if the condition is not checked then the two elements are interchanged and the index decreases
        for example if we have the following list:
        l = [5, 1, 3, 6, 9, 7] - which is a list with 6 elements
        And we want to sort it in an ascending order, so the comparison will be done by the following criteria: a > b
        where in this first care b will be 5 and a will be 1
        So we check if 1 >= 5, which is false so we interchange the values
        The list will become: 1 5 3 6 9 7
        We check if the index reached the value 0, and if so it will be increased by 1
        The index will be one again, so we check this time if 5 >= 1 which is true so the index will increase by 1
        The index will be 2 so we check if 3 >= 5 which if False, so we interchange 3 and 5 and the index will be
        decreased by 1
        The list will become: 1 3 5 6 9 7
        Now the index is 1 again and we check if 3>=1 which is true, so the index will increase
        Now the index is 2 and we check if 5 >= 3 which is true, so the index will increase
        Now the index is 3 and we check if 6 >= 5 which is true, so the index will increase and we go further
        Now the index is 4 and we check if 9 >= 6 which is true, so the index will increase and we go further
        Now the index is 5 and we check if 7 >= 9  which is false, so we interchange 7 and 9 and the index will be
        decreased by 1
        The list will become:
        1 3 5 6 7 9
        Now the index is 4 and we check if 7 >= 5 which is true, so the index will be increased and we go further
        Now the index is 5 and we check if 9 >= 7 which is true, so the index will be increased and we go further
        Now because the index is equal to the length of the list, which is 6 we get out of the while because the list is
        finally sorted : 1 3 5 6 7 9
        """

        n = len(list_)  # the length of the given list
        index = 0
        while index < n:
            if index == 0:
                index = index + 1
            if relation(list_[index], list_[index-1]):  # if the condition is checked we go to the next element
                index = index + 1
            else:  # if not, then we interchange the elements and the index decrease
                list_[index], list_[index - 1] = list_[index - 1], list_[index]
                index = index - 1

    @staticmethod
    def filter(list_, criteria):
        """
        :param list_: represents the list which is going to be filtered
        :param criteria: the criteria after which the new list will be created
        :return: it returns the filtered list
        """
        result = []
        for elem in list_:
            if criteria(elem) is True:
                result.append(elem)
        return result

