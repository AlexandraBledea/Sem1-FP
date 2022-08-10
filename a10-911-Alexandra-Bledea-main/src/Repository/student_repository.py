from src.Iterable.iterable_object import IterableObject


class StudentRepository:

    def __init__(self):
        self._student_list = IterableObject()

    @property
    def student_list(self):
        return self._student_list

    @student_list.setter
    def student_list(self, new_list):
        self._student_list = new_list

    def add_student_to_list(self, student):
        """
        With this function we add another student to the list
        :param student: the new student
        :return: it doesn't return anything
        """
        self.student_list.add_item(student)

    def delete_student_from_list(self, index):
        """
        With this function we delete a student from the list at a specified position
        :param index: represents the position of the student in list
        :return: it doesn't return anything
        """
        del self.student_list[index]

    def update_student(self, new_name, index):
        self.student_list[index].student_name = new_name

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.student_list)
