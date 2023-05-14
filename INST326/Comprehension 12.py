""" extracts the location for each sighting in 
the database and creates a tally of sightings by city
"""
import requests
from bs4 import BeautifulSoup

class UFO: 
    """As you read in records, keep track of how 
    many reports there are for each city. You will 
    likely need a data structure to connect city and 
    state names to your objects. When you get a new report 
    for a city/state, increment the variable that tracks 
    the number of reports.
    """
    def __init__(self, city, state):
        self.city = city
        self.state = state 
        self.numReports = 1
    
    def incCount(self):
        self.numReports += 1
        

def getHtml(url):
    with requests.get(url) as response:
        html = response.content
    return html

def parseHtml(html):
    soup = BeautifulSoup(html, "html.parser")
    table = soup.find("table")
    rows = table.find_all("tr")[1:]
    
    sightings = []
    
    for row in rows: 
        #find cols 
        cols = row.find_all("td")
        city_state = cols[1].text.strip().split(", ")
        if len(city_state) >= 2:
            city = city_state[0]
            state = city_state[1]
        
        found = False
        for sighting in sightings:
            #if city and state match a sighting in sightings, inc count
            if sighting.city == city and sighting.state == state:
                sighting.incCount()
                found = True
                break 
        if not found: #no such sighting in sightings
            #add a UFO object into sightings
            sightings.append(UFO(city, state)) 
            
    return sightings

def output(sightings):
    with open("output.txt", "w") as file:
        for sighting in sightings:
            file.write(f"{sighting.city},{sighting.state}\t{sighting.numReports}\n")
            
if __name__ == '__main__':
    url1 = "http://www.cs.umd.edu/~golbeck/INST326/ndxe201903.html"
    url2 = "http://www.cs.umd.edu/~golbeck/INST326/ndxe201902.html"
    
    html1 = getHtml(url1)
    html2 = getHtml(url2)
    
    sightings1 = parseHtml(html1)
    sightings2 = parseHtml(html2)
    
    output(sightings1)
    output(sightings2)
        