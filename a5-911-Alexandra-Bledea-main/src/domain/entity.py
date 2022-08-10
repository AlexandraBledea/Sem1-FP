"""
    Entity class should be coded here
"""


class ComplexNumber:

    def __init__(self, real_part, imaginary_part):
        """
        :param real_part: the real part of the complex number
        :param imaginary_part: the imaginary part of the complex number
        """

        self._real = real_part
        self._imaginary = imaginary_part

    @property
    def real(self):
        """
        getter for the real part of the complex number
        :return:it returns the real part of the complex number
        """
        return self._real

    @property
    def imaginary(self):
        """
        getter for the imaginary part of the complex number
        :return:it returns the imaginary part of the complex number
        """
        return self._imaginary

    def __str__(self):
        """
        :return: it returns the string form of the complex number
        """
        if self.imaginary == -1:
            if self.real == 0:
                return "-i"
            else:
                return str(self.real) + " - i"
        elif self.imaginary == 1:
            if self.real == 0:
                return "i"
            else:
                return str(self.real) + " + i"
        elif self.real == 0 and self.imaginary != 0:
            return str(self.imaginary) + "i"
        elif self.imaginary < 0:
            return str(self.real) + " - " + str(abs(self.imaginary)) + "i"
        elif self.imaginary == 0:
            return str(self.real)
        else:
            return str(self.real) + " + " + str(self.imaginary) + "i"

    def __eq__(self, other):
        if not isinstance(other, ComplexNumber):
            raise TypeError("Cannot compare complex number to " + str(type(other)))
        return self.real == other.real and self.imaginary == other.imaginary


class TestFunctionsForEntity:

    def test_str_part(self):
        z1 = ComplexNumber(1, 3)
        z2 = '1 + 3i'
        assert str(z1) == z2

        z3 = ComplexNumber(0, 0)
        z4 = '0'
        assert str(z3) == z4

        z5 = ComplexNumber(0, -1)
        z6 = '-i'
        assert str(z5) == z6

        z7 = ComplexNumber(1, 0)
        z8 = '1'
        assert str(z7) == z8

        z9 = ComplexNumber(3, 1)
        z10 = '3 + i'
        assert str(z9) == z10

        z11 = ComplexNumber(3, -1)
        z12 = '3 - i'
        assert str(z11) == z12

    def test_real_imaginary_part(self):
        z1 = ComplexNumber(0, 3)
        assert 0 == z1.real
        assert 3 == z1.imaginary
        z2 = ComplexNumber(0, 0)
        assert 0 == z2.real
        assert 0 == z2.imaginary
        z3 = ComplexNumber(-2, -4)
        assert -2 == z3.real
        assert -4 == z3.imaginary
        z4 = ComplexNumber(7, -2)
        assert -7 != z4.real
        assert 2 != z4.imaginary

    def test_for_equality(self):
        z1 = ComplexNumber(3, 4)
        z2 = ComplexNumber(3, 4)
        z3 = ComplexNumber(2, 4)
        assert z1 == z2
        assert z1 != z3

    def test_the_test_functions(self):
        self.test_real_imaginary_part()
        self.test_str_part()
        self.test_for_equality()
