import unittest
import requests
import json
import tkinter as tk
from unittest.mock import patch, Mock
import tkintermapview

from restaurant import YelpRestaurantSearch

class TestYelpRestaurantSearch(unittest.TestCase):

    def setUp(self):
        self.API_KEY = "TEST_API_KEY"
        self.search = YelpRestaurantSearch(self.API_KEY)

    def test_create_widgets(self):
        self.search.create_widgets()
        self.assertIsInstance(self.search.search_entry, tk.Entry)
        self.assertIsInstance(self.search.city_entry, tk.Entry)
        self.assertIsInstance(self.search.state_entry, tk.Entry)
        self.assertIsInstance(self.search.price_entry, tk.Entry)
        self.assertIsInstance(self.search.food_type_entry, tk.Entry)
        self.assertIsInstance(self.search.listbox_frame, tk.Frame)
        self.assertIsInstance(self.search.listbox_scrollbar, tk.Scrollbar)
        self.assertIsInstance(self.search.listbox, tk.Listbox)
        self.assertIsInstance(self.search.map_widget, tkintermapview.TkinterMapView)
        self.assertIsInstance(self.search.explore_addy_input, tk.Entry)
        self.assertIsInstance(self.search.sort_variable, tk.StringVar)
        self.assertIsInstance(self.search.sort_menu, tk.OptionMenu)
        self.assertIsInstance(self.search.sort_button, tk.Button)

    def get_search_params(self):
        search_term = self.search_entry.get().strip()
        city = self.city_entry.get().strip()
        state = self.state_entry.get().strip()
        price = self.price_entry.get().strip()

    # split the food_type_entry value by comma to create a list of categories
        food_type = self.food_type_entry.get().strip().split(',')

        if state:
            location = f"{city}, {state}"
        else:
            location = city

    # map the price value to Yelp's price range (1-4)
        price_range = {"$": "1", "$$": "2", "$$$": "3", "$$$$": "4"}
        price_param = price_range.get(price, "")

        params = {
            "term": search_term,
            "location": location,
            "price": price_param,
            "categories": food_type
        }

        return params

    @patch('requests.get')
    def test_search_restaurants(self, mock_get):
        mock_data = {'businesses': [
            {'id': '123', 'name': 'Pizza Palace', 'location': {'address1': '123 Main St', 'city': 'New York'}},
            {'id': '456', 'name': 'Pizza Express', 'location': {'address1': '456 Broadway', 'city': 'New York'}}
        ]}
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.text = json.dumps(mock_data)
        mock_get.return_value = mock_response

        self.search.search_entry.insert(0, "Pizza")
        self.search.city_entry.insert(0, "New York")
        self.search.state_entry.insert(0, "NY")
        self.search.price_entry.insert(0, "$$")
        self.search.food_type_entry.insert(0, "Italian")
        self.search.search_restaurants()

        self.assertEqual(len(self.search.listbox.get(0, tk.END)), 2)
        self.assertEqual(self.search.listbox.get(0), "Pizza Palace - Rating: None, Price: None, Address: 123 Main St")
        self.assertEqual(self.search.listbox.get(1), "Pizza Express - Rating: None, Price: None, Address: 456 Broadway")

    def test_add_marker(self):
        self.search.map_widget = Mock()
        self.search.explore_addy_input.insert(0, "1600 Pennsylvania Ave NW")
        self.search.city_entry.insert(0, "Washington")
        self.search.state_entry.insert(0, "DC")
        self.search.add_marker()
        expected_address = '1600 Pennsylvania Ave NW, Washington, DC, United States'
        self.search.map_widget.set_address.assert_called_once_with(expected_address, marker=True)
    
    def test_get_food_type_filter(self):
        self.assertEqual(self.search.get_food_type_filter("Pizza, Burgers, Sandwiches"), "pizza,burgers,sandwiches")

    def test_get_price_value(self):
        self.assertEqual(self.search.get_price_value("$"), "1")
        self.assertEqual(self.search.get_price_value("$$"), "2")
        self.assertEqual(self.search.get_price_value("$$$"), "3")
        self.assertEqual(self.search.get_price_value("$$$$"), "4")
        self.assertEqual(self.search.get_price_value(""), None)
        
if __name__ == '__main__':
    unittest.main()
