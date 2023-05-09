import requests
import json
import tkinter as tk
import tkintermapview

# Yelp API Key
API_KEY = "EXWS2sWe5HTCU-Rg0HqXbuLhrMPfjVBAuaXUute-zQXj6CCuQLH4lUqp0iC92b8PYpLZ5lvofohpSjSpxDxLCqOWpV7Z9vumSoQAV24O0aPV-YbPyopg0YuCLwE_ZHYx"

# Create the Tkinter GUI window
root = tk.Tk()
root.geometry("800x900")
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

# Create the search button
def search_restaurants():
    """ Scraps the API and obtain only the fields we need through get requests
    """
    # Clear any previous results
    listbox.delete(0, tk.END)
    # Clear previous markers
    map_widget.delete_all_marker()
    
    
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
        "rating": float(rating) if rating else None,
        "price": price,
        "categories": get_food_type_filter(food_type)
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
search_button.pack(pady=18)

# Create the search results listbox
listbox_frame = tk.Frame(root, bd=2, relief="groove")
listbox_frame.pack(side="left", fill="both", expand=True)

listbox_scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
listbox_scrollbar.pack(side="right", fill="y")

listbox = tk.Listbox(listbox_frame, width=50, yscrollcommand=listbox_scrollbar.set)
listbox.pack(side="left", fill="both", expand=True)

listbox_scrollbar.config(command=listbox.yview)


# Create a map 
my_label = tk.LabelFrame(root)
my_label.pack(pady=20)

map_widget = tkintermapview.TkinterMapView(my_label, width=350, height=350, corner_radius=0)

# Set address
map_widget.set_zoom(10)
   
def add_marker():
    """ Adds a marker to each address entered
    """
    address = explore_addy_input.get()
    city = city_entry.get()
    state = state_entry.get()
    country = "United States"
    full_address = f'{address}, {city}, {state}, {country}'
    
    map_widget.set_address(full_address, marker=True)
        
# Create search button for map
explore_addy = tk.Label(root, text="Enter an address to explore:")
explore_addy.pack()

# Create input box for address input
explore_addy_input = tk.Entry(root, width=30)
explore_addy_input.pack()

search_addy = tk.Button(root, text="Search Address", command=add_marker)
search_addy.pack()

map_widget.pack()


# Create the sorting dropdown menu
sort_options = ["Best Match", "Rating - High to Low", "Rating - Low to High", "Price - High to Low", "Price - Low to High"]
sort_variable = tk.StringVar(root)
sort_variable.set(sort_options[0])
sort_menu = tk.OptionMenu(root, sort_variable, *sort_options)
sort_menu.pack(pady=(18,0))

# Create the sort button
def sort_results():
    # Get the current sort option
    sort_option = sort_variable.get()

    # Get all items in the listbox
    items = listbox.get(0, tk.END)

    # Sort the items based on the current sort option
    if sort_option == "Best Match":
        items = sorted(items)
    elif sort_option == "Rating - High to Low":
        items = sorted(items, key=lambda x: float(x.split("Rating: ")[1].split(",")[0]), reverse=True)
    elif sort_option == "Rating - Low to High":
        items = sorted(items, key=lambda x: float(x.split("Rating: ")[1].split(",")[0]))
    elif sort_option == "Price - High to Low":
        items = sorted(items, key=lambda x: x.count("$"), reverse=True)
    elif sort_option == "Price - Low to High":
        items = sorted(items, key=lambda x: x.count("$"))

    # Clear the listbox and add the sorted items
    listbox.delete(0, tk.END)
    for item in items:
        listbox.insert(tk.END, item)

# Create the sort button
sort_button = tk.Button(root, text="Sort List", command=sort_results)
sort_button.pack()


def get_food_type_filter(food_type_str):
    """ Filtering the data by food types entered
    
        Args: food_type_str(str): user input of food types 
        
        Returns: a joined string of the results
    """
    # Return an empty string if no food type is specified
    if not food_type_str:
        return ""

    # Split the food type string into a list of individual food types
    food_types = [c.strip() for c in food_type_str.split(",")]

    # Create a filter string for each food type
    filters = []
    for food_type in food_types:
        filters.append(f"{food_type.lower().replace(' ', '-')}")
    
    # Join the filter strings with commas and return the result
    return ",".join(filters)

def get_price_value(price_str):
    """ Makes sure user string input is converted into 1, 2, 3, 4 used in the API
    
        Args: price_str(str): string of the price
        
        Returns: a num representation of the price
    """
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
    
# Create the label for the API attribution
attribution_label = tk.Label(root, text="Powered by Yelp", fg="#8B0000", font=("Arial", 10))
attribution_label.pack(side="bottom")

# Start the mainloop
if __name__ == "__main__":
    root.mainloop()