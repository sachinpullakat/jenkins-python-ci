import unittest
from app import add, subtract, multiply,square

class TestApp(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)

    def test_square(self):
        self.assertEqual(square(5), 25)

if __name__ == "__main__":
    unittest.main(verbosity=2)
