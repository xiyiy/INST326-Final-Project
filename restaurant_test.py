import tkinter as tk
import unittest
from unittest.mock import patch, Mock
from restaurant import YelpRestaurantSearch

API_KEY = "EXWS2sWe5HTCU-Rg0HqXbuLhrMPfjVBAuaXUute-zQXj6CCuQLH4lUqp0iC92b8PYpLZ5lvofohpSjSpxDxLCqOWpV7Z9vumSoQAV24O0aPV-YbPyopg0YuCLwE_ZHYx"

class TestYelpRestaurantSearch(unittest.TestCase):
    def get_API(self):
        self.restaurant = YelpRestaurantSearch(API_KEY)
    
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
            
            YelpRestaurantSearch.search_restaurants(search_entry, city_entry, state_entry, rating_entry, price_entry, food_type_entry, listbox)
            
            mock_get.assert_called_with("https://api.yelp.com/v3/businesses/search", headers={"Authorization": "Bearer "}, params={"term": "Pizza", "location": "New York, NY", "rating": 4.0, "price": "2", "categories": "italian"})
            listbox.delete.assert_called_with(0, "end")
            listbox.insert.assert_called_with("end", "Restaurant A - Rating: 4.5, Price: $$, Address: 123 Main St")

    def test_get_price_value(self):
        # Test when price_str is "$"
        price_str = "$"
        expected_output = 1
        self.assertEqual(YelpRestaurantSearch.get_price_value(price_str), expected_output)

        # Test when price_str is "$$"
        price_str = "$$"
        expected_output = 2
        self.assertEqual(YelpRestaurantSearch.get_price_value(price_str), expected_output)

        # Test when price_str is "$$$"
        price_str = "$$$"
        expected_output = 3
        self.assertEqual(YelpRestaurantSearch.get_price_value(price_str), expected_output)

        # Test when price_str is "$$$$"
        price_str = "$$$$"
        expected_output = 4
        self.assertEqual(YelpRestaurantSearch.get_price_value(price_str), expected_output)

        # Test when price_str is not a valid input
        price_str = "invalid"
        expected_output = None
        self.assertEqual(YelpRestaurantSearch.get_price_value(price_str), expected_output)

    def test_get_food_type_filter(self):
        # Test when food_type is a valid input
        food_type = "Mexican"
        expected_output = "mexican"
        self.assertEqual(YelpRestaurantSearch.get_food_type_filter(food_type), expected_output)

        # Test when food_type is an empty string
        food_type = ""
        expected_output = None
        self.assertEqual(YelpRestaurantSearch.get_food_type_filter(food_type), expected_output)

        # Test when food_type is None
        food_type = None
        expected_output = None
        self.assertEqual(YelpRestaurantSearch.get_food_type_filter(food_type), expected_output)
        
    def test_get_search_params(self):
          # Test the get_search_params method
        # Define test inputs
        search_term = "pizza"
        city = "New York"
        state = "NY"
        rating = "4"
        price = "$$"
        food_type = "Italian"

        # Set the input values in the entry fields
        YelpRestaurantSearch.search_entry.insert(0, search_term)
        YelpRestaurantSearch.city_entry.insert(0, city)
        YelpRestaurantSearch.state_entry.insert(0, state)
        YelpRestaurantSearch.rating_entry.insert(0, rating)
        YelpRestaurantSearch.price_entry.insert(0, price)
        YelpRestaurantSearch.food_type_entry.insert(0, food_type)

        # Call the get_search_params method
        params = YelpRestaurantSearch.get_search_params()

        # Assert the expected output
        expected_params = {
            "term": search_term,
            "location": f"{city}, {state}",
            "rating": float(rating),
            "price": "2",
            "categories": "italian"
        }
        self.assertEqual(params, expected_params)
        
    def test_sort_results(self):
        # Test the sort_results method
        # Define test inputs
        sort_option = "Rating - High to Low"

        # Set the input values in the entry fields
        YelpRestaurantSearch.sort_variable.set(sort_option)

        # Insert some test items into the listbox
        YelpRestaurantSearch.listbox.insert(tk.END, "Restaurant A - Rating: 4.5, Price: $$")
        YelpRestaurantSearch.listbox.insert(tk.END, "Restaurant B - Rating: 3.7, Price: $")
        YelpRestaurantSearch.listbox.insert(tk.END, "Restaurant C - Rating: 4.2, Price: $$$$")
        YelpRestaurantSearch.listbox.insert(tk.END, "Restaurant D - Rating: 4.0, Price: $$$")

        # Call the sort_results method
        YelpRestaurantSearch.sort_results()

        # Get the sorted items from the listbox
        sorted_items = YelpRestaurantSearch.listbox.get(0, tk.END)

        # Assert the expected output
        expected_items = [
            "Restaurant A - Rating: 4.5, Price: $$",
            "Restaurant C - Rating: 4.2, Price: $$$$",
            "Restaurant D - Rating: 4.0, Price: $$$",
            "Restaurant B - Rating: 3.7, Price: $"
        ]
        self.assertEqual(sorted_items, expected_items)
        
    def test_add_marker(self):
        # Test the add_marker method
        address = "405 N Charles St."
        city = "Baltimore"
        state = "Maryland"
        
        # Set the input values in the entry fields
        YelpRestaurantSearch.explore_addy_input.insert(0, address)
        YelpRestaurantSearch.city_entry.insert(0, city)
        YelpRestaurantSearch.state_entry.insert(0, state)
        
        # Call the add_marker method
        YelpRestaurantSearch.add_marker()
        marker_present = YelpRestaurantSearch.map_widget.has_marker()
        self.assertTrue(marker_present)
        
if __name__ == '__main__':
    unittest.main()
