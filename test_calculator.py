import unittest
from calculator import add, subtract, multiply, divide
from app import app

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(10, 5), 15)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(10, 5), 5)
        self.assertEqual(subtract(-1, 1), -2)

    def test_multiply(self):
        self.assertEqual(multiply(10, 5), 50)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(0, 5), 0)

    def test_divide(self):
        self.assertEqual(divide(10, 5), 2)
        self.assertEqual(divide(-1, 1), -1)
        with self.assertRaises(ValueError):
            divide(10, 0)

class TestFlask(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_index_get(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Calculator', response.data)

    def test_index_post(self):
        response = self.app.post('/', data={'num1': '10', 'num2': '5', 'operator': '+'})
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Result: 15.0', response.data)


if __name__ == '__main__':
    unittest.main()
