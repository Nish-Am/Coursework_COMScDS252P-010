import unittest
from person import Person

class UnitTestPerson(unittest.TestCase):

    # Test valid Person creation
    '''
    def test_valid_person(self):
        p = Person("Alice", 101, "alice@uni.edu", "+123456789")
        self.assertEqual(p.name, "Alice")
        self.assertEqual(p.email, "alice@uni.edu")
        self.assertEqual(p.phone, "+123456789")
    '''

    # Test invalid name (contains number)
    def test_invalid_name(self):
        with self.assertRaises(ValueError) as context:
            Person("Bob123", 102, "bob@uni.edu", "12345")
        self.assertIn("Invalid name", str(context.exception))

    # Test invalid email (missing @)
    def test_invalid_email(self):
        with self.assertRaises(ValueError) as context:
            Person("Charlie", 103, "charlie.uni.edu", "+987654321")
        self.assertIn("Invalid email", str(context.exception))

    # Test invalid phone (invalid characters)
    def test_invalid_phone(self):
        with self.assertRaises(ValueError) as context:
            Person("David", 104, "david@uni.edu", "123-456-789")
        self.assertIn("Invalid phone", str(context.exception))

    if __name__ == '__main__':
        unittest.main()