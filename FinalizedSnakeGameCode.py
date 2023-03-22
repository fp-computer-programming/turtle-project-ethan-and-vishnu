#import the turtle module
import turtle
#import the time module
import time
#import the random module
import random
#from the turtle dictionaries, import the star module
#this module is used for the advanced design
#and it is also used for the textinput function in order to create a textbook for questions
from turtle import *

#the delay variable of the snake is equal to 0.1
delay = 0.1
#the variable of playerscore is equal to 0
playerscore = 0
#the variable of maximumscore is equal to 0
maximumscore = 0

#Graphic module built into Python
#the variable of snakeggameswindow creates a turtle a window
snakegamewindow = turtle.Screen()
#title of the window is called Across the Stars
snakegamewindow.title("Across the Stars")
#the setup of the window is 450 units across and 450 units up
snakegamewindow.setup(450, 450)
#the screensize of the window is 450 units across and 450 units up
snakegamewindow.screensize(450, 450)
#the background for the window is a picture in a gif file
snakegamewindow.bgpic('Interstellar.gif')


#create a function for the color design of the shape in the background of the turtle
def openingcredits():

    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster
    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster
    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster
    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster
    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster
    #for a certain in the range of colors in the following list:
    for colours in ["red", "magenta", "blue", "cyan", "green", "brown", "pink", "white"]:
        color(colours)#display the colors 
        circle(100) #the circle moves 100 units counter clockwise
        left(10)#the circle moves 10 units  left counter clockwise
        speed(0) #the speed of the circle design being formed is zero to make it go faster

    # The keyword, Global, is when a user is allowed to modify a certain variable beyond its limited scope
    # The variable used is t for 
    global t
    # the variable t is equal to turtle.Turtle()
    t = turtle.Turtle()
    # the variable s is equal to screen 
    s = turtle.Screen()
    # the background color of the variable is black
    s.bgcolor("black")
    #the pencolor of the the variable t is white
    t.pencolor("white")
    #the speed of t is 0
    t.speed(0)
    #the setup of width = 450 units and height = 450 units 
    s.setup(450, 450)

    #write the name of the game in the center of the screen
    t.write("Across the Stars", 
            #the alignment of the name of the game is in the center
        align = "center",
        #the font is Gotham, the size is 30 and the title is in bold
          font=("Gotham", 30, "bold"))
    
#close the overall function
openingcredits()

#create a new function called surveyquestions
def surveyquestions():
    #create a turtle screen for the variable snake game window
    snakegamewindow = turtle.Screen()
    #create the title of the turtle screen, Across the Stars
    snakegamewindow.title("Across the Stars")
    #the background color of the snakegamewindow is snakegamewindow
    snakegamewindow.bgcolor("skyblue")
    #the setup is 450 units across and 450 units up
    snakegamewindow.setup(450, 450)
        #the screensize is 450 units across and 450 units up
    snakegamewindow.screensize(450, 450)
        #the background picture is a picture
    snakegamewindow.bgpic('Interstellar.gif')
    #several questions are entered in the textboz for the user to enter their answers
    #as a sample survey similar to what video games in other gaming
    #platofrms have to offer
    x2 = textinput(title, "Wel. Wel. Wel. Welcome. Analysis of Guidance System operating at 37 percent efficiency, Would you like to Assume Command?")
    x1 = textinput(title, "Very Well. Please Enter your Name User: ")
    y1 = textinput(title, x1 + " " + "You have accessed the interface of the guidance system by entering your name as a user for the game.")
    y2 = textinput(title, "I am part of the System. I am Kelex, and I work for the Host of the System. What is your occupation?")
    y3 = textinput(title, "Very Well" + y2 + " " + x1 + " " + "Before you Proceed, there will be a list of questions. Write Ok to Proceed. " )
    z1 = textinput(title, "Age: ")
    z2 = textinput(title, "Country: ")
    z3 = textinput(title, "Date: ")
    z4 = textinput(title, "Favorite Movie: ")
    z5 = textinput(title, "Favorite Game: ")
    a1 = textinput(title, "Favorite Song: ")
    a2 = textinput(title, "Favorite Subject in School: ")
#close function
surveyquestions()

#the head of the snake that will eat the food
headofsnake = turtle.Turtle()
#the shape of the head of the snake is a turtle 
headofsnake.shape("turtle")
#the color of the head of the snake is black
headofsnake.color("Black")
#the original point of the head of the snake is the typical origin point in a cartisian coordinate system
headofsnake.goto(0,0)
#penup() – not "touching" the window
headofsnake.penup()
#need an attribute for the direction in order for the snake to move as identified by the errors in the terminal
headofsnake.direction = 'Motion' 

