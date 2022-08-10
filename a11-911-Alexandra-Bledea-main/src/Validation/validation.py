

class Validation:

    @staticmethod
    def validate_input(user_input):
        """
        With this function we validate the choice of the user when it has to select the column on which it wants to
        place the piece
        :param user_input: the number of the column
        :return: it returns false if the input is not valid and true if it is
        """
        if len(user_input) == 0:
            return False
        for i in range(len(user_input)):
            if not user_input[i].isdigit():
                return False

        number = int(user_input)
        if number > 6 or number < 0:
            return False
        return True

    @staticmethod
    def validate_user_choice(user_input):
        """
        With this function we check if the user's input for the two choices it has to make is valid or not
        :param user_input: 1 or 2, depends on the user choice
        :return: returns false if the input is not valid and true if it is
        """
        if len(user_input) == 0:
            return False
        for i in range(len(user_input)):
            if not user_input[i].isdigit():
                return False
        number = int(user_input)
        if number != 1 and number != 2:
            return False
        return True

