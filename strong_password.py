import unittest

def is_strong_password(password: str) -> bool:
    return True




class StrongPasswordShould(unittest.TestCase):

    def test_happy_test(self):
        self.assertTrue(is_strong_password("Mario_123"))

    def test_has_as_a_minimum_six_characteres(self):
        self.assertFalse(is_strong_password("23"))
        self.assertFalse(is_strong_password("12_Mar"))




if __name__ == '__main__':
    unittest.main()
