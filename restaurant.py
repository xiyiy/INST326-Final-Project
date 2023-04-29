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

def get_user_input():
    """
    Takes in the user input

    Args:
        cuisine(str): the type of cuisine served
        rating(float): the restaurant's rating out of 5
        location(str): the city where the restaurant is located
        price_range(str): the restaurant's price range

    Returns:
        user_preference(dict): dictionary of the user preferences
    """
    user_preference = {}
    
    cuisine = input("Enter the type of cuisine you want: ")
    user_preference['cuisine'] = cuisine
    
    rating = input("Enter the minimum rating you want (out of 5): ")
    user_preference['rating'] = rating
    
    city = input("Enter the state you prefer: ")
    state = input("Enter the city you prefer: ")
    user_preference['location'] = city + state 
    
    price_range = input("Enter the price range($, $$ or $$$)")
    user_preference['price_range'] = price_range 
    
    return user_preference

def get_rec_list(user_preference, restaurants):
    """
    Creates a list of of restaurants based on the user's inputs

    Args:
        user_preference(dict): dictionry of the user's input
        restaurants(list): list of resturants from API

    Returns:
        rec_list: A list containing the restaurants that matches the user's preferences
    """

    rec_list = []
    for restaurant in restaurants:
        #if cuisine match or user preference is empty
        if ((restaurant['cuisine'] == user_preference['cuisine'] or user_preference['cuisine'] == " ") and
            (restaurant['rating'] >= user_preference['rating'] or user_preference['rating'] == " ") and
            (restaurant['location'] == user_preference['location'] or user_preference['location'] == " ") and
            (restaurant['price_range'] == user_preference['price_range'] or user_preference['price_range'] == " ")):
            rec_list.append(restaurant['name'])
    return rec_list
                
