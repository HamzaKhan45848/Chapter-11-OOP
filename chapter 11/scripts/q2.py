import unittest
def city_country(city, country, population=None):
    if population:
        return f"{city.title()}, {country.title()} – population {population}"
    else:
        return f"{city.title()}, {country.title()}"
class TestCityFunctions(unittest.TestCase):

    def test_city_country(self):
        formatted = city_country('santiago', 'chile')
        self.assertEqual(formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        formatted = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(formatted, 'Santiago, Chile – population 5000000')
if __name__ == '__main__':
    unittest.main()
