import unittest
def city_country(city, country):
    """Return a formatted city-country string."""
    return f"{city.title()}, {country.title()}"
class TestCityFunctions(unittest.TestCase):
    def test_city_country(self):
        """Test city_country() with 'santiago' and 'chile'."""
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')
if __name__ == '__main__':
    unittest.main()