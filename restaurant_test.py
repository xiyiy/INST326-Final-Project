import unittest
from unittest.mock import patch, Mock
from restaurant import search_restaurants, get_price_value, get_food_type_filter

class TestYelpRestaurantSearch(unittest.TestCase):
    
    def test_search_restaurants(self):
        with patch("yelp_restaurant_search.requests.get") as mock_get:
            mock_response = Mock()
            mock_response.text = '{"businesses": [{"name": "Restaurant A", "rating": 4.5, "price": "$$", "location": {"address1": "123 Main St"}}]}'
            mock_get.return_value = mock_response
            search_entry = Mock()
            search_entry.get.return_value = "Pizza"
            city_entry = Mock()
            city_entry.get.return_value = "New York"
            state_entry = Mock()
            state_entry.get.return_value = "NY"
            rating_entry = Mock()
            rating_entry.get.return_value = "4"
            price_entry = Mock()
            price_entry.get.return_value = "$$"
            food_type_entry = Mock()
            food_type_entry.get.return_value = "Italian"
            listbox = Mock()
            
            search_restaurants(search_entry, city_entry, state_entry, rating_entry, price_entry, food_type_entry, listbox)
            
            mock_get.assert_called_with("https://api.yelp.com/v3/businesses/search", headers={"Authorization": "Bearer "}, params={"term": "Pizza", "location": "New York, NY", "rating": 4.0, "price": "2", "categories": "italian"})
            listbox.delete.assert_called_with(0, "end")
            listbox.insert.assert_called_with("end", "Restaurant A - Rating: 4.5, Price: $$, Address: 123 Main St")

    def test_get_price_value(self):
        # Test when price_str is "$"
        price_str = "$"
        expected_output = 1
        self.assertEqual(get_price_value(price_str), expected_output)

        # Test when price_str is "$$"
        price_str = "$$"
        expected_output = 2
        self.assertEqual(get_price_value(price_str), expected_output)

        # Test when price_str is "$$$"
        price_str = "$$$"
        expected_output = 3
        self.assertEqual(get_price_value(price_str), expected_output)

        # Test when price_str is "$$$$"
        price_str = "$$$$"
        expected_output = 4
        self.assertEqual(get_price_value(price_str), expected_output)

        # Test when price_str is not a valid input
        price_str = "invalid"
        expected_output = None
        self.assertEqual(get_price_value(price_str), expected_output)

    def test_get_food_type_filter(self):
        # Test when food_type is a valid input
        food_type = "Mexican"
        expected_output = "mexican"
        self.assertEqual(get_food_type_filter(food_type), expected_output)

        # Test when food_type is an empty string
        food_type = ""
        expected_output = None
        self.assertEqual(get_food_type_filter(food_type), expected_output)

        # Test when food_type is None
        food_type = None
        expected_output = None
        self.assertEqual(get_food_type_filter(food_type), expected_output)
