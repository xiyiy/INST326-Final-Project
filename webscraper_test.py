import unittest
from restaurant import read_restaurants

class TestScraper(unittest.TestCase):
    
    def test_read_restaurants(self):
        # Test that the function returns a list
        restaurants = read_restaurants('TripAdvisor_RestauarantRecommendation.csv')
        self.assertIsInstance(restaurants, list)
        
        # Test that each item in the list is a dictionary
        for restaurant in restaurants:
            self.assertIsInstance(restaurant, dict)
        
        # Test that each dictionary contains the expected keys
        expected_keys = ['name', 'Type', 'rating', 'location', 'price_range']
        for restaurant in restaurants:
            self.assertCountEqual(list(restaurant.keys()), expected_keys)
        
        # Test that the function returns the expected number of restaurants
        
        
        # Test that the function correctly reads data from the CSV file
        expected_first_restaurant = {
            'name': 'Coach House Diner',
            'Type': ' Diner, American, Vegetarian Friendly',
            'rating': '4 of 5 bubbles',
            'location': 'Hackensack, NJ 07601-6337',
            'price_range': '$$ - $$$'
        }
        self.assertEqual(restaurants[1], expected_first_restaurant)
        
if __name__ == '__main__':
    unittest.main() 
    
