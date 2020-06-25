#20200622_environmentalAssessmentGUI_v1.42
#ethanMclachlan

##change log
#1.41 finished game (not addng the "GAME OVER" bits as then Chase and T-Bone would never finish)
#1.42 commented

# import the library
from appJar import gui

##Variables
#items on path
items = ["plastic bottle","pile of leaves","hobo","plastic bag","the gardeners lost secateurs","dog poo",
        "nylon fishing line","descarded fish and chips in paper","batteries","litter","noDiscard"]
     
score = 0  
holding = []  #list of items you are holding.        

##Class and Function stuff
class Tile:  #a class to contain the tile variables, the answers and the possible outcomes in the list
    def __init__(self, text, yesLocation, noLocation, isContinue, addScore = 0, item = None, isAppend = None, itemCondID = None, condYesLocations = None, func = None):
        self.text = text  #is the question or statement
        self.yesLocation = yesLocation  #is where to go to next if the answer is yes or continue
        self.noLocation = noLocation  #is where you go to if the answer is no
        self.isContinue = isContinue  #is if the question is a continue or a yes/no question
        self.addScore = addScore  #adds to the score
        self.item = item  #is the item that is checked by is append
        self.isAppend = isAppend  #is wether to append or remove the item from the list
        self.itemCondID = itemCondID  #checks if an item is in holding
        self.condYesLocations = condYesLocations  #provides the locations of the next tile based on wether you have the item required
        self.func = func  #runs the ending function 
        
    def displayTile(self):
        global score  #had to make score global to add to it from within the class
        if self.func is not None:  #checks to see if the end function should be run
            self.func()
        app.setLabel("text",self.text)  #adds the text to the label to be displayed
        if(self.isAppend != None): #adds or removes item from holding depending if is append is True or False
            self.appendRemove()  
        if len(holding) != 0: #if there is something in the list of holding it prints the list
            for things in holding:  
                print ("["+items[things]+"]",end="")
            print()
        else:
            print("[nothing in list]")  #prints if you are holding nothing
        if self.addScore == 1:  #adds score
            score += 1        
            
    def appendRemove(self):
        if(self.isAppend == True): 
            holding.append(self.item)  #adds the item to the holding list
        elif(self.isAppend == False):
            if(holding.count(self.item)):  #checks if the item is in the holding list
                holding.remove(self.item)  #removes the item from the holding list
            

def endCheck():
    if len(holding) != 0 and "noDiscard" in holding:  #checks to see if there is something in the holding list and if there is adds these tiles tothe list
        tile.append(Tile("Would you like to put all of the recycling in the recycling bin?",136,137,False))
        tile.append(Tile("You put all of the recycling in the bin sit down and enjoy your lunch. YOU WIN! \n\nScore = %d/30" % score,None,None,None))
        tile.append(Tile("You sit down and enjoy your lunch with your collection of recycling. YOU WIN! \n\nScore = %d/30" % score,None,None,None))
    else:  #if there is nothing in holding then it adds this tile to the list
        tile.append(Tile("You sit down and enjoy your lunch. YOU WIN! \n\nScore = %d/30" % score,None,None,None))

def updateButtons():
    if(tile[current].isContinue):  #if the tile just needs continue buttton
        app.hideButton("No")  #hides yes/no buttons
        app.hideButton("Yes")
        app.showButton("Continue")  #shows continue button
    elif tile[current].isContinue is None and tile[current].yesLocation is None and tile[current].noLocation is None:
        print("finished")  #if the game is finished it hides all the buttons
        app.hideButton("No")
        app.hideButton("Yes")        
        app.hideButton("Continue")
    else:  #if the tlis needs yes/no buttons
        app.hideButton("Continue")  #hides continue button
        app.showButton("Yes")  #shows yes/no buttons
        app.showButton("No")
        
