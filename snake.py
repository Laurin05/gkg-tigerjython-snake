################################
#                              #
# SNAKE.PY                     #
#                              #
# Author:  Laurin Egeler       #
# Date:    18 November 2020    #
#                              #
################################

###########
# IMPORTS #
###########


from gturtle import *


#####################
# GLOBAL PROPERTIES #
#####################


# Key codes
KEY_CODE_LEFT = 37
KEY_CODE_RIGHT = 39
KEY_CODE_UP = 38
KEY_CODE_DOWN = 40
KEY_CODE_ENTER = 10

# Constant settings
frameSize = 500

# General properties
points = 0
highScore = 0
lastKey = None
name = ""
dangerZone = 15
text = None
punkte = 0
highscore = 0
a = 100


# Turtle properties
frame = TurtleFrame() #create a turtle playground with the name frame
snakeTurtle = None
appleTurtle = None
stoneTurtle = None
stoneTurtles = [] #creates n empty list named stoneTurtles

#############
# FUNCTIONS #
#############


def createFrameTurtle():    #making a square 
    frameTurtle = Turtle(frame)
    frameTurtle.hideTurtle()
    frameTurtle.setPos(-250,-250)
    repeat 4:
        frameTurtle.forward(frameSize)
        frameTurtle.right(90)
        
def onKeyPressed(key):       #looks which key do you press and give then the variable the number of the key
    global lastKey #this definition can now change the value of the variable for the whole game.
    if key.getKeyCode() == KEY_CODE_LEFT:
        lastKey = key.getKeyCode()
    elif key.getKeyCode() == KEY_CODE_RIGHT:
        lastKey = key.getKeyCode()
    elif key.getKeyCode() == KEY_CODE_UP:
        lastKey = key.getKeyCode()
    elif key.getKeyCode() == KEY_CODE_DOWN:
        lastKey = key.getKeyCode()
    elif key.getKeyCode() == KEY_CODE_ENTER:
        lastKey = key.getKeyCode()
                
def steuern():   #if the last key was 37,39,38 or 40 then it sets a new heading.
    heading = snakeTurtle.heading()
    if lastKey == 37:
        if heading == 0 or heading == 180:  #now the snake can only turn to the left direction when the last direction was up or down
            snakeTurtle.setHeading(-90)
    elif lastKey == 39:
        if heading == 0 or heading == 180:   #now the snake can only turn to the right direction when the last direction was up or down
            snakeTurtle.setHeading(90)
    elif lastKey == 38:
        if heading == 90 or heading == -90:    #now the snake can only turn to the up direction when the last direction was right or left
            snakeTurtle.setHeading(0)
    elif lastKey == 40:
        if heading == 90 or heading == -90:    #now the snake can only turn to the down direction when the last direction was right or left
            snakeTurtle.setHeading(180)
        

# Checks whether the snake (turtle) is alive or not.
# Then we check if the turtle touches a stone or the main frame (blue square).
# Returns True or False.
def snakeTurtleIsAlive():
    posX = snakeTurtle.getX()
    posY = snakeTurtle.getY()# gets the X and Y cordinates of the snake
    
    for stoneTurtle in stoneTurtles: #the game checks al stones which are inside the list stoneTurtles
        dist = stoneTurtle.distance(posX, posY)#checks the distance of the stone to the snake position
        if dist < dangerZone:  #when dis distance is smaler than the dangerzone(15 pixels) then it return False(snake die)
            playTone(250, 1000)#play a tone , first number the frequenz(tonehigh) and the second number the tone lenght
            return False
            
            
    if posX > 249 or posX < -249 or posY > 249 or posY < -249: #when the X or the Y cordinate of the snake is biger than 249 or -249 then its returning False
        playTone(250, 1000)
        return False
    
    
    else:  #if none of the if conditions are corecct then it returns True
        return True
    

    
    