#the food for the snake as a turtle function
foodforsnake = turtle.Turtle()
#the standerdized color of the food is blue
foodforsnake.color('Blue')
#out of several options for the food, there are several option for the shape of the food
foodforsnakeshape = random.choice(['triangle', 'square', 'circle', 'turtle'])
#the speed of the food for the snake is 0
foodforsnake.speed(0)
#penup() – not "touching" the window
foodforsnake.penup()
#the original point of the food of the snake is 6, 40 in a cartisian coordinate system
foodforsnake.goto(6, 40)

#the score captions as a turtle function
ScoreCaptions = turtle.Turtle()
#the speed of the scorecaptions is 0
ScoreCaptions.speed(0)
#out of several options for the scorecaptions, there are several options for the color
ScoreCaptionscolor = random.choice(['blue', 'red', 'green', 'yellow', 'brown', 'black'])
#the shae of the scorecaptions is a square
ScoreCaptions.shape('square')
#penup() – not "touching" the window
ScoreCaptions.penup()
#• hideturtle() – do not display the turtle. Speeds up drawing
ScoreCaptions.hideturtle()
#original position of the scorecaptions is 0, 110 units
ScoreCaptions.goto(0, 110)
#write the the Users score and maximum score 
ScoreCaptions.write("Users Score:0 Maximum Score:0",
                    align="center",  #alignment is center, and its font is Courier New
                    font = ('Courier New', 10, "bold"))
#Results as a turtle function
Results = turtle.Turtle()
#the speed of the results is zero
Results.speed(0)
#out of several options for the results, there are several options for the color
Resultscolor = random.choice(['blue', 'red', 'green', 'yellow', 'brown', 'black'])
#the shape is a square
Results.shape('square')
#penup() – not "touching" the window
Results.penup()
#• hideturtle() – do not display the turtle. Speeds up drawing
Results.hideturtle()
#original position of the results is 0, 110 units
Results.goto(0, 110)

#Results1 as a turtle function
Results1 = turtle.Turtle()
#the speed of the results1 is zer0
Results1.speed(0)
#out of several options for the results1, there are several options for the color
Resultscolor1 = random.choice(['blue', 'red', 'green', 'yellow', 'brown', 'black'])
#the shape is a square
Results1.shape('square')
#penup() – not "touching" the window
Results1.penup()
#• hideturtle() – do not display the turtle. Speeds up drawing
Results1.hideturtle()
#original position of the results is 0, 110 units
Results1.goto(0, 110)

#Results2 as a turtle function
Results2 = turtle.Turtle()
#the speed of the results2 is zer0
Results2.speed(0)
#out of several options for the results2, there are several options for the color
Resultscolor2 = random.choice(['blue', 'red', 'green', 'yellow', 'brown', 'black'])
#the shape is a square
Results2.shape('square')
#penup() – not "touching" the window
Results2.penup()
#• hideturtle() – do not display the turtle. Speeds up drawing
Results2.hideturtle()
#original position of the results is 0, 110 units
Results2.goto(0, 110)

#function for the direction of the snake moving up
def snakemotionup():
    #the direction of the snake moving up
    headofsnake.direction = "Up"
#function for the direction of the snake moving down
def snakemotiondown():
    headofsnake.direction = "Down"
#function for the direction of the snake moving left
def snakemotionleft():
    headofsnake.direction = "Left"  
#function for the direction of the snake moving right
def snakemotionright():
    headofsnake.direction = "Right"
#function for the direction of the full snake motion in all 4 directions
def fullsnakemotion():
    # moving up 
    if headofsnake.direction == "Up":
        # the ycoordinate of the headsnake to move a certain amount of units
        y = headofsnake.ycor()
        # the ycoordinate of the headsnake to move a certain amount of units
        headofsnake.sety(y + 10)
        
    # moving down 
    if headofsnake.direction == "Down":
        # the ycoordinate of the headsnake to move a certain amount of units
        y = headofsnake.ycor()
        # the ycoordinate of the headsnake to move a certain amount of units
        headofsnake.sety(y - 10)
    
    # moving left
    if headofsnake.direction == "Left":
        # the xcoordinate of the headsnake to move a certain amount of units
        x = headofsnake.xcor()
        # the xcoordinate of the headsnake to move a certain amount of units
        headofsnake.setx(x - 10)
    
    # moving right 
    if headofsnake.direction == "Right":
                # the xcoordinate of the headsnake to move a certain amount of units
        x = headofsnake.xcor()
                # the xcoordinate of the headsnake to move a certain amount of units
        headofsnake.setx(x + 10)

#listen() – sets focus on turtle window to record actions
snakegamewindow.listen()
#onkey(fun, key) – calls a function when a specific key, i,  is pressed
snakegamewindow.onkeypress(snakemotionup, key = "i")
#onkey(fun, key) – calls a function when a specific key, o,  is pressed
snakegamewindow.onkeypress(snakemotiondown, key = "o")
#onkey(fun, key) – calls a function when a specific key, j,  is pressed
snakegamewindow.onkeypress(snakemotionleft, key = "j")
#onkey(fun, key) – calls a function when a specific key, k,  is pressed
snakegamewindow.onkeypress(snakemotionright, key = "k")

