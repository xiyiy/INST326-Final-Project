import requests
import json
import tkinter as tk

# Yelp API Key
API_KEY = "EXWS2sWe5HTCU-Rg0HqXbuLhrMPfjVBAuaXUute-zQXj6CCuQLH4lUqp0iC92b8PYpLZ5lvofohpSjSpxDxLCqOWpV7Z9vumSoQAV24O0aPV-YbPyopg0YuCLwE_ZHYx"

# Create the Tkinter GUI window
root = tk.Tk()
root.geometry("800x600")
root.title("Yelp Restaurant Search")

root.configure(bg='#FFFFFF')

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

rating_label = tk.Label(root, text="rating:")
rating_label.pack()
rating_entry = tk.Entry(root, width=30)
rating_entry.pack()

price_label = tk.Label(root, text="price:")
price_label.pack()
price_entry = tk.Entry(root, width=30)
price_entry.pack()

food_type_label = tk.Label(root, text="Food Type:")
food_type_label.pack()
food_type_entry = tk.Entry(root, width=30)
food_type_entry.pack()

# Create the sorting dropdown menu
sort_options = ["Best Match", "Rating - High to Low", "Rating - Low to High", "Price - High to Low", "Price - Low to High"]
sort_variable = tk.StringVar(root)
sort_variable.set(sort_options[0])
sort_menu = tk.OptionMenu(root, sort_variable, *sort_options)
sort_menu.pack()

# Create the search results listbox
listbox_frame = tk.Frame(root, bd=2, relief="groove")
listbox_frame.pack(side="left", fill="both", expand=True)

listbox_scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
listbox_scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(listbox_frame, width=50, yscrollcommand=listbox_scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)

listbox_scrollbar.config(command=listbox.yview)


# Create the search button
def search_restaurants():
    # Clear any previous results
    listbox.delete(0, tk.END)
    

    # Get the search term and parameters from the entry fields
    search_term = search_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    rating = rating_entry.get()
    price_str = price_entry.get()
    food_type = food_type_entry.get()
    price = get_price_value(price_str)
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
def get_price_value(price_str):
    if price_str == '$':
        return '1'
    elif price_str == '$$':
        return '2'
    elif price_str == '$$$':
        return '3'
    elif price_str == '$$$$':
        return '4'
    else:
        return None   
# Create the search button
search_button = tk.Button(root, text="Search", command=search_restaurants)
search_button.pack()
if __name__ == "__main__":
    root.mainloop()