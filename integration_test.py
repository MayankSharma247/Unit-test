import unittest

class TestRollNumberColumn(unittest.TestCase):
    
    def test_valid_roll_numbers(self):
        """
        Test case to check if roll numbers are valid.
        """
        valid_roll_numbers = [1001, 2002, 3003, 4004, 5005]
        for roll_number in valid_roll_numbers:
            with self.subTest(roll_number=roll_number):
                self.assertTrue(is_valid_roll_number(roll_number))

    # def test_invalid_roll_numbers(self):
    #     """
    #     Test case to check if invalid roll numbers are detected.
    #     """
    #     invalid_roll_numbers = [-1001, 0, 999, 6000]
    #     for roll_number in invalid_roll_numbers:
    #         with self.subTest(roll_number=roll_number):
    #             self.assertFalse(is_valid_roll_number(roll_number))

    def test_zero_as_roll_number(self):
        """
        Test case to check handling of zero as a roll number.
        """
        self.assertFalse(is_valid_roll_number(0))

    def test_large_roll_number(self):
        """
        Test case to check handling of large roll numbers.
        """
        self.assertFalse(is_valid_roll_number(10000))

    # Add more test cases as needed...

def is_valid_roll_number(roll_number):
    """
    Function to check if a roll number is valid.
    
    Args:
    roll_number (int): The roll number to validate.
    
    Returns:
    bool: True if the roll number is valid, False otherwise.
    """
    if roll_number > 0 and roll_number <= 5000:
        return True
    return False

if __name__ == "__main__":
    unittest.main()
