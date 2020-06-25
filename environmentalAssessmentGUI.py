#20200522_environmentalAssessmentGUI_v1.1
#ethanMclachlan with help from Chase Meister and mlj

##change log
#1.1 have everything working
#1.2 figure out how to only ask a question if item requirements are met

# import the library
from appJar import gui

##Variables
#items on pat
items    = ["plastic bottle","pile of leaves","hobo","plastic bag","the gardeners lost secateurs","dog poo",
            "nylon fishing line","descarded fish and chips in paper","batteries","someone littering"]


import random  #gets random for random number; oldMan, bossFight and chicken.       
score = 0  #score is split into categories to tell you how well you did.
holding = []  #list of items you are holding.        

###############################################################################################################################
class Tile:
    def __init__(self, text, yesLocation, noLocation, isContinue):
        self.text = text
        self.yesLocation = yesLocation
        self.noLocation = noLocation
        self.isContinue = isContinue
        
    def displayTile(self):
        app.setLabel("text",self.text)

def updateButtons():
    if(tile[current].isContinue):
        app.hideButton("No")
        app.hideButton("Yes")
        app.showButton("Continue")
    else:
        app.hideButton("Continue")
        app.showButton("Yes")   
        app.showButton("No")

def press(button):
    global current
    if(tile[current].isContinue):
        if button == "Continue":
            current = tile[current].yesLocation
    else:
        if button == "Yes":
            current = tile[current].yesLocation
            tile[current].displayTile()
        elif button == "No":
            current = tile[current].noLocation
            tile[current].displayTile()        
    updateButtons()
          
current = 0 # so it starts at tile 0 in the list

# create a GUI variable called app
app = gui("Login Window","400x200")
app.addLabel("text")
app.addButtons(["Yes","No"],press)
app.addButton("Continue",press)

# question/statement, what it goes to if you press yes or continue, what it goes to if you press no, false is yes/no and true is continue.
tile=[Tile(".... You come across a "+(obstacles[0])+"""!     
Would you like to pick up the """+(obstacles[0])+"?",1 and holding.append(obstacles[0]),2,False),  #Need a starting cover tile and a finishing stats tile.
Tile("question2?",3,3,True),
Tile("question3?",3,3,True),
Tile("4?",(2 if (obstacles[0]) in holding else 1),3,False)]

updateButtons()
tile[current].displayTile()
# start the GUI
app.go()

