import random 

class Simulation:
    """ Simulation should take an attribute, an integer, which represents the amount of doors that the
    simulation will use to play the game.

    Attributes: 
        numdoors(int): the number of doors that will be used to play the game.
    """
    
    def __init__(self, numdoors):
        """Set an attribute named numdoors that will be the number of doors that will be used to
        play the game
        """
        self.numdoors = numdoors
        
    def set_random_doors(self):
        """Create a list containing “zonk” strings and replace one of those items in
        the list to the string “car” at random. 

        Returns:
            a list of indexes
        """
        
        random_num = random.randint(0,self.numdoors - 1)
        zonk_list = ["zonk"] * self.numdoors
        zonk_list[random_num] = "car"
        
        return zonk_list
    
    def choose_doors(self):
        """ Call set_random_doors() and save the list to a variable. Pick and remove a random item
        from the this list which represents the door that the user/contestant has chosen. It should
        then pick and remove a random door from the list as the alternate door. 
        
        Returns: tuple of the contestant door and the alternate door
        """
        
        game_list = self.set_random_doors()
        door_option = int(random.randint(0, len(game_list) - 1))
        door_option = game_list[door_option]
        game_list.remove("zonk")
        game_list.remove(door_option)
        
        alt_choice = int(random.randint(0, len(game_list) - 1))
        alt_choice = game_list[alt_choice]
        
        return (door_option, alt_choice)
    
    def play_game(self, switch = False, iterations = 1):
        """ Stimulate the Monty Hall game based on the iterations of the user
        
        Args: 
            switch(boolean): determines whether a contestant decides to switch their door when playing, default is false
            iterations(int): Default value of 1; The number of times that a person will play the game. 
        
        Returns: 
            A float of the percentage of the amount of times that the game won
        """
        self.wins = 0
        
        for i in range(iterations):
            (user_door, alternate_door) = self.choose_doors()
            if alternate_door == "car" and switch == True:
                self.wins += 1
                
            if user_door == "car" and switch == False:
                
                self.wins += 1
                    
        return float(self.wins/iterations)
    
if __name__ == "__main__":
    game1 = Simulation(3)
    print(game1.play_game(True, 1000))
                