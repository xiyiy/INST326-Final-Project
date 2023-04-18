"""
Team Members: Xiyi Yang, Sean August, Devin Webb, Ildreed Mbami
INST326
Professor Daniel Pauw

We are utlizing TripAdvisor's restaurant dataset from Kaggle.com.
(https://www.kaggle.com/datasets/siddharthmandgi/tripadvisor-restaurant-recommendation-data-usa)

Creates a restaurant recommendation system that recommends restaurants based on the user's preferences
"""

import pandas as pd
import numpy as np
import csv

def read_restaurants(filename):
    """
    Read restaurant data from a CSV file.

    Args:
        filename: The filename of the CSV file to read.

    Returns:
        A list of dictionaries, where each dictionary represents a restaurant and contains the following keys:
        - name: the name of the restaurant
        - cuisine: the type of cuisine served
        - rating: the restaurant's rating out of 5
        - location: the city where the restaurant is located
        - price_range: the restaurant's price range (e.g. "$" for cheap, "$$" for moderate, etc.)
    """
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        restaurants = []
        for row in reader:
            restaurant = {
                'name': row['Name'],
                'Type': row['Type'],
                'rating': row['Reviews'],
                'location': row['Location'],
                'price_range': row['Price_Range']
            }
            restaurants.append(restaurant)
        return restaurants

def get_user_input(cuisine, rating, location, price_range):
    """
    Takes in the user input

    Args:
        cuisine(str): the type of cuisine served
        rating(float): the restaurant's rating out of 5
        location(str): the city where the restaurant is located
        price_range(str): the restaurant's price range

    Returns:
        cuisine, rating, location, price_range
    """
    
    cuisine = input("Enter the type of cuisine you want: ")
    rating = float(input("Enter the minimum rating you want (out of 5): "))
    location = input("Enter the location you prefer: ")
    price_range = input("Enter the price range($, $$ or $$$)")
    
    return cuisine, rating, location, price_range
    
def rec_list(cuisine, rating, location, price_range):
    """
    Creates a list of of restaurants based on the user's inputs

    Args:
        input(dict): dictionry of the user's input

    Returns:
        rec_list: A list containing the restaurants that matches the user's preferences
    """
