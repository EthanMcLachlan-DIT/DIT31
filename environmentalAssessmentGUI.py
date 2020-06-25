#20200530_environmentalAssessmentGUI_v1.22
#ethanMclachlan with help from Chase Meister, T Bone and mlj

##change log
#1.3 when everything works start adding game tiles

# import the library
from appJar import gui

##Variables
#items on pat
items = ["plastic bottle","pile of leaves","hobo","plastic bag","the gardeners lost secateurs","dog poo",
        "nylon fishing line","descarded fish and chips in paper","batteries","someone littering"]

import random  #gets random for random number; oldMan, bossFight and chicken.       
score = 0  #score is split into categories to tell you how well you did.
holding = []  #list of items you are holding.        

##Class and Function stuff
class Tile:
    def __init__(self, text, yesLocation, noLocation, isContinue, addScore = 0, item = None, isAppend = None, itemCondID = None, condYesLocations = None):
        self.text = text
        self.yesLocation = yesLocation
        self.noLocation = noLocation
        self.isContinue = isContinue
        self.addScore = addScore # 1 to add score when answer is Yes, -1 to add score when answer is No, 0 to not change score
        self.item = item
        self.isAppend = isAppend
        self.itemCondID = itemCondID
        self.condYesLocations = condYesLocations
        
    def displayTile(self):
        app.setLabel("text",self.text)
        if(self.isAppend):
            self.appendRemove()
        for things in holding:  #checks what items are in list but doesnt print in GUI
            print (items[things])  
            
    def appendRemove(self):
        if(self.isAppend):
            holding.append(self.item) 
        else:
            holding.remove(self.item)

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
    if tile[current].yesLocation is None:
        if tile[current].itemCondID in holding:
            tile[current].yesLocation = tile[current].condYesLocations[0]
        else:
            tile[current].yesLocation = tile[current].condYesLocations[1]
            
    if(tile[current].isContinue):
        if button == "Continue":
            current = tile[current].yesLocation
    else:
        if button == "Yes":
            current = tile[current].yesLocation
            if tile[current].addScore == 1:
                score += 1
        elif button == "No":
            current = tile[current].noLocation
            if tile[current].addScore == -1:
                score -= 1
    tile[current].displayTile()        
    updateButtons()

##Setup of questions and GUI          
current = 0 # so it starts at tile 0 in the list

# create a GUI variable called app
app = gui("Login Window","400x200")
app.addLabel("text")
app.addButtons(["Yes","No"],press)
app.addButton("Continue",press)

# question/statement, what it goes to if you press yes or continue write none if there is a condition, what it goes to if you press no, false is yes/no and true is continue, if we want to change score when answer ==no (addScore = -1), when answer ==yes (addScore = 1), any required key words.
tile=[Tile(".... You come across a "+(items[0])+"""!     
Would you like to pick up the """+(items[0])+"?",1,2,False),  #Need a starting cover tile and a finishing stats tile.
Tile("question2?",3,3,True,item = 0,isAppend = True),
Tile("question3?",3,3,True),
Tile("4?",None,3,False,itemCondID = 0,condYesLocations = (1,2))] ## want to go to question3? if you press yes and have the bottle







##What makes it run
updateButtons()
tile[current].displayTile()

# start the GUI
app.go()

