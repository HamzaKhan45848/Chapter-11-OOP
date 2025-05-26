import unittest

class Employee:
    def __init__(self, first_name, last_name, annual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary

    def give_raise(self, amount=5000):
        """Add raise amount to the annual salary (default is $5,000)."""
        self.annual_salary += amount
class TestEmployee(unittest.TestCase):

    def setUp(self):
        """Create an employee instance to use in all test methods."""
        self.employee = Employee('John', 'Doe', 50000)

    def test_give_default_raise(self):
        """Test the default raise of $5,000."""
        self.employee.give_raise()
        self.assertEqual(self.employee.annual_salary, 55000)

    def test_give_custom_raise(self):
        """Test a custom raise amount."""
        self.employee.give_raise(10000)
        self.assertEqual(self.employee.annual_salary, 60000)
if __name__ == '__main__':
    unittest.main()