def press(button):  #where you go depending on which button you push
    global current
    if tile[current].yesLocation is None:  #if you press yes or continue and there is none in the yes location then you must be holding something to continue and if youre not you dont go to that tile
        if tile[current].itemCondID in holding:  #checks if you are holding the item and then if you are sends you to the next tile
            tile[current].yesLocation = tile[current].condYesLocations[0]
        else:  #if youre not holding the item it sends you to an alternate tile
            tile[current].yesLocation = tile[current].condYesLocations[1]
    if tile[current].noLocation is None:  #same as above but checks when answer picked is no
        if tile[current].itemCondID in holding:
            tile[current].noLocation = tile[current].condYesLocations[0]
        else:
            tile[current].noLocation = tile[current].condYesLocations[1]    
            
    if(tile[current].isContinue):  #if the continue button is pressed it goes to the next tile wich is the one in the yes location
        if button == "Continue":  
            current = tile[current].yesLocation
    else:
        if button == "Yes":  #if the yes button is ressed you go to the yes location
            current = tile[current].yesLocation
        elif button == "No":  #if the no button is pressed you go to the no location
            current = tile[current].noLocation
    tile[current].displayTile()  #displays the next tile        
    updateButtons()  #updates the buttons

##Setup of questions and GUI          
current = 0 # so it starts at tile 0 in the list

# create a GUI variable called app
app = gui("Environmental Game","900x175")  #creates a gui named Environmental game 
app.addLabel("text")  #adds text to the gui
app.addButtons(["Yes","No"],press)  #adds yes/no buttons to the gui
app.addButton("Continue",press)  #adds continue button to the gui

# question/statement, what it goes to if you press yes or continue write none if there is a condition, what it goes to if you press no, false is yes\no and true is continue, if we want to change score addScore = 1, any required key words(for condition yesLocation has to == none and no Location has to == none

