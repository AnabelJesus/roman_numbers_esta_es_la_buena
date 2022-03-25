import unittest
from roman_numbers import roman_numbers


class roman_numbers_should(unittest.TestCase):

    def test_return_I_when_1(self):

        # Arrange
        input_int = 1
        expected_output = "I"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)


    def test_return_V_when_5(self):

        # Arrange
        input_int = 5
        expected_output = "V"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)

    def test_return_X_when_10(self):

        # Arrange
        input_int = 10
        expected_output = "X"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)

    def test_return_L_when_50(self):

        # Arrange
        input_int = 50
        expected_output = "L"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)

    def test_return_C_when_100(self):
        # Arrange
        input_int = 100
        expected_output = "C"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)

    def test_return_D_when_500(self):
        # Arrange
        input_int = 500
        expected_output = "D"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)

    def test_return_M_when_1000(self):
        # Arrange
        input_int = 1000
        expected_output = "M"

        # Act
        output = roman_numbers().roman(input_int=input_int)

        # Act
        self.assertEqual(expected_output, output)