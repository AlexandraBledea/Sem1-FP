

class StudentRepository:

    def __init__(self):
        self._student_list = []

    @property
    def student_list(self):
        return self._student_list

    def add_student_to_list(self, student):
        """
        With this function we add another student to the list
        :param student: the new student
        :return: it doesn't return anything
        """
        self.student_list.append(student)

    def delete_student_from_list(self, index):
        """
        With this function we delete a student from the list at a specified position
        :param index: represents the position of the student in list
        :return: it doesn't return anything
        """
        del self.student_list[index]

    def __len__(self):
        """
        :return: it returns the length of the list
        """
        return len(self.student_list)

    def __getitem__(self, item):
        return self.student_list[item]
