import unittest
from src.Validation.validation import Validation


class TestValidation(unittest.TestCase):

    def test_validate_input(self):

        user_text = ''
        self.assertEqual(Validation.validate_input(user_text), False)

        user_text = '1dsah'
        self.assertEqual(Validation.validate_input(user_text), False)

        user_text = '10'
        self.assertEqual(Validation.validate_input(user_text), False)

        user_text = '-10'
        self.assertEqual(Validation.validate_input(user_text), False)

        user_text = '4'
        self.assertEqual(Validation.validate_input(user_text), True)

    def test_validate_user_choice(self):

        user_text = ''
        self.assertEqual(Validation.validate_user_choice(user_text), False)

        user_text = '12dcxsa'
        self.assertEqual(Validation.validate_user_choice(user_text), False)

        user_text = '3'
        self.assertEqual(Validation.validate_user_choice(user_text), False)

        user_text = '1'
        self.assertEqual(Validation.validate_user_choice(user_text), True)