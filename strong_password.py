import unittest
import re

def is_strong_password(password: str) -> bool:

    has_not_the_minimun_number_of_characteres = len(password) < 6
    has_not_some_number = not(re.findall("[0-9]", password))
    has_not_capital_letters = not(re.findall("[A-Z]", password))
    has_not_non_capital_letters = not(re.findall("[a-z]", password))
    has_not_some_underscores = not(re.findall("_", password))

    if has_not_the_minimun_number_of_characteres:
        return False
    if has_not_some_number:
        return False
    if has_not_capital_letters:
        return False
    if has_not_non_capital_letters:
        return False
    if has_not_some_underscores:
        return False

    return True




class StrongPasswordShould(unittest.TestCase):

    def test_happy_test(self):
        self.assertTrue(is_strong_password("Mario_123"))

    def test_has_as_a_minimum_six_characteres(self):
        self.assertFalse(is_strong_password("23m_"))

    def test_has_some_number(self):
        self.assertFalse(is_strong_password("dsfjkd__"))

    def test_has_some_capital_letter(self):
        self.assertFalse(is_strong_password("21dfdsf3_3_3"))

    def test_has_some_non_capital_letter(self):
        self.assertFalse(is_strong_password("2A3_3_3F"))

    def test_has_some_underscore(self):
        self.assertFalse(is_strong_password("ssdSDF213"))




if __name__ == '__main__':
    unittest.main()
