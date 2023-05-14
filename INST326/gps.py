"""Create routes between cities on a map."""
import sys
import argparse

class City: 
    
    def __init__(self, name): 
        """Define a __init__() and sets name and neighbors to their corresponding parameters
    
        Args:
            self: reference to the current instance of the class
            name (string): name of the city 
            neighbors (dict): set to an empty dictionary
        """
        
        self.name = name
        self.neighbors = {}
        
    def __repr__(self):
        """Returns the name attribute
    
        Args:
            self: reference to the current instance of the class
        
        Returns: name attrbiute of the instance  
        """
        
        return self.name
    
    def add_neighbor(self, neighbor, distance, interstate):
        """Populates the neighbor dictionary
    
        Args:
            self: reference to the current instance of the class
            neighbor(City): The City object that will be connected to this instance
◦           distance(str): The distance between the two cities.
◦           interstate(str): The interstate number that connects the two cities.
        """
        
        self.neighbor = neighbor
        self.distance = distance
        self.interstate = interstate
        
        #adding newNeighbor to both current city and neighboring city
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = distance, interstate
        
        #current instance
        if self not in neighbor.neighbors:
            neighbor.neighbors[self] = distance, interstate
            
def cityInList(cities, city):
    '''Searches cities list to see if city is in it
        
    Args: 
        cities(list): list of city objects
        city(str): city object
            
    Returns: 
        Boolean: True if city is in cities, otherwise False
    '''
    
    for i in range(len(cities)):
        #city names are equal
        if cities[i].name == city:
            return True
    return False
    
def getIndex(cities, city):
    '''Searches cities list for index of city
        
    Args: 
        cities(list): list of city objects
        city(str): city object
            
    Returns: 
        index of the city object
    '''
    
    for i in range(len(cities)):
        #city names are equal
        if cities[i].name == city:
            return i
            
class Map: 
    
    def __init__(self, relationships): 
        """Uses cityInList and getIndex functions to create neighbor objects 
    
        Args:
            self: reference to the current instance of the class
            relationships(dict): keys are cities and values are lists of tuples
            cities(list): list of city objects 
        """
        
        self.cities = []
        self.relationships = relationships
        
        for city in self.relationships:
            if cityInList(self.cities, city) == False:
                city_object = City(city)
                self.cities.append(city_object)

            cityIdx = getIndex(self.cities, city)
            

            for cityTuple in self.relationships[city]:
                if cityInList(self.cities, cityTuple[0]) == False:
                    neighbor = City(cityTuple[0])
                    self.cities.append(neighbor)

                cityIdx2 = getIndex(self.cities, cityTuple[0])
                
                self.cities[cityIdx].add_neighbor(self.cities[cityIdx2], cityTuple[1], cityTuple[2])
                self.cities[cityIdx2].add_neighbor(self.cities[cityIdx], cityTuple[1], cityTuple[2])
        
    def __repr__(self):
        """Returns the city list
    
        Args:
            self: reference to the current instance of the class
        
        Returns: string represetation of cities attrbiute of the instance  
        """
        return f'Map(cities={self.cities})'
        
def bfs(graph, start, goal):
    """Finds the shortest paths between two nodes in the graph
    
    Args:
        graph(Map): A map object representing the graph 
        start(str): The start city 
        goal(str): The destination city
                    
    Returns: A list of strings(cities) that we will visit on the shortest path
    """
    
    explored = []
    queue = [[start]]
    
    if start == goal:
            return [start]
        
    while queue: #not empty queue
        path = queue.pop(0)
        node = path[-1] #last item in the list of paths
        
        if node not in explored:
            for index in range(len(graph.cities)):
                if node == graph.cities[index].name:
                    neighborsDict = graph.cities[index].neighbors
                    break
            for neighbor in neighborsDict:
                #explicitly make path into a list
                new_path = list(path)
                new_path.append(neighbor.name)
                queue.append(new_path)
            
                if neighbor.name == goal:
                    return new_path
                
            explored.append(node)
            
    print("No path found")
    return None

def main(start, destination, graph):
    """Create a Map object with the connections data being passed in. 
    Use bfs() to find the path between a start City and a destination City. 
    It will parse the returned value and instruct the user on where 
    they should drive given a start node and an end node
        
    Args:
        graph(Map): A map object representing the graph 
        start(str): The start city 
        destination(str): The destination city
                    
    Returns: A string that contains printed out content
    """
    
    map = Map(graph)
    instructions = bfs(map, start, destination)
    displayStr = ""
    
    if instructions == None:
        sys.exit(1)
    
    for i in range(len(instructions)):
        if i == 0:
            print (f"Starting at {instructions[i]}\n")
            displayStr += f"Starting at {instructions[i]}\n"
    
        #if position is before last
        if i < len(instructions) - 1:
            #next to current city
            nextCity = instructions[i+1]
            
            #looks at each city obj
            for nextIdx in range(len(map.cities)):
                if map.cities[nextIdx].name == instructions[i]:
                    #neighbor tuple
                    neighbors = map.cities[nextIdx].neighbors
                
                    for key in neighbors:
                        if key.name == nextCity:
                            #neighbors[key][0] is distance, neighbors[key][1] is interstate
                            temp = f"Drive {neighbors[key][0]} miles on {neighbors[key][1]} towards {nextCity}, then"
                            print(temp)
                            displayStr += temp
                            break
                        
    temp = f"You will arrive at your destination"
    print(temp)
    displayStr += temp
    return displayStr
                  
def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """

    parser = argparse.ArgumentParser()
    
    parser.add_argument('--starting_city', type = str, help = 'The starting city in a route.')
    parser.add_argument('--destination_city', type = str, help = 'The destination city in a route.')
    
    args = parser.parse_args(args_list)
    
    return args

if __name__ == "__main__":
    connections = {  
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"), ("Bedford", 137, "70")], 
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"), ("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro", 54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond", 171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville", 173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"), ("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"), ("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"), ("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456, "75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"), ("Chattanooga", 118, "75"), ("Macon", 83, "75"), ("Tampa", 456, "75"), ("Jacksonville", 346, "75"), ("Tallahassee", 273, "27") ],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"), ("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112,"75"), ("Lexington", 172, "75"), ("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"), ("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"), ("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64") ],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"), ("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"), ("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"), ("Mississauga", 218, "401")],
        "Cleveland":[("Chicago", 344, "80"), ("Columbus", 143, "71"), ("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown":[("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St. Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"), ("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"), ("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")], #COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"), ("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"), ("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }
    
    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)
    
   