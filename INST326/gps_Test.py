"""Create routes between cities on a map."""
import sys
import argparse

class City:
    """
        This class holds data representing a City. We assume that 
        Cities have names and neighbors. We also assume that the Neighbor relationships have 
        associated values such as the distance between cities,
        and the interstates that connect them.
        
        Attributes: 
            name(String): The input string that 
            contains the name of the city.
            
            neighbors (dict):  Starts  off  as  an  empty  string  that  we  
            will  populate  with  the  add_neighbor() method  later.  The  keys  of  this  
            dictionary  will  be  other  City  objects  that  are  connected  to  this
            instance of City. The values of those keys are tuples 
            where the first item is the distance between
            the cities(int), and the interstate(str) that connects them.
            
    """
    def __init__(self, name):
        """
        Set the name argument to an attribute.
        Set the neighbors attribute to an empty dictionary.
        """
        self.name = name
        self.neighbors = {}

    def __repr__(self):
        """
        Returns the name attribute of the class
        """
        return self.name

    def add_neighbor(self, neighbor, distance, interstate):
        """
        Adds the neighbor city to a certain city object if it doesn't already exist
        
        Args:
            self: Instance of the class
            neighbor(City): The City object that will be connected to this instance
            distance(string): The distance between 2 cities
            interstate(string): The interstate number that connects the 2 cities
        """
        if neighbor not in self.neighbors:
            self.neighbors[neighbor] = distance, interstate
            
        if self not in neighbor.neighbors:
           neighbor.neighbors[self] = distance, interstate
           
def is_city_in_list(city_list, city):
    """Searches the city list in the Map class.
    
    Args:
        city_list(list): The list of city objects in the Map class.
        city(string): The specific City object.
    Returns:
        Boolean: True if the city is found in city_list, returns false if not.
    """
    for i in range(len(city_list)):
        if city_list[i].name == city:
            return True
    return False

def find_city_index(city_list, city):
    """Finds the index in the city list of the Map class.
    
    Args:
        city_list(list): The list of city objects in the Map class.
        city(string): The specific City object.
    Returns:
        The index of the city object identified in the list
    """
    for i in range(len(city_list)):
        if city_list[i].name == city:
            return i


class Map:
    """
    This  class  stores  the  map  data  as  a  form  of  Graph  
    where each  node  in  the  Graph  is  a  city,  and  the
    edges are represented by the relationships that the cities 
    have to each other.
    
    Attributes:
    cities (list): a list of all of the unique city objects that make 
    up the Graph structure.
    relationships (dictionary): An adjacency list that contains the
    connections of cities.
    
    """
    def __init__(self, relationships):
        """
        Iterates through the relationships dictionary being passed in
        and uses the is_city_in_list function, as well as the find_city_index 
        function to create neighbors for each city
        
        Args:
            self: The instance that we are working with
            relationships(dictionary): A  dictionary  where  the  keys  are  
            individual  cities  and  the  values  are  a
            list of tuples of the neighbor city
        """
        self.relationships = relationships
        self.cities = []

        for city in self.relationships:
            if is_city_in_list(self.cities, city) == False:

                city_object = City(city)
                self.cities.append(city_object)

            city_index = find_city_index(self.cities, city)
            

            for city_tuple in self.relationships[city]:
                if is_city_in_list(self.cities, city_tuple[0]) == False:
                    neighbor_object = City(city_tuple[0])
                    self.cities.append(neighbor_object)

                city_index2 = find_city_index(self.cities, city_tuple[0])
                
                self.cities[city_index].add_neighbor(self.cities[city_index2], city_tuple[1], city_tuple[2])
                self.cities[city_index2].add_neighbor(self.cities[city_index], city_tuple[1], city_tuple[2])



    def __repr__(self):
        """
        Returns the string representation of the city list
        """
        return str(self.cities)


def bfs(graph, start, goal):
    """ Implements  the  bfs  (Breadth  First  Search)  algorithm  to  
        find  the  shortest  paths
        between  the  two  nodes  in  a  graph  structure.
    Args:
        graph (Map object): A map object representing 
        the graph that we will be traversing.
        start (string): The start city
        goal (string): The destination city
        
    Returns:
        A list of strings (cities) that we will visit on the shortest 
        path between the start and goal cities.
    """
    explored = []
    queue = [[start]]
    if start == goal:
        return "Same Node"
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node not in explored:
            for index in range(len(graph.cities)):
                if node == graph.cities[index].name:
                    neighbor_dict = graph.cities[index].neighbors
                    break
            for city in neighbor_dict:
                new_path = list(path)
                new_path.append(city.name)
                queue.append(new_path)
                if city.name == goal:
                    return new_path

            explored.append(node)
    
    print("A connecting path doesn't exist")
    return None


def main(start, destination, graph):
    """
    This  function  will  create  a  Map  object  with  the  connections  
    data  being  passed  in.  It  will  then  use
    bfs()  to  find  the  path  between  a  start  City  and  a  
    destination  City.  It  will  parse  the  returned  value
    and instruct the user on where they should drive given a 
    start node and an end node.
    
    Args:
        start(string): The start city
        destination(string): The destination city
        graph(Map object):  A  dictionary  representing  an  adjecency  
        list  of  cities  and  the  cities  to  which  they
        connect.
    """
    map_object = Map(graph)
    instructions = bfs(map_object, start, destination)

    if instructions == None:
        sys.exit(1)
    empty_string = ""
    count = len(instructions)
    for index in range(count):
        if index == 0:
            new_string = f"Starting at {instructions[index]}"
            print(new_string)
            empty_string += new_string
            
        if index < count - 1:
            next_city = instructions[index+1]
            for next_index in range(len(map_object.cities)):
                if map_object.cities[next_index].name == instructions[index]:
                    neighbors = map_object.cities[next_index].neighbors

                    for key in neighbors:
                        if key.name == next_city:
                            new_string = f"Drive {neighbors[key][0]} miles on {neighbors[key][1]} towards {next_city}, then"
                            print(new_string)
                            empty_string += new_string
                            break
    new_string = "You will arrive at your destination"
    print(new_string)
    empty_string += new_string
    return empty_string


