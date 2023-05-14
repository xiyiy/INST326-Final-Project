import matplotlib.pyplot as plt
import seaborn as sns
import monty_hall as mh
import pandas as pd

class Plot:
    """ This class stores the data for a particular instance of 
    a simulation of the Monty Hall problem. It contains functionality 
    to export a visualization of the win percentages.
    
    Attributes:
        doors(int): The number of doors that the simulation 
        will be based on.
        
        iterations(int): The number of iterations that a 
        simulation will be based on.
        
        sequence(list): Populated by dictionaries, each containing the number of
        iterations a game was played, the win percentage for that simulation, the doors used in that
        simulation, and whether the door was switched or not for that simulation.
    """
    
    def __init__(self, doors=3, iterations=200):
        """ Create an attribute named sequence that will be a list that will 
        eventually contain dictionaries that we will use to create a data frame
        
        Args:
            doors(int): The number of doors that the simulation 
        will be based on.
        
            iterations(int): The number of iterations that a 
        simulation will be based on. 
        
        """
        self.doors = doors
        self.iterations = iterations
        self.sequence = []
        self.switch = True
        
        for i in range(1, iterations + 1):
            if (i % 2) == 0:
                self.switch = True
            else:
                self.switch = False
            
            y = mh.Simulation(doors)
            number_win = y.play_game(self.switch)
            
            self.sequence.append({
                "doors": self.doors, 
                "iterations": i, 
                "switched": self.switch, 
                "percentage": number_win})
        
        self.make_plot()
        
    def make_plot(self):
        """ Create a pandas DataFrame and use the lmplot method of seaborn in order to create a plot 
        object where x is "iterations", y is "percentage", data is the pandas DataFrame that we created 
        and "hue" is "switched".
        """
        
        sns.set_theme(color_codes=True)
        df = pd.DataFrame(self.sequence)
        sns.lmplot(x="iterations", y="percentage", data=df, hue="switched")
        plt.savefig(f"iterations_{self.iterations}_doors_{self.doors}.png")
        
if __name__ == "__main__":
    Plot(5, 100)