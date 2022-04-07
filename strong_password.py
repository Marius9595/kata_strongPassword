import unittest
import re

def is_strong_password(password: str) -> bool:

    if len(password) < 6:
        return False

    if not (re.findall("[0-9]", password)):
        return False

    return True




class StrongPasswordShould(unittest.TestCase):

    def test_happy_test(self):
        self.assertTrue(is_strong_password("Mario_123"))

    def test_has_as_a_minimum_six_characteres(self):
        self.assertFalse(is_strong_password("23m_"))

    def test_has_some_number(self):
        self.assertFalse(is_strong_password("dsfjkd__"))




if __name__ == '__main__':
    unittest.main()
