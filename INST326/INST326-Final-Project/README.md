# INST326 Project: Restaurant Recommender Documentation

What is the project and what does it do?
-------------
Our project is a series of programs that effectively recommend restaurants to the user based on their preferences. Additionally, users have the ability to search and view the address of the restaurants in the provided list on a map. 

How to run the program from the Command Line?
-------------
To run the program, open a terminal and ensure you are in the directory where the script is saved. The program does not take in any required command-line argument, instead, it utilizes the Tkinter GUI to maximize usability for the user. From the command line, if you are a Windows user, you can type “python restaurant.py” to bring up the GUI component of our project. If you use macOS replace “python” with “python3”. 

How to run the program?
-------------
Users should input the desired city and state in the relevant entry field. This step is mandatory to ensure accurate restaurant recommendations. Users can also provide additional details to refine their search. Users can customize their preferences based on rating, price, and food type. The rating input ranges from 1 to 5 stars, allowing users to specify their desired level of restaurant quality. The price input accepts a range from $ to $$$$, providing flexibility in selecting restaurants based on budget. Additionally, users can specify a particular food type of interest. It is important to note that selecting these preferences is entirely optional. After specifying the necessary preferences, users can proceed by clicking the "Search" button. The program will compile the information provided and generate a list of restaurant recommendations based on the specified criteria. These recommendations will be displayed in the list box located below the search button.

Interpreting the Results
-------------
The list of restaurant recommendations will be presented in a standardized format, including the restaurant name, rating, price, and address. The rating represents the average user rating for each restaurant, while the price reflects the estimated cost range (from $ to $$$$). Users can review the addresses to identify the physical location of each restaurant.

How to use the Explore a Restaurant feature? 
-------------
To explore a specific restaurant further, users can select the desired address from the list and enter it into the entry box provided below the map. Upon entering the address, users should click the "Search address" button. The program will display the restaurant's location on the map, enabling users to interact with the map by dragging or zooming in/out. This functionality allows users to explore the surroundings of the selected restaurant conveniently.

Bibliography
-------------
We utilized the documentation for the Tkinter package(https://docs.python.org/3/library/tk.html) to develop our program's graphical user interface (GUI) and optimize the user experience. This documentation played a pivotal role in guiding us through the process of creating various GUI elements and implementing their functionalities. We learned how to create entry inputs for users to input their preferences.The documentation provided clear instructions on how to incorporate search buttons that trigger the program to process user inputs and generate relevant results. Additionally, the documentation helped us understand how to incorporate a list box into the GUI. We utilized this list box to display the results of the restaurant recommendations, presenting information such as restaurant names, ratings, prices, and addresses in an organized manner.
We also took advantage of the documentation's instructions on modifying the GUI's appearance to meet both our design preferences and the users' needs. This allowed us to customize the visual aspects of the GUI, ensuring an aesthetically pleasing and user-friendly interface. 


Tom Schimanky's Github documentation (https://github.com/TomSchimansky/TkinterMapView) for the Tkintermapview package allowed us to effectively incorporate a map component. We took advantage of the ability to create map widgets, set positions, and add markers. We utilized the set_address() function to customize the address we wanted to display. We decided to let the user enter a desired address from the recommendations list and combined with the state and city entered alongside the assumption of only utilizing restaurants in the United States, we were able to convert the address to a position by the OpenStreetMap geocode service Nomatim.


In our project, we utilized the resources the Yelp developers' website (https://docs.developer.yelp.com/reference/v3_business_search) provided to enhance our program's functionality. This website served as a crucial reference for constructing appropriate functions and making efficient queries to the Yelp API. For instance, the website guided us in designing the get_price_value() function. Since the price input in our program is represented as a string ranging from $ to $$$$, we needed to convert it into integers for compatibility with the Yelp API. By consulting the website, we obtained the necessary information to transform the price input into numerical values, allowing us to effectively retrieve the associated restaurants from the Yelp dataset. Moreover, the website provided comprehensive documentation on the structure and format of various variables, such as restaurant names, ratings, prices, and addresses. This allowed us to ensure that our program aligned with the API's requirements and enabled a smooth integration of the retrieved data into our program's output.