tile = [ #list of print statements and the info that applies to them
#scenario 0
Tile("""You are on your way to the beach where you will sit in your favourite seat, admire 
the view, breathe in the fresh sea air and eat lunch. To get to your favourite bench 
you have to walk through Winston Park and then along the beach. You start off on 
your journey walking through the park when...""",1,1,True),
#tile1 plastic bottle 1
Tile(".... You come across a "+(items[0])+"! \nWould you like to pick up the "+(items[0])+"?",2,3,False),
Tile("You continue on your journey with the "+(items[0])+" in hand.",4,4,True,item = 0,isAppend = True,addScore = 1),
Tile("You leave the "+(items[0])+" on the ground and continue on your journey.",4,4,True),
#tile2 cat 4
Tile("You are walking along the path when you come across a cat.",None,1,True,itemCondID = 0,condYesLocations = (5,10)),
Tile("Would you like to throw the "+(items[0])+" at the cat?",8,6,False),
Tile("Would you like to leave the "+(items[0])+" on the ground?",7,9,False), 
Tile("You leave the "+(items[0])+" on the ground and continue on your journey.",10,10,True,item = 0,isAppend = False),
Tile("You throw the "+(items[0])+" at the cat which then attacks you.",13,13,True,item = 0,isAppend = False), 
Tile("You continue on your journey with the "+(items[0])+" in hand.",10,10,True,addScore = 1),
Tile("Would you like to stroke the cat?",12,11,False), 
Tile("You leave the cat alone and continue on your journey.",13,13,True),
Tile("You stroke the cat, it meows and you continue on your journey.",13,13,True,addScore = 1),
#tile3 pedestrian 13
Tile("You are walking along the path when you come across a pedestrian.",None,1,True,itemCondID = 0,condYesLocations = (14,19)),
Tile("Would you like to whack the pedestrian with the "+(items[0])+"?",18,15,False),
Tile("You leave the pedestrian alone and continue on your journey.",16,16,True,addScore = 1),
Tile("Would you like to leave the "+(items[0])+" on the ground?",20,17,False),
Tile("You continue on your journey past the pedestrian with the "+(items[0])+" in hand.",21,21,True,addScore = 1),
Tile("You smack the pedestrian with the "+(items[0])+" so he mugs you and steals your pants.",21,21,True),
Tile("""The pedestrian says "hi" and smiles.  You then continue on your journey.""",21,21,True),
Tile("You leave the "+(items[0])+" on the ground and continue.",21,21,True,item = 0,isAppend = False),
#tile4 rubish bin beside garden 21
Tile("You are walking along the path when you come across a rubbish bin \nbeside a bench looking over the beautiful garden.",None,1,True,itemCondID = 0,condYesLocations = (22,23)),
Tile("Would you like to dispose of the "+(items[0])+" in the rubbish bin?",24,25,False),
Tile("You sit down on the bench to look at the garden.",28,28,True),
Tile("You throw the "+(items[0])+" in the bin and sit down on the bench to look at the garden.",28,28,True,item = 0,isAppend = False),
Tile("Would you like to leave the "+(items[0])+" in the garden?",27,26,False), 
Tile("You admire the beautiful garden and then continue on your journey.",31,31,True,addScore = 1),
Tile("You leave the "+(items[0])+" in the garden and continue on your journey.",31,31,True,item = 0,isAppend = False),
Tile("Would you like to smell the flowers?",30,29,False),
Tile("You admire the beautiful garden and then continue on your journey.",31,31,True),
Tile("You smell the flowers and then continue on your journey.",31,31,True),
#tile5 pile of leaves 31
Tile("You are walking along the path when you come across a "+(items[1])+". \nWould you like to sweep the "+(items[1])+" off the path?",32,33,False),
Tile("You sweep the "+(items[1])+" off the path and continue.",34,34,True,addScore = 1),
Tile("You leave the "+(items[1])+" on the path and continue on your journey.",34,34,True),
#tile6 hobo 34
Tile("You are walking along the path when you come across a "+(items[2])+"! \nWould you like to give the "+(items[2])+" a sandwich from your lunch?",35,36,False),
Tile("You give the "+(items[2])+" a sandwich and continue.",41,41,True,addScore = 1),
Tile("Would you like to mock the "+(items[2])+"?",39,None,False,itemCondID = 0,condYesLocations = (37,40)),
Tile("Would you like to throw the "+(items[0])+" at the "+(items[2])+"?",39,40,False),
Tile("You throw the "+(items[0])+" at the "+(items[2])+".",39,39,True),              
Tile("The "+(items[2])+" beats you and then proceeds to steal your sandwitch!",41,41,True),
Tile("You leave the "+(items[2])+" alone and continue on your journey.",41,41,True),
#tile7 plastic bag 41
Tile("You are walking along the path when you come across a "+(items[3])+"! \nWould you like to pick up the "+(items[3])+"?",43,42,False),
Tile("You leave the "+(items[3])+" on the ground and continue on your journey.",46,46,True),
Tile("Would you like to put the "+(items[3])+" in the bushes?",44,45,False),
Tile("You put the "+(items[3])+" in the bushes, the gardener yells at you \nand you continue on your journey.",46,46,True),
Tile("You continue on your journey with the "+(items[3])+" in hand.",46,46,True,item = 3,isAppend = True,addScore = 1),
#tile8 secateurs 46
Tile("You are walking along the path when you come across "+(items[4])+"! \nWould you like to pick up "+(items[4])+"?",48,47,False),
Tile("You leave "+(items[4])+" on the ground and continue on your journey.",52,52,True),
Tile("You pick up "+(items[4])+".",49,49,True,addScore = 1),
Tile("Would you like to leave "+(items[4])+" beside a tree?",50,51,False), 
Tile("You put "+(items[4])+" beside the tree and continue.",52,52,True),
Tile("You continue on your journey with "+(items[4])+" in hand.",52,52,True,item = 4,isAppend = True,addScore = 1),
#tile9 arrive at beach 52 
Tile("You arrive at the beach and set off walking along it to your favourite seat.",None,1,True,itemCondID = 0,condYesLocations = (53,56)),
Tile("Would you like to leave the "+(items[0])+" on the sand?",54,55,False),
Tile("You drop the "+(items[0])+" and continue.",57,57,True,item = 0,isAppend = False),
Tile("You don't leave the "+(items[0])+" on the sand and continue.",57,57,True,addScore = 1),
Tile("There are seagulls flying past.",None,1,True,itemCondID = 3,condYesLocations = (57,60)),
Tile("Would you like to leave the "+(items[3])+" in the sand?",58,59,False),
Tile("You drop the "+(items[3])+" and continue.",60,60,True,item = 3,isAppend = False),
Tile("You don't leave the "+(items[3])+" in the sand and continue.",60,60,True,addScore = 1),
Tile("You can smell the salty sea.",None,1,True,itemCondID = 4,condYesLocations = (61,64)),
Tile("Would you like to leave "+(items[4])+" on the sand?",62,63,False),
Tile("You drop "+(items[4])+" and continue.",64,64,True,item = 4,isAppend = False),
Tile("You continue with "+(items[4])+" in hand.",64,64,True,addScore = 1),
#tile10 dog poo 64
Tile("You are walking along the beach when you come across "+(items[5])+" beside a rubbish bin.",None,1,True,itemCondID = 3,condYesLocations = (65,70)),
Tile("Would you like to pick up the "+(items[5])+" with the "+(items[3])+" and dispose of it in the rubbish bin?",66,67,False), 
Tile("You dispose of the "+(items[5])+" in the rubbish bin.",67,67,True,addScore = 1), 
Tile("You see a pile of rubbish beside the bin. Would you like to put it in the bin?",68,69,False),  
Tile("You put the rubbish in the bin and continue.",None,1,True,itemCondID = 3,condYesLocations = (71,73),addScore = 1),
Tile("You leave the rubbish and continue down the beach.",None,1,True,itemCondID = 3,condYesLocations = (71,73)),
Tile("You continue down the beach avoiding the "+(items[5])+", leaving it for someone to stand in.",None,1,True,itemCondID = 0,condYesLocations = (71,73)),
Tile("Would you like to dispose of the "+(items[0])+" in the rubbish bin?",72,73,False),    
Tile("You throw the "+(items[0])+" in the bin.",73,73,True,item = 0,isAppend = False),
Tile("There are more seagulls flying past making annoying squawking noises.",None,1,True,itemCondID = 3,condYesLocations = (74,76)),
Tile("Would you like to dispose of the "+(items[3])+" in the rubbish bin?",75,76,False), 
Tile("You throw the "+(items[3])+" in the bin.",76,76,True,item = 3,isAppend = False),
Tile("There are some cool shells by the bin.",None,1,True,itemCondID = 4,condYesLocations = (77,79)),
Tile("Would you like to dispose of "+(items[4])+" in the rubbish bin?",78,79,False),
Tile("You throw "+(items[4])+" in the bin and continue down the beach.",80,80,True,item = 4,isAppend = False),
Tile("You continue down the beach.",80,80,True),
#tile11 seal 80
Tile("You are walking along the beach when you come across a seal wrapped in "+(items[6])+".",None,1,True,itemCondID = 4,condYesLocations = (81,87)),
Tile("Would you like to use "+(items[4])+" to cut the seal free.",83,82,False),
Tile("You leave the seal wrapped in "+(items[6])+" to die and continue on your journey.",90,90,True),
Tile("You use "+(items[4])+" to cut the seal free from the "+(items[6])+" and then continue down the beach.",84,84,True,addScore = 1),
Tile("Would you like to leave "+(items[4])+" and the "+(items[6])+" on the beach?",85,86,False),
Tile("You leave "+(items[4])+" and the "+(items[6])+" on the beach and continue on your journey.",90,90,True,item = 4,isAppend = False),
Tile("You continue down the beach with the "+(items[6])+".",90,90,True,item = 6,isAppend = True,addScore = 1),
Tile("Would you like to use your teeth to cut the seal free from the "+(items[6])+"?",88,89,False),
Tile("You cut the seal free from the "+(items[6])+" with your teeth, breaking a tooth. \nThe seal is saved but you'll have a hefty dentist bill.",90,90,True,addScore = 1), 
Tile("You leave the seal wrapped in "+(items[6])+" to die and continue.",90,90,True),
#tile12 fish 'n' chips in paper 90
Tile("You are walking along the beach when you come across "+(items[7])+"! \nWould you like to pick up the "+(items[7])+"?",92,91,False),
Tile("You leave the "+(items[7])+""" on the ground and try to continue 
on your journey, BUT! A policeman sees you beside the """+(items[7])+""",
he assumes they're yours and gives you a one million dollar fine.""",93,93,True), 
Tile("You continue on your journey with the "+(items[7])+" in hand.",93,93,True,item = 7,isAppend = True,addScore = 1),
#tile13 dog walker 93
Tile("You are walking along the beach when you come across a woman walking her dog.",None,1,True,itemCondID = 0,condYesLocations = (94,98)),
Tile("Would you like to whack the woman walking her dog with the "+(items[0])+"?",97,95,False),
Tile("Would you like to leave the "+(items[0])+" on the ground?",96,98,False,addScore = 1),
Tile("You drop the "+(items[0])+" and continue.",98,98,True),
Tile("You try to smack the woman walking her dog with the "+(items[0])+" but her dog attacks you.",98,98,True), 
Tile("There is a surfer carving up the waves.",None,1,True,itemCondID = 4,condYesLocations = (99,103)),
Tile("Would you like to throw "+(items[4])+" at woman walking her dog?",102,100,False),
Tile("Would you like to leave "+(items[4])+" on the ground?",101,103,False,addScore = 1),
Tile("You leave "+(items[4])+" in the sand.",103,103,True),
Tile("You try to throw "+(items[4])+" at the woman walking her dog but her dog attacks you.",103,103,True), 
Tile("The womans dog looks at you.",None,1,True,itemCondID = 7,condYesLocations = (104,109)),
Tile("Would you like to throw the "+(items[7])+" at woman walking her dog?",108,105,False),
Tile("Would you like to leave the "+(items[7])+" on the ground?",106,107,False,addScore = 1),
Tile("You leave the "+(items[7])+" in the sand and continue.",110,110,True,item = 7,isAppend = False),
Tile("You continue down the beach.",110,110,True),
Tile("You throw the "+(items[7])+" at the woman walking her dog. She becomes angry and storms off. \nHer dog eats some chips and then scurries off after her.",110,110,True,item = 7,isAppend = False),
Tile("""The woman walking her dog says "hi" and smiles. You then continue on your journey.""",110,110,True),
#tile14 batteries and seagulls 110
Tile("You are walking along the path when you come across two "+(items[8])+"! \nWould you like to pick up the "+(items[8])+"?",112,111,False),
Tile("You leave the two "+(items[8])+" on the ground and continue on your journey.",None,1,True,itemCondID = 7,condYesLocations = (113,116)),
Tile("You continue on your journey down the beach with the two "+(items[8])+" in hand.",None,1,True,itemCondID = 7,condYesLocations = (113,116),addScore = 1),
Tile("There are some seagulls on the beach in front of you.  Would you like to feed the \nseagulls some chips from the "+(items[7])+"?",114,115,False), 
Tile("You feed the seagulls some chips and continue on your journey.",116,116,True,item = 7,isAppend = False,addScore = 1),
Tile("You don't feed the seagulls the chips and continue on your journey.",116,116,True), 
#tile15 seat comes into view 116
Tile("Your favourite seat is just ahead of you glistening in the sun looking like the \nperfect place to relax and have lunch.  Would you like to drop all \nof the things you are holding except for your lunch of course and run to get there faster?",118,117,False),
Tile("You continue down the beach as normal.",119,119,True,item = 10,isAppend =True,addScore = 1),  # adds item no then if noDiscard is in the list when you finish it keeps everything.
Tile("You drop everything and start running.",119,119,True,item = 4,isAppend = False), #only need to remove secuateers.
#tile16 boss fight 119
Tile("You are going along the beach when you come across someone "+(items[9])+"ing! \nWould you like to force them to pick up their "+(items[9])+"?",121,120,False),
Tile("You continue leaving them to scatter the beach with "+(items[9])+".",127,127,True),
Tile("You shout them down but they refuse to pick up their "+(items[9])+"! \nDo you wish to challenge them to a duel?",125,122,False,addScore = 1),
Tile("Would you like to pick up their "+(items[9])+" and take it with you?",123,124,False),
Tile("You pick up their "+(items[9])+" and take it with you.",127,127,True,item = 9,isAppend = True,addScore = 1), 
Tile("You leave the "+(items[9])+" and continue.",127,127,True),
Tile("You challenge them to a duel with the loser having to pick up the "+(items[9])+".",126,126,True),
Tile("YOU TEACH THEM A LESSON! They go on to never "+(items[9])+" again!",127,127,True,addScore = 1),
#tile17 plastic bag 2 and gardner 127
Tile("You see a "+(items[3])+" blowing along the beach would you like to catch the "+(items[3])+"?",129,128,False),
Tile("You leave the "+(items[3])+" to blow into the sea and kill the wildlife.",134,134,True),
Tile("You chase after the "+(items[3])+" and catch it.",130,130,True,addScore = 1),
Tile("While walking back towards the bench you see the gardner walking along the beach.",None,1,True,itemCondID = 4,condYesLocations = (131,134)),
Tile("Would you like to give "+(items[4])+" back to him?",133,132,False),
Tile("You don't give "+(items[4])+" back to him and continue.",134,134,True),
Tile("You give "+(items[4])+" back and continue.",134,134,True,addScore = 1),
#tile18 final destination 134
Tile("You arive at your favourite bench with a recycling bin conveinently beside it.",135,135,True,func=endCheck)]

##What makes it run
updateButtons()  #this changes the buttons either yes/no or continue
tile[current].displayTile()  #displays the next tile in the list

# starts the GUI
app.go()