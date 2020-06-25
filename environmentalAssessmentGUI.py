#20200602_environmentalAssessmentGUI_v1.3
#ethanMclachlan with help from Chase Meister, T Bone and mlj

##change log
#1.31 tile 1 and 2
#1.32 tile 3 and 4
# etc
#1.4 when everything works and add game tiles and then score

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
        if(self.isAppend != None):
            self.appendRemove()
        if len(holding) != 0:
            for things in holding:  
                print (items[things])
        else:
            print("nothing in list")
            
    def appendRemove(self):
        if(self.isAppend == True):
            holding.append(self.item)
        elif(self.isAppend == False):
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
app = gui("Login Window")
app.addLabel("text")
app.addButtons(["Yes","No"],press)
app.addButton("Continue",press)

# question/statement, what it goes to if you press yes or continue write none if there is a condition, what it goes to if you press no, false is yes/no and true is continue, if we want to change score when answer ==no (addScore = -1), when answer ==yes (addScore = 1), any required key words(for condition yesLocation has to == none and no Location has to == none
#tile=[Tile(".... You come across a "+(items[0])+"""!     
#Would you like to pick up the """+(items[0])+"?",1,2,False),  #Need a starting cover tile and a finishing stats tile.
#Tile("question2?",3,3,True,item = 0,isAppend = True),
#Tile("question3?",3,3,True),
#Tile("4?",None,3,False,itemCondID = 0,condYesLocations = (1,2))] ## want to go to question3? if you press yes and have the bottle

tile = [
#scenario
Tile("""You are on your way to the beach where you will sit in your favourite seat, admire 
the view, breathe in the fresh sea air and eat lunch. To get to your favourite bench 
you have to walk through Winston Park and then along the beach. You start off on 
your journey walking through the park when...""",1,1,True),
#tile1 plastic bottle
Tile(".... You come across a "+(items[0])+"""!     
Would you like to pick up the """+(items[0])+"?",2,3,False),
Tile("You continue on your journey with the "+(items[0])+" in hand.",4,4,True,item = 0,isAppend = True),
Tile("You leave the "+(items[0])+" on the ground and continue on your journey.",4,4,True),
#tile2 cat
Tile("You are walking along the path when you come across a cat.",None,None,True,itemCondID = 0,condYesLocations = (5,10)),
Tile("Would you like to throw the "+(items[0])+" at the cat?",8,6,False),
Tile("Would you like to leave the "+(items[0])+" on the ground?",7,9,False), 
Tile("You leave the "+(items[0])+" on the ground and continue on your journey.",10,10,True,item = 0,isAppend = False),
Tile("You throw the "+(items[0])+" at the cat which then attacks you.",13,13,True,item = 0,isAppend = False),
Tile("You continue on your journey with the "+(items[0])+" in hand.",10,10,True),
Tile("Would you like to stroke the cat?",12,11,False), 
Tile("You leave the cat alone and continue on your journey.",13,13,True),
Tile("You stroke the cat, it meows and you continue on your journey.",13,13,True) ]

##What makes it run
updateButtons()
tile[current].displayTile()

# start the GUI
app.go()


"""
#tile3 pedestrian
Tile("You are walking along the path when you come across a pedestrian.")
"Would you like to whack the pedestrian with the "+(obstacles[0].name)+"?
"You leave the pedestrian alone and continue on your journey.")
"Would you like to leave the "+(obstacles[0].name)+" on the ground? 
"You leave the "+(obstacles[0].name)+" on the ground and continue on your journey.")
("You continue on your journey past the pedestrian with the "+(obstacles[0].name)+" in hand.")
("You smack the pedestrian with the "+(obstacles[0].name)+" so he mugs you and steals your lunch.
No beach for you!   GAME OVER")
("The pedestrian says "hi" and smiles.  You then continue on your journey.")
#tile4 rubish bin beside garden
"You are walking along the path when you come across a rubbish bin beside a bench 
looking over the beautiful garden.")
("Would you like to dispose of the "+(obstacles[0].name)+" in the rubbish bin?"
("You sit down on the bench to look at the garden.")
("You throw the "+(obstacles[0].name)+" in the bin and sit down on the bench to look at the garden.")
("Would you like to leave the "+(obstacles[0].name)+" in the garden? 
("You admire the beautiful garden and then continue on your journey.")
("You leave the "+(obstacles[0].name)+" in the garden and continue on your journey.")
("Would you like to smell the flowers?
("You admire the beautiful garden and then continue on your journey.")
"You smell the flowers and then continue on your journey.")
#tile5 pile of leaves
("You are walking along the path when you come across a "+(obstacles[1].name)+".
Would you like to sweep the "+(obstacles[1].name)+" off the path?")
("You sweep the "+(obstacles[1].name)+" off the path and continue.")
("You leave the "+(obstacles[1].name)+" on the path and continue on your journey.") 
#tile6 hobo
("You are walking along the path when you come across a "+(obstacles[2].name)+"!
Would you like to give the "+(obstacles[2].name)+" a sandwich from your lunch?)
"You give the "+(obstacles[2].name)+" a sandwich and continue.")
("Would you like to mock the "+(obstacles[2].name)+"? 
("Would you like to throw the "+(obstacles[0].name)+" at the "+(obstacles[2].name)+"?
("You throw the "+(obstacles[0].name)+" at the "+(obstacles[2].name)
 ("The "+(obstacles[2].name)+" beats you for mocking him and then proceeds to chase you out of the park!
 No beach for you!   GAME OVER")
("You leave the "+(obstacles[2].name)+" alone and continue on your journey.")
#tile7 plastic bag
("You are walking along the path when you come across a "+(obstacles[3].name)+"!
Would you like to pick up the "+(obstacles[3].name)+"?
("You leave the "+(obstacles[3].name)+" on the ground and continue on your journey.")
("Would you like to put the "+(obstacles[3].name)+" in the bushes?
("You put the "+(obstacles[3].name)+" in the bushes the gardener yells at you and you continue 
on your journey.")
("You continue on your journey with the "+(obstacles[3].name)+" in hand.")
#tile8 secateurs
("You are walking along the path when you come across "+(obstacles[4].name)+"!
Would you like to pick up "+(obstacles[4].name)+"?
("You leave "+(obstacles[4].name)+" on the ground and continue on your journey.")
("You pick up "+(obstacles[4].name)+".")
("Would you like to leave "+(obstacles[4].name)+" beside a tree? 
("You put "+(obstacles[4].name)+" beside the tree and continue.")
("You continue on your journey with "+(obstacles[4].name)+" in hand.")
#tile9 arrive at beach
("You arrive at the beach and set off walking along it to your favourite seat.")
("Would you like to leave the "+(obstacles[0].name)+" on the sand?
("You drop the "+(obstacles[0].name)+" and continue.")
("You don't leave the "+(obstacles[0].name)+" on the sand and continue.")
("Would you like to leave the "+(obstacles[3].name)+" in the sand?
("You drop the "+(obstacles[3].name)+" and continue.")
("You don't leave the "+(obstacles[3].name)+" in the sand and continue.")
("Would you like to leave "+(obstacles[4].name)+" on the sand?
("You drop "+(obstacles[4].name)+" and continue.")
("You continue with "+(obstacles[4].name)+" in hand.")
#tile10 dog poo """





