

class Validation:

    def validate_ship_input(self, command):

        """
        With this function we check if the position given by the user is a valid one
        Which means either all the letters have to be the same and the numbers different but consecutive
        or all the numbers have to be the same and the letters different but consecutive
        A1A2A3
        0 1 2 3 4 5
        A 1 B 1 C 1
        0 1 2 3 4 5 -  4 possibilities
        A B C D E F - 4 possibilities

        :param command: represents the position gave by the user for the boat
        :return: it returns true if the position is valid or false otherwise
        """
        if len(command) != 6:
            return False

        if not command[0].isalpha():
            return False

        if not command[2].isalpha():
            return False

        if not command[4].isalpha():
            return False

        if not command[1].isnumeric():
            return False

        if not command[3].isnumeric():
            return False

        if not command[5].isnumeric():
            return False

        if command[0] == command[2] == command[4]:
            if command[1] == '0' and command[3] == '1' and command[5] == '2':
                return True
            elif command[1] == '1' and command[3] == '2' and command[5] == '3':
                return True
            elif command[1] == '2' and command[3] == '3' and command[5] == '4':
                return True
            elif command[1] == '3' and command[3] == '4' and command[5] == '5':
                return True
        elif command[1] == command[3] == command[5]:
            if command[0] == 'A' and command[2] == 'B' and command[4] == 'C':
                return True
            elif command[0] == 'B' and command[2] == 'C' and command[4] == 'D':
                return True
            elif command[0] == 'C' and command[2] == 'D' and command[4] == 'E':
                return True
            elif command[0] == 'D' and command[2] == 'E' and command[4] == 'F':
                return True

        return False

    def validate_input_attack(self, command):

        if len(command) != 2:
            return False
        letters = ['A', 'B', 'C', 'D', 'E', 'F']
        found = False
        for letter in letters:
            if command[0] == letter:
                found = True
        if not found:
            return False

        found = False
        digits = ['0', '1', '2', '3', '4', '5']
        for digit in digits:
            if command[1] == digit:
                found = True

        if not found:
            return False

        return True

