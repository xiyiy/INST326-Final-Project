import requests
import json
import tkinter as tk
import io

# Yelp API Key
API_KEY = "EXWS2sWe5HTCU-Rg0HqXbuLhrMPfjVBAuaXUute-zQXj6CCuQLH4lUqp0iC92b8PYpLZ5lvofohpSjSpxDxLCqOWpV7Z9vumSoQAV24O0aPV-YbPyopg0YuCLwE_ZHYx"

# Create the Tkinter GUI window
root = tk.Tk()
root.geometry("600x400")
root.title("Yelp Restaurant Search")

root.configure(bg='#c41200')

# Create the search box label and entry field
search_label = tk.Label(root, text="Search for a Restaurant:")
search_label.pack()
search_entry = tk.Entry(root, width=30)
search_entry.pack()

# Create the search parameters labels and entry fields
city_label = tk.Label(root, text="City:")
city_label.pack()
city_entry = tk.Entry(root, width=30)
city_entry.pack()

state_label = tk.Label(root, text="State:")
state_label.pack()
state_entry = tk.Entry(root, width=30)
state_entry.pack()

rating_label = tk.Label(root, text="Rating:")
rating_label.pack()
rating_entry = tk.Entry(root, width=30)
rating_entry.pack()

price_label = tk.Label(root, text="Price:")
price_label.pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

food_type_label = tk.Label(root, text="Food Type:")
food_type_label.pack()
food_type_entry = tk.Entry(root, width=30)
food_type_entry.pack()

# Create the search results listbox
listbox = tk.Listbox(root, width=50)
listbox.pack()

# Create the search button
def search_restaurants():
    # Clear any previous results
    listbox.delete(0, tk.END)
    

    # Get the search term and parameters from the entry fields
    search_term = search_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    rating = rating_entry.get()
    price = price_entry.get()
    food_type = food_type_entry.get()

    # Create the search parameters dictionary
    params = {
        "term": search_term,
        "location": f"{city}, {state}",
        "rating": rating,
        "price": price,
        "categories": food_type
    }
    # Remove any parameters that are not provided by the user
    params = {k: v for k, v in params.items() if v}

    # Make the API request
    headers = {
        "Authorization": "Bearer " + API_KEY
    }
    response = requests.get("https://api.yelp.com/v3/businesses/search", headers=headers, params=params)
    data = json.loads(response.text)

    # Loop through the results and add them to the listbox
    businesses = data.get("businesses", [])
    for business in businesses:
        name = business.get("name")
        rating = business.get("rating")
        price = business.get("price")
        address = business.get("location", {}).get("address1")
        listbox.insert(tk.END, f"{name} - Rating: {rating}, Price: {price}, Address: {address}")

# Create the search button
search_button = tk.Button(root, text="Search", command=search_restaurants)
search_button.pack()

root.mainloop()