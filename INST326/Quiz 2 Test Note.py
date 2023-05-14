from random import randint
TEAMS = ["Nice","Marseille","Paris","Saint-Etienne","Lille","Lyon","Bordeaux","Lens","Rennes","Troyes"]

class League:
    def __init__(self, teams):
        self.teams = teams
        self.results = []
    
    def simulate(self):
        for team in self.teams:
            numWins = randint(0,38)
            numLose = randint(0, numWins)
            draws = 38 - numWins - numLose 
            scores = {"Wins": numWins, "Losses": numLose, "Draws": draws}
            team_record = (team, scores)
            self.results.append(team_record) 
            
if __name__ == "__main__":
    league = League(TEAMS)
    league.simulate()
    print(league.results)
        
        
    