#using a while loop
while True:
    #update each time a new loop occurs
    snakegamewindow.update()

    #conditional of an if and else statement 
    #if the head of the snake xcoordinate is greater than 200 
    if headofsnake.xcor() > 200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake xcoordinate is less than -200   
    if headofsnake.xcor() < -200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold")) 
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is greater than 200   
    if headofsnake.ycor() > 200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than -200   
    if headofsnake.ycor() < -200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
                #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than 20 and captures the food
    if headofsnake.distance(foodforsnake) < 20:
        #the food is at any random point both as a x and 
        # y coordinate across the screen
        #within its border
        xcoordinate = random.randint(-200, 200)
        ycoordinate = random.randint(-200, 200)
        #the origin point for the foodofsnake is x, y
        foodforsnake.goto(xcoordinate, ycoordinate)
        #if the player captures the food, its +10 points
        playerscore += 10
        #the maximum score is equal to the player score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold"))     

    #finish of the level 1 as there are three levels for the game
    #if the player's score exceeds 100
    if playerscore > 100:
            #clear() – clear window but do not reset turtle or variables
            Results.clear()
            #The results will be 100 units down from the origin displaying the title, you have finished level
            Results.goto(0, -100)
            #writing the caption, you have finished level 1 in the center, similar to the score
            Results.write("You Have Finished Level 1.",
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
    
#update each time a new loop occurs
    snakegamewindow.update()

    #conditional of an if and else statement 
    #if the head of the snake xcoordinate is greater than 200 
    if headofsnake.xcor() > 200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake xcoordinate is less than -200   
    if headofsnake.xcor() < -200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold")) 
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is greater than 200   
    if headofsnake.ycor() > 200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than -200   
    if headofsnake.ycor() < -200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
                #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than 20 and captures the food
    if headofsnake.distance(foodforsnake) < 20:
        #the food is at any random point both as a x and 
        # y coordinate across the screen
        #within its border
        xcoordinate = random.randint(-200, 200)
        ycoordinate = random.randint(-200, 200)
        #the origin point for the foodofsnake is x, y
        foodforsnake.goto(xcoordinate, ycoordinate)
        #if the player captures the food, its +10 points
        playerscore += 10
        #the maximum score is equal to the player score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold"))     
    #the second level results
    #if the player's score exceeds 500 points
    if playerscore > 500:
            #clear() – clear window but do not reset turtle or variables
            Results1.clear()
            #the results for the second level is 70 units below the origin point 
            Results1.goto(0, -70)
            #the results will display the caption you have finished level 2 and center it
            Results1.write("You Have Finished Level 2.",
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
            
    #update each time a new loop occurs
    snakegamewindow.update()

    #conditional of an if and else statement 
    #if the head of the snake xcoordinate is greater than 200 
    if headofsnake.xcor() > 200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake xcoordinate is less than -200   
    if headofsnake.xcor() < -200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold")) 
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is greater than 200   
    if headofsnake.ycor() > 200: 
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
        #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than -200   
    if headofsnake.ycor() < -200:
        #the time for sleep is 1 
        time.sleep(1)
        #origin point of the headofsnake
        headofsnake.goto(0, 0)
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
            playerscore, maximumscore),
                    align="center", 
                    font = ('Courier New', 10, "bold"))
                #if the player hits the wall its minus 30 points
        playerscore -= 30
        #the maximum score of the player will also equal the player's score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
        #if the head of the snake ycoordinate is less than 20 and captures the food
    if headofsnake.distance(foodforsnake) < 20:
        #the food is at any random point both as a x and 
        # y coordinate across the screen
        #within its border
        xcoordinate = random.randint(-200, 200)
        ycoordinate = random.randint(-200, 200)
        #the origin point for the foodofsnake is x, y
        foodforsnake.goto(xcoordinate, ycoordinate)
        #if the player captures the food, its +10 points
        playerscore += 10
        #the maximum score is equal to the player score
        maximumscore = playerscore
        #clear() – clear window but do not reset turtle or variables
        ScoreCaptions.clear()
        #write the scorecaptions for the when the headofthesnake hits the wall
        #in the format of the socre, and the maximum score in the cneter in Courier New 10
        ScoreCaptions.write("Users Score:{} Maximum Score : {}".format(
                playerscore, maximumscore),
                        align="center", 
                        font = ('Courier New', 10, "bold"))     
        
    #if the player's score exceeds 1000
    if playerscore > 1000:
            #clear() – clear window but do not reset turtle or variables
            Results2.clear()
            ##the results will be displayed 40 units below the origin point
            Results2.goto(0, -40)
            #write the results in the center of the caption, you have successfully completed the task at hand 
            Results2.write("You Have Successfully Completed the Task at Hand.",
                        align="center", 
                        font = ('Courier New', 10, "bold")) 
    #close the function of the full motion of the snake
    fullsnakemotion()
#close the overall window
snakegamewindow.mainloop()