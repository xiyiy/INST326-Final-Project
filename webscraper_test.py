import unittest
import tkinter as tk
from webscraper_API import search_restaurants

class YelpRestaurantSearchGUITest(unittest.TestCase):

    def setUp(self):
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("Yelp Restaurant Search")

        self.search_label = tk.Label(self.root, text="Search for a Restaurant:")
        self.search_label.pack()
        self.search_entry = tk.Entry(self.root, width=50)
        self.search_entry.pack()

        self.city_label = tk.Label(self.root, text="City:")
        self.city_label.pack()
        self.city_entry = tk.Entry(self.root, width=50)
        self.city_entry.pack()

        self.state_label = tk.Label(self.root, text="State:")
        self.state_label.pack()
        self.state_entry = tk.Entry(self.root, width=50)
        self.state_entry.pack()

        self.rating_label = tk.Label(self.root, text="Rating:")
        self.rating_label.pack()
        self.rating_entry = tk.Entry(self.root, width=50)
        self.rating_entry.pack()

        self.price_label = tk.Label(self.root, text="Price:")
        self.price_label.pack()
        self.price_entry = tk.Entry(self.root, width=50)
        self.price_entry.pack()

        self.food_type_label = tk.Label(self.root, text="Food Type:")
        self.food_type_label.pack()
        self.food_type_entry = tk.Entry(self.root, width=50)
        self.food_type_entry.pack()

        self.listbox = tk.Listbox(self.root, width=80)
        self.listbox.pack()

        self.search_button = tk.Button(self.root, text="Search", command=search_restaurants)
        self.search_button.pack()

    def test_search(self):
        # Set the search parameters
        self.search_entry.insert(0, "sushi")
        self.city_entry.insert(0, "San Francisco")
        self.state_entry.insert(0, "CA")
        self.rating_entry.insert(0, "4.0")
        self.price_entry.insert(0, "2")
        self.food_type_entry.insert(0, "Japanese")

        # Click the search button
        self.search_button.invoke()

        # Check that the listbox contains at least one item
        self.assertGreater(self.listbox.size(), 0)

    def tearDown(self):
        self.root.destroy()

if __name__ == '__main__':
    unittest.main()