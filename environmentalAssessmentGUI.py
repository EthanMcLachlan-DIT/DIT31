#20200528_environmentalAssessmentGUI_v1.21
#ethanMclachlan with help from Chase Meister and mlj

##change log
#1.21 add and remove items from the list
#1.22 check if items are in list before asking question
#1.3 when everything works

# import the library
from appJar import gui

##Variables
#items on pat
items = ["plastic bottle","pile of leaves","hobo","plastic bag","the gardeners lost secateurs","dog poo",
        "nylon fishing line","descarded fish and chips in paper","batteries","someone littering"]


import random  #gets random for random number; oldMan, bossFight and chicken.       
score = 0  #score is split into categories to tell you how well you did.
holding = []  #list of items you are holding.        

###############################################################################################################################
class Tile:
    def __init__(self, text, yesLocation, noLocation, isContinue, item = None, isAppend = None):
        self.text = text
        self.yesLocation = yesLocation
        self.noLocation = noLocation
        self.isContinue = isContinue
        self.item = item
        self.isAppend = isAppend
        
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

# question/statement, what it goes to if you press yes or continue, what it goes to if you press no, false is yes/no and true is continue, item, wether you add(true) or remove(false) from holding
tile=[Tile(".... You come across a "+(items[0])+"""!     
Would you like to pick up the """+(items[0])+"?",1,2,False),  #Need a starting cover tile and a finishing stats tile.
Tile("question2?",3,3,True,0,True),
Tile("question3?",3,3,True),
Tile("4?",(2 if (items[0]) in holding else 1),3,False)]

updateButtons()
tile[current].displayTile()
# start the GUI
app.go()

