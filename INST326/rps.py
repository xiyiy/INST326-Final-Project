"""A template for a python script deliverable for INST326.
Driver: Instructor Gabriel Cruz
Navigator: None
Assignment: Template INST326
Date: 1_24_21
Challenges Encountered: ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Collaborated with Adharsh Maheswaran
"""
import sys
import argparse
import os
def determine_winner(p1, p2):
    """Determines the winner of a round of rock, paper, scissors
    
    Args: 
        p1(str): represents player 1's hand sign, either r, p, or s
        p2(str): represents player 2's hand sign, either r, p, or s
  
    Returns: 
        a string, either "tie", "player1" or "player2" signifying a tie or win
    """

    if (p1 == p2): 
        return "tie"
    elif (p1 == "p"): 
        if(p2 == "r"): 
            return "player1"
        else: 
            return "player2"
    elif (p1 == "s"):
        if(p2 == "p"): 
            return "player1"
        else: 
            return "player2"
    elif (p1 == "r"): 
        if(p2 == "s"): 
            return "player1"
        else: 
            return "player2"
    else: 
        return "error"
            
def main(player1_name, player2_name):
    """Displays the appropriate name of the winner or "Tie!" if tied
    
    Args: 
        player1_name(str): represents player 1's name for the round
        player2_name(str): represents player 2's name for the round
    
    """
 
    p1Sign = input("Enter player 1's hand shape ('r', 'p', or 's'):")
    p2Sign = input("Enter player 2's hand shape ('r', 'p', or 's'):")
      
    # Cross platform solution for clearing out a termianl/cmd prompt in Python.
    os.system('cls||clear')

    winner = determine_winner(p1Sign,p2Sign)

    if (winner == "player1"):
        print(player1_name + " wins!")
    elif (winner == "player2"):
        print(player2_name + " wins!")
    else: 
        print("Tie!")
        

def parse_args(args_list):
  """Takes a list of strings from the command prompt and passes them through as
arguments
  Args:
  args_list (list) : the list of strings from the command prompt
  Returns:
  args (ArgumentParser)
  """
  #For the sake of readability it is important to insert comments all throughout.
  #Complicated operations get a few lines of comments before the operations commence.
  #Non-obvious ones get comments at the end of the line.
  #For example:
  #This function uses the argparse module in order to parse command line arguments.
  parser = argparse.ArgumentParser() #Create an ArgumentParser object.
  #Then we will add arguments to this parser object.
  #In this case, we have a required positional argument.
  #Followed by an optional keyword argument which contains a default value.
  parser.add_argument('p1_name', type=str, help="Please enter Player1's Name")
  parser.add_argument('p2_name', type=str, help="Please enter Player2's Name")
  args = parser.parse_args(args_list) #We need to parse the list of command line arguments using this object.
  return args
if __name__ == "__main__":
  #If name == main statements are statements that basically ask:
  #Is the current script being run natively or as a module?
  #It the script is being run as a module, the block of code under this will not beexecuted.
  #If the script is being run natively, the block of code below this will be executed.
  arguments = parse_args(sys.argv[1:]) #Pass in the list of command line arguments to the parse_args function.
  #The returned object is an object with those command line arguments as attributes of an object.
  #We will pass both of these arguments into the main function.
  #Note that you do not need a main function, but you might find it helpfull.
  #You do want to make sure to have minimal code under the 'if __name__ == "__main__":' statement.
  main(arguments.p1_name, arguments.p2_name)
