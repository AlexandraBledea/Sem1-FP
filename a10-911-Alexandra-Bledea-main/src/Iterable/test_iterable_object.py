import unittest

from src.Domain.grade import Grade
from src.Iterable.iterable_object import IterableObject
from src.Domain.student import Student


class TestIterableObjectClass(unittest.TestCase):

    def test_next(self):

        test_list = []
        iterable_data = IterableObject()
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('8888-888', 'Andre O'))
        for student in iterable_data:
            test_list.append(student)
        self.assertEqual(next(iterable_data), test_list[0])
        self.assertEqual(next(iterable_data), test_list[1])
        self.assertEqual(next(iterable_data), test_list[2])
        with self.assertRaises(StopIteration):
            next(iterable_data)

    def test_get_item(self):

        iterable_data = IterableObject()
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('8888-888', 'Andre O'))
        self.assertEqual(str(iterable_data[0]), '9999-999 |           Ale B')
        self.assertNotEqual(str(iterable_data[0]), '8888-888 |         Andre O')
        self.assertEqual(str(iterable_data[1]), '8888-888 |         Andre O')

    def test_set_item(self):
        iterable_data = IterableObject()
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('8888-888', 'Andre O'))
        iterable_data[0] = Student('7777-777', 'Ana P')
        self.assertEqual(str(iterable_data[0]), '7777-777 |           Ana P')

    def test_del_item(self):
        iterable_data = IterableObject()
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('8888-888', 'Andre O'))
        iterable_data.__delitem__(1)
        self.assertEqual(str(iterable_data[0]), '9999-999 |           Ale B')
        self.assertEqual(len(iterable_data), 1)
        iterable_data.__delitem__(0)
        self.assertEqual(len(iterable_data), 0)

    def test_sort(self):

        iterable_data = IterableObject()
        iterable_data.add_item(Student('9999-999', 'Ale B'))
        iterable_data.add_item(Student('7777-777', 'Medeea M'))
        iterable_data.add_item(Student('8888-888', 'Andre O'))
        IterableObject.sort(iterable_data, lambda student1, student2: student1.student_id <= student2.student_id)
        self.assertEqual(str(iterable_data[0]), '9999-999 |           Ale B')
        self.assertEqual(str(iterable_data[1]), '8888-888 |         Andre O')
        self.assertEqual(str(iterable_data[2]), '7777-777 |        Medeea M')
        IterableObject.sort(iterable_data, lambda student1, student2: student1.student_id >= student2.student_id)
        self.assertEqual(str(iterable_data[0]), '7777-777 |        Medeea M')
        self.assertEqual(str(iterable_data[1]), '8888-888 |         Andre O')
        self.assertEqual(str(iterable_data[2]), '9999-999 |           Ale B')
        IterableObject.sort(iterable_data, lambda student1, student2: student1.student_name >= student2.student_name)
        self.assertEqual(str(iterable_data[0]), '9999-999 |           Ale B')
        self.assertEqual(str(iterable_data[1]), '8888-888 |         Andre O')
        self.assertEqual(str(iterable_data[2]), '7777-777 |        Medeea M')

    def test_filter(self):

        iterable_data = IterableObject()
        iterable_data.add_item(Grade('99-99-999', '9999-999', 10))
        iterable_data.add_item(Grade('88-88-888', '7778-273', 6))
        iterable_data.add_item(Grade('77-55-342', '1124-245', 3))
        iterable_data.add_item(Grade('47-34-124', '1353-245', 7))
        iterable_data.add_item(Grade('98-23-244', '1345-134', 2))
        iterable_data.add_item(Grade('74-24-133', '1111-123', 1))

        result = IterableObject.filter(iterable_data, lambda x: x.grade_value <= 5)
        self.assertEqual(iterable_data[2], result[0])
        self.assertEqual(iterable_data[4], result[1])
        self.assertEqual(iterable_data[5], result[2])

        result = IterableObject.filter(iterable_data, lambda x: x.grade_value >= 5)
        self.assertEqual(iterable_data[0], result[0])
        self.assertEqual(iterable_data[1], result[1])
        self.assertEqual(iterable_data[3], result[2])
