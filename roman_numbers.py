ROMAN_NUMBERS_DICT = {1:'I',
                      5:'V',
                      10:'X',
                      50:'L',
                      100:'C',
                      500:'D',
                      1000:'M'}


class roman_numbers:

    def __init__(self):
        pass

    def roman(self,input_int):
        if input_int in ROMAN_NUMBERS_DICT:
            return ROMAN_NUMBERS_DICT[input_int]
        return 'II'