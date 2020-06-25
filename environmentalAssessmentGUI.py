#20200520_environmentalAssessmentGUI_v1
#ethanMclachlan with help from Chase Meister and mlj

# import the library
from appJar import gui

#Class
class Obstacle:
    def __init__(self, name, score, kills=None):
        self.name = name
        self.score = score
        self.kills = kills

    def throw_away(self):
        global saved, killed, holding

        if self.kills is not None:
            if self.kills in saved:
                saved.remove(self.kills)  
            killed.append(self.kills)
        if self in holding:
            holding.remove(self) 

    def pick_up(self): #and just get points
        global saved, score, holding

        if self.kills is not None:
            saved.append(self.kills)
        score += self.score  #adds points to the score
        holding.append(self)  #adds the item to holding so they can use it later on.       

##Variables
#[item on path (problems), points for resolving problem, what problem impacts]
obstacles = [Obstacle("plastic bottle",10,"a dolphin"),  #this list needs to be after the class as the class defines the Obstacle
            Obstacle("pile of leaves",2,None),
            Obstacle("hobo",10,None),
            Obstacle("plastic bag",20,"two aqua turtles"),
            Obstacle("the gardeners lost secateurs",50,"a small child"),
            Obstacle("dog poo",15,"someones shoe"),
            Obstacle("nylon fishing line",20,"seal"),
            Obstacle("descarded fish and chips in paper",10,"five seagulls"),
            Obstacle("batteries",50,"a school of fish"),
            Obstacle("someone littering",50,"a whale")]

import time  #gets time for sleeps inbetween tiles and new groups of action
import random  #gets random for random number; oldMan, bossFight and chicken.
playAgain = ""  #will be changed to Y or N depending if user wants to play again. 
        
class tiles():
    
    def __init__(self, saved, killed, score, status, holding):
        self.saved = ["You saved:","Nothing!"]  #list of wildlife saved.
        self.killed = ["You killed:","Nothing!"]  #list of wildlife killed.
        self.score = 0  #score is split into categories to tell you how well you did.
        self.status = "still_going"  #changes to "GAMEOVER" to skip tiles if you do something bad.
        self.holding = []  #list of items you are holding.        

###############################################################################################################################
class Tile:
    def __init__(self, text, yesLocation, noLocation):
        self.text = text
        self.yesLocation = yesLocation
        self.noLocation = noLocation
        
    def displayTile(self):
        app.setLabel("text",self.text)
   
def press(button):
    global current
    if button == "Yes":
        current = tile[current].yesLocation
        tile[current].displayTile()
    elif button == "No":
        current = tile[current].noLocation
        tile[current].displayTile()        
          
current = 0 # so it starts at tile 0 in the list

# create a GUI variable called app
app = gui("Login Window","400x200")
app.addLabel("text")
app.addButtons(["Yes","No"],press)


tile=[Tile(".... You come across a "+(obstacles[0].name)+"""!
Would you like to pick up the """+(obstacles[0].name)+"?",1,2),  #Need a starting cover tile and a finishing stats tile.
Tile("question2?",3,3),
Tile("question3?",2,3),
Tile("4?",2,3)]

tile[current].displayTile()
# start the GUI
app.go()