def apple():
    global appleTurtle
    if appleTurtle == None: #creates an appleTurtle if there isnt one.
        appleTurtle = Turtle(frame,"apple.png")# create aplleTurtle with picture in the Playground frame
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)#set a random position inside the frame
    else:     #if there is alredy a appleTurtle it sets only a new random Position
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
        
        
    
    
def eatApple():
    posAX = appleTurtle.getX()
    posAY = appleTurtle.getY()
    dist = snakeTurtle.distance(posAX, posAY) #get X,Y cordinates of appleTurtle and snakeTurtle checks distance to appleTurtle
    if dist < dangerZone:     #when dis distance is smaler than the dangerzone(15) then the snake eat the apple and get a point
        global points
        appleTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)#when the snake touches the apple, the apple gets a new random position inside the frame
        points = points +1
        playTone(700)#play a tone with the frequenz 700
        barText()
        
def stone():
    global a 
    if i == a:  #if i is a(a in beginning 100) then it creates a stone
        stoneTurtle = Turtle(frame,"stone.png")
        stoneTurtles.append(stoneTurtle) #add the stone to the stoneTurtles list
        stoneTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
        a = a + 100 #a is now 100 bigger. that means the while loop has now to end again 100 times to create a stone
        posX = stoneTurtle.getX()
        posY = stoneTurtle.getY()
        dist = appleTurtle.distance(posX, posY) #get X,Y cordinates of stoneTurtle checks distance to appleTurtle
        
        if dist < dangerZone: #if this distance is smaller than 15 then the stone gets a now random position(the stone can never spawn inside the apple.
            stoneTurtle.setRandomPos(0.9*frameSize, 0.9*frameSize)
    
    

def barText():
    global highscore #this funktion can change the highscore for the whole game
    if points > highscore: #if the points which you now have are higher, then the highscore updates to the points you now have
            highscore = points
    snakeTurtle.setStatusText("Player name: "+name +" | Game: "+ str(points)+" points | Highscore: "+ str(highscore)) #overwrite the old text with an updated one
    

def restart():
    global points
    global highscore
    global a
    global stoneTurtles    #this funktion can change all these variables for the whole code
    snakeTurtle.setStatusText("Player name: "+name +" | Game: "+ str(points)+" points | Highscore: "+ str(highscore)+" | Game over: Press ENTER to restart!")#add text to the statusbar which gives you the Tipp that you can restart the game with Enter
    while True:
        if lastKey == 10: #goes through the while loop untile the last key is Enter
            
            points = 0 #set points back to 0
            for stoneTurtle in stoneTurtles:
                stoneTurtle.hideTurtle()#hide all stones of the list
            stoneTurtles = []#clear the stone list
            a = 100 #set a back to 100
            play()#start the game, playfunktion again            
            
                    
#
# GENERAL METHODS
#

# Waits until a name is entered by a dialog.
# It saves the name to the global variable name.
def waitForInputName():
    global name # we want to change the value

    name = input("Enter your Name")



#
# MAIN METHODS
#

# The function to play the game.
def play():
    global points # we want to change the value
    global snakeTurtle
    global IsAlive
    global i      
    
    
    if snakeTurtle == None: #if there is no snake turtle create one with a pictur and react to pressed keys
        snakeTurtle = Turtle(frame,"snake.png",keyPressed = onKeyPressed)
        
    else: #if there is already a snake then the snakeposition is 0,0 and the the heading 0
        snakeTurtle.setPos(0,0)
        snakeTurtle.setHeading(0)
    snakeTurtle.penUp() #the snake shouldn't paint a line
    snakeTurtle.addStatusBar(25) #create a statusbar under the game
    snakeTurtle.setStatusText("Player name: "+name +" | Game: "+ str(points)+" points | Highscore: "+ str(highscore))#add once text inside the statusbar at the beginning of the game.
    
    
    apple()
    
    
    i = 0
    isAlive = True
    while (isAlive): # Run the game while the snake is alive
        global a
        snakeTurtle.forward(4)#the snake goes always four forward
        snakeTurtle.speed(-1)#the snake has  the maximum speed.
        steuern()
        eatApple()
        stone()         
            
        

        
            
        # Check if the snake is still alive
        isAlive = snakeTurtleIsAlive()

        i = i + 1 #everytime the while loop starts again i gets one bigger
        snakeTurtleIsAlive()
        
    # The game is over now
    restart()
            
            
# The main function.
def main():

    # Wait until a name is input
    waitForInputName();

    # Create the frame turtle
    createFrameTurtle()
    # Start the actual game
    play()
    


#############
# MAIN CODE #
#############



main()