def parse_args(args_list):
    """Takes a list of strings from the command prompt and passes them through as 
arguments
    
    Args:
        args_list (list) : the list of strings from the command prompt
    Returns:
        args (ArgumentParser)
    """
    parser = argparse.ArgumentParser()

    parser.add_argument('--starting_city', type=str, help= 'The starting city in a route.')
    parser.add_argument('--destination_city', type=str, help= 'The destination city in a route.')

    args = parser.parse_args(args_list)

    return args


if __name__ == "__main__":

    connections = {
        "Baltimore": [("Washington", 39, "95"), ("Philadelphia", 106, "95")],
        "Washington": [("Baltimore", 39, "95"), ("Fredericksburg", 53, "95"),("Bedford", 137, "70")],
        "Fredericksburg": [("Washington", 53, "95"), ("Richmond", 60, "95")],
        "Richmond": [("Charlottesville", 71, "64"), ("Williamsburg", 51, "64"),("Durham", 151, "85")],
        "Durham": [("Richmond", 151, "85"), ("Raleigh", 29, "40"), ("Greensboro",54, "40")],
        "Raleigh": [("Durham", 29, "40"), ("Wilmington", 129, "40"), ("Richmond",171, "95")],
        "Greensboro": [("Charlotte", 92, "85"), ("Durham", 54, "40"), ("Ashville",173, "40")],
        "Ashville": [("Greensboro", 173, "40"), ("Charlotte", 130, "40"),("Knoxville", 116, "40"), ("Atlanta", 208, "85")],
        "Charlotte": [("Atlanta", 245, "85"), ("Ashville", 130, "40"),("Greensboro", 92, "85")],
        "Jacksonville": [("Atlanta", 346, "75"), ("Tallahassee", 164, "10"),("Daytona Beach", 86, "95")],
        "Daytona Beach": [("Orlando", 56, "4"), ("Miami", 95, "268")],
        "Orlando": [("Tampa", 94, "4"), ("Daytona Beach", 56, "4")],
        "Tampa": [("Miami", 281, "75"), ("Orlando", 94, "4"), ("Atlanta", 456,"75"), ("Tallahassee", 243, "98")],
        "Atlanta": [("Charlotte", 245, "85"), ("Ashville", 208, "85"),("Chattanooga", 118, "75"), ("Macon",83, "75"), ("Tampa", 456, "75"),("Jacksonville", 346, "75"), ("Tallahassee", 273, "27")],
        "Chattanooga": [("Atlanta", 118, "75"), ("Knoxville", 112, "75"),("Nashville", 134, "24"), ("Birmingham", 148, "59")],
        "Knoxville": [("Chattanooga", 112, "75"), ("Lexington", 172, "75"),("Nashville", 180, "40"), ("Ashville", 116, "40")],
        "Nashville": [("Knoxville", 180, "40"), ("Chattanooga", 134, "24"),("Birmingam", 191, "65"), ("Memphis", 212, "40"), ("Louisville", 176, "65")],
        "Louisville": [("Nashville", 176, "65"), ("Cincinnati", 100, "71"),("Indianapolis", 114, "65"), ("St. Louis", 260, "64"), ("Lexington", 78, "64")],
        "Cincinnati": [("Louisville", 100, "71"), ("Indianapolis,", 112, "74"),("Columbus", 107, "71"), ("Lexington", 83, "75"), ("Detroit", 263, "75")],
        "Columbus": [("Cincinnati", 107, "71"), ("Indianapolis", 176, "70"),("Cleveland", 143, "71"), ("Pittsburgh", 185, "70")],
        "Detroit": [("Cincinnati", 263, "75"), ("Chicago", 283, "94"),("Mississauga", 218, "401")],
        "Cleveland": [("Chicago", 344, "80"), ("Columbus", 143, "71"),("Youngstown", 75, "80"), ("Buffalo", 194, "90")],
        "Youngstown": [("Pittsburgh", 67, "76")],
        "Indianapolis": [("Columbus", 175, "70"), ("Cincinnati", 112, "74"), ("St.Louis", 242, "70"), ("Chicago", 183, "65"), ("Louisville", 114, "65"),("Mississauga", 498, "401")],
        "Pittsburg": [("Columbus", 185, "70"), ("Youngstown", 67, "76"),("Philadelphia", 304, "76"), ("New York", 391, "76"), ("Bedford", 107, "76")],
        "Bedford": [("Pittsburg", 107, "76")],  # COMEBACK
        "Chicago": [("Indianapolis", 182, "65"), ("St. Louis", 297, "55"),("Milwaukee", 92, "94"), ("Detroit", 282, "94"), ("Cleveland", 344, "90")],
        "New York": [("Philadelphia", 95, "95"), ("Albany", 156, "87"),("Scranton", 121, "80"), ("Providence,", 95, "181"), ("Pittsburgh", 389, "76")],
        "Scranton": [("Syracuse", 130, "81")],
        "Philadelphia": [("Washington", 139, "95"), ("Pittsburgh", 305, "76"), ("Baltimore", 101, "95"), ("New York", 95, "95")]
    }

    args = parse_args(sys.argv[1:])
    main(args.starting_city, args.destination_city, connections)