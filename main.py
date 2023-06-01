import time
import pygame
import random
import math
def show_go_screen():
    global score
    #puts the backgroup image over the screen
    screen.blit(background_image, (0, 0))
    #makes a render for the score
    textImg = font.render(str(score), 1, white)
    #puts the score on the screen
    screen.blit(textImg, (400, 300))
    #makes the render for the text on the game over screen
    text_surface = font.render("Game Over! You Lose!", True, white)
    screen.blit(text_surface, (200, 100))
    text_surface = font.render("Final Score!", True, white)
    screen.blit(text_surface, (300, 200))
    pygame.display.flip()
    global done
    #the while true list for the end screen
    again = False
    while again == False:
        for event in pygame.event.get():
            #sets up the quit function for the game and the repeat
            if event.type == pygame.QUIT:
                again = True
                done = True
                start = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    again = True
                    start = False
                    done = False
        clock.tick(20)
class Button(pygame.sprite.Sprite):
    #The button class for all button functions
    def __init__(self,x,y,direction,buttonType,rand):
        #Gets information to what we will pass throught the function
        pygame.sprite.Sprite.__init__(self)
        #setting the directions and movement and spawnpoints
        self.Direction = direction
        self.ButtonType = buttonType
        self.spawn = y
        self.rand = rand
        if buttonType == 1:
            #This gives each button it's atributes like speed, image and score
            buttonImage = pygame.image.load("startbutpng.png")
            if dif == 1:
                self.Speed = random.randint(5, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 0
        elif buttonType == 2:
            buttonImage = pygame.image.load("easybutton.png")
            if dif == 1:
                self.Speed = random.randint(5, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 0
        elif buttonType == 3:
            buttonImage = pygame.image.load("mediumbutton.png")
            if dif == 1:
                self.Speed = random.randint(5, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 0
        elif buttonType == 4:
            buttonImage = pygame.image.load("hardbutton.png")
            if dif == 1:
                self.Speed = random.randint(5, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 0
        if buttonType == 1:
            #This sets the size of each of the different buttons
            self.image = pygame.Surface([120, 80])
        if buttonType >= 2:
            self.image = pygame.Surface([120, 80])
        #Sets the x, y and other values for the button like the blit onto the screen
        self.image.set_colorkey(black)
        self.image.blit(buttonImage, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def moveButtons(self):
        #Code for the moveButton function that allows the buttons to update their x and y value and move in the sine curve
        if self.Direction == "right":
            self.rect.x += self.Speed
        if self.Direction == "left":
            self.rect.x -= self.Speed
        #This is the code for the wave pattern that the button moves in
        Time = time.time()
        clock2 = (Time + self.rand) % (math.pi * 2)
        output = math.sin(clock2)
        height = 50 * (output)
        self.rect.y = self.spawn + height
class Balloon(pygame.sprite.Sprite):
    #This is the class for balloons that can be called for the balloon function and properties
    def __init__(self,x,y,direction,balloonType,rand):
        pygame.sprite.Sprite.__init__(self)
        #This gives the balloon its spawn and its atributes
        self.Direction = direction
        self.BalloonType = balloonType
        self.spawn = y
        self.rand = rand
        #Defines the type of balloon and the different atributes of each individual balloon
        if balloonType == 1:
            balloonImage = pygame.image.load("bev.png")
            self.balloonSound = pygame.mixer.Sound("bevpop.wav")
            #chnages the speed based on difficulty
            if dif == 1:
                self.Speed = random.randint(1, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 5
        if balloonType == 2:
            balloonImage = pygame.image.load("waje.png")
            self.balloonSound = pygame.mixer.Sound("hey.wav")
            if dif == 1:
                self.Speed = random.randint(1, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 15
        if balloonType == 3:
            balloonImage = pygame.image.load("Jai.png")
            self.balloonSound = pygame.mixer.Sound("jai.wav")
            if dif == 1:
                self.Speed = random.randint(1, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 10
        if balloonType == 4:
            balloonImage = pygame.image.load("Declan.png")
            self.balloonSound = pygame.mixer.Sound("fart.wav")
            if dif == 1:
                self.Speed = random.randint(1, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 10
        if balloonType == 5:
            balloonImage = pygame.image.load("Thane.png")
            self.balloonSound = pygame.mixer.Sound("stop.wav")
            if dif == 1:
                self.Speed = random.randint(1, 5)
            if dif == 2:
                self.Speed = random.randint(10, 20)
            if dif == 3:
                self.Speed = random.randint(20, 50)
            self.Score = 0
        #helding to render the balloon by setting the balloons size
        if balloonType == 1:
            self.image = pygame.Surface([67, 90])
        elif balloonType == 2:
            self.image = pygame.Surface([90, 120])
        elif balloonType == 3:
            self.image = pygame.Surface([60, 80])
        elif balloonType == 4:
            self.image = pygame.Surface([68, 90])
        elif balloonType == 5:
            self.image = pygame.Surface([90, 90])
        else:
            self.image = pygame.Surface([26,50])
        #gives the balloon the starting area to appear on the screen and its x and y values
        self.image.set_colorkey(black)
        self.image.blit(balloonImage,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    #the code for moving a balloon and changing direction once it has hit the wall
    def moveBalloons(self):
       if self.Direction == "right":
           self.rect.x += self.Speed
       if self.Direction == "left":
           self.rect.x -= self.Speed
        #the sin wave curve that the balloons follow
       Time = time.time()
       clock2 = (Time + self.rand) % (math.pi * 2)
       output = math.sin(clock2)
       height = 50 * (output)
       self.rect.y = self.spawn + height
#the code for rendering text and putting the text and the screen
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))
class Dart(pygame.sprite.Sprite):
#the calable class for the dart and its atributes
    def __init__(self):
        #contains the information for the dart like the image, where to render and its size
        pygame.sprite.Sprite.__init__(self)
        dartImage = pygame.image.load("pointer.png")
        self.image = pygame.Surface([90, 45])
        self.image.set_colorkey(black)
        self.image.blit(dartImage,(0,0))
        self.rect = self.image.get_rect()
        self.rect.x = 398
        self.rect.y = 190
    #code to move the dart by changing its x and y values based on the mouse position
    def moveDart(self, mousePosition):
        self.rect.x = mousePosition[0]
        self.rect.y = mousePosition[1]
#initialises the pygame
pygame.init()
#sets the screen size
screen = pygame.display.set_mode([800,400])
#sets the caption to Balloon Burst
pygame.display.set_caption("Balloon Burst")
#sets the background image to a picture of st.Stanislaus college
background_image = pygame.image.load("stan.jpeg").convert()
pygame.mouse.set_visible(False)
#the variables for the loops being set as false so the game can begin
done = False
start = False
#the clock function for frames
clock = pygame.time.Clock()
#defines black and white as the colours of black and white
black    = (   0,   0,   0)
white    = ( 255, 255, 255)
#sets the font size and type
font = pygame.font.Font(None, 36)
color = (255, 255, 255)
#the audio variables for the game
popSound = pygame.mixer.Sound("pop.wav")
yoo = pygame.mixer.Sound("yoo.wav")
game = pygame.mixer.Sound("game.wav")
#some of the sprite groups used to put images into groups based on their atributes
otherBalloons = pygame.sprite.Group()
pinkBalloons = pygame.sprite.Group()
blueBalloons = pygame.sprite.Group()
allBalloons = pygame.sprite.Group()
allButtons = pygame.sprite.Group()
starButton = pygame.sprite.Group()
difButton = pygame.sprite.Group()
#decides the time until the next button or balloon will spawn
timeTillNextBalloon = random.randint(1000,2000)
timeTillNextButton = random.randint(1000,2000)
#sets the mouse position
mousePosition = [0]*2
#sets the starting score to 0
score = 0
#defines dart and make a sprite group for the dart for collisions
dart = Dart()
darts = pygame.sprite.Group()
darts.add(dart)
#render for the dart
render_offset = [0, 0]
#the starting difficulty variable
dif = 1
# defining fonts
font = pygame.font.SysFont("arialblack", 40)
#the first loop, this particular one for the main menu mini game that is used to simulate the different difficulties
while start == False:
    #starts by checking for events in the loop
    for event in pygame.event.get():
        #sets a quit function to kill the app
        if event.type == pygame.QUIT:
            done = True
        #creates the cursor and allows it to move with the mouse
        if event.type == pygame.MOUSEMOTION:
            mousePosition[:] = list(event.pos)
            dart.moveDart(mousePosition)
        #the event that controls collisions between the dart and the buttons
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hitButtons = pygame.sprite.groupcollide(allButtons,darts,False, False)
            for button in (hitButtons):
                #the code for when the start button has been hit
                if button in (starButton):
                    #starts the actual game
                    start = True
                    #plays music and a sound effect
                    yoo.play()
                    game.play()
                    #wooga is the variable used to make balloons starts spawning after and not before reaching the game
                    wooga = pygame.time.get_ticks()
                    #kills and the buttons
                    for button in allButtons:
                        button.kill()
                elif button in (difButton):
                    #the code for if the button hit was a difficulty button
                    if buttonType == 2:
                        #sets the difficulty to easy
                        dif = 1
                        #kills the button
                        button.kill()
                    elif buttonType == 3:
                        #sets the difficulty to medium
                        dif = 2
                        #kills the button
                        button.kill()
                    elif buttonType == 4:
                        #sets the difficulty to hard
                        dif = 3
                        #kills the button
                        button.kill()
            pygame.sprite.spritecollide(dart,allButtons, True, collided = None)
    #code for the spawn time for the buttons
    if pygame.time.get_ticks() > timeTillNextButton:
        #randomising the time between spawns
        timeTillNextButton += random.randint(1000, 3500)
        #randomly choosing the y axis spawn point
        yCoord = random.randint(50,350)
        #picking the button type that will spawn
        buttonType = random.randint(1,4)
        #the start of the code for the sine wave used for the buttons
        rand = random.uniform(0, 2*math.pi)
        button = Button(0,yCoord,"right",buttonType,rand)
        if buttonType ==1:
            #adds the buttons the the different sprite groups used ofr collisions
            starButton.add(button)
        elif buttonType >= 2:
            difButton.add(button)
        allButtons.add(button)
    #code for the changing direction when the button hits either side of the screen
    for button in (allButtons.sprites()):
        if button.rect.x < 0:
            button.Direction = "right"
        if button.rect.x > 774:
            button.Direction = "left"
    #allows the button to move
    for button in (allButtons.sprites()):
        button.moveButtons()
    #sets the background image for the loop
    screen.blit(background_image, [0,0])
    allButtons.draw(screen)
    #draws the buttons on the screen
    darts.draw(screen)
    #draws the darts on the screen
    textImg = font.render(str("SOFTWARE MAYHAM"),1,white)
    #creates the variable for the title screen text
    screen.blit( textImg, (10,10) )
    #renders the text onto the screen
    pygame.display.flip()
    #refreshes the screen
    clock.tick(20)
#the loop for the actual game
while done == False:
    #checks for events in the main game
    for event in pygame.event.get():
        #gives the user the ability to quit using the quit function
        if event.type == pygame.QUIT:
            #sets the end of the main game to true
            done = True
        #the code for the movvement of the dart with the mouse
        if event.type == pygame.MOUSEMOTION:
            mousePosition[:] = list(event.pos)
            dart.moveDart(mousePosition)
        #if the event detected is a collsion between the dart sprite group and the allBalloons sprite group
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            hitBalloons = pygame.sprite.groupcollide(allBalloons,darts,False, False)
            for balloon in (hitBalloons):
                #enacts what happens for each balloon
                if balloon in (blueBalloons):
                    #if the balloon is in the blue balloon sprite group it will play the sound associated with
                    #that balloon and set the end of the game to true
                    balloon.balloonSound.play()
                    done = True
                elif balloon in (pinkBalloons):
                    #if the balloon hit is a 'pink balloon' it will play the sound and kill all blue balloobs
                    balloon.balloonSound.play()
                    for balloon in (blueBalloons):
                        balloon.kill()
                else:
                    balloon.balloonSound.play()
                    #adds the self score of the balloon hit to the total socre
                    score += balloon.Score
            pygame.sprite.spritecollide(dart,allBalloons, True, collided = None)
    #the code for the time between balloon spawn, assigning sprite groups, randomising events and making sure balloons
    #don't spawn on the main menu
    if pygame.time.get_ticks() - wooga > timeTillNextBalloon:
        #gives the balloon a random spawn time
        timeTillNextBalloon += random.randint(1000, 3500)
        #gives the balloon a random y spawn
        yCoord = random.randint(50,350)
        #randomly picks which balloon will spawn
        balloonType = random.randint(1,5)
        #the code for the sine wave for the balloons
        rand = random.uniform(0, 2*math.pi)
        balloon = Balloon(0,yCoord,"right",balloonType,rand)
        #assigning sprite groups to balloons
        if balloonType >=1 and balloonType <=3:
            otherBalloons.add(balloon)
        elif balloonType == 4:
            pinkBalloons.add(balloon)
        else:
            blueBalloons.add(balloon)
        allBalloons.add(balloon)
    #the code to make ballons bounce on the walls
    for balloon in (allBalloons.sprites()):
        if balloon.rect.x < 0:
            balloon.Direction = "right"
        if balloon.rect.x > 774:
            balloon.Direction = "left"
    #allows the balloons to move
    for balloon in (allBalloons.sprites()):
        balloon.moveBalloons()
    #renders the background image on the screen
    screen.blit(background_image, [0,0])
    #drawns the balloons onto the screen
    allBalloons.draw(screen)
    #draws the dart onto the screen
    darts.draw(screen)
    #assings the atributes to the variable used for the score
    textImg = font.render(str(score),1,white)
    #renders the score onto the screen
    screen.blit( textImg, (10,10) )
    #refreshes the screen
    pygame.display.flip()
    clock.tick(20)
#calls the code for the end/game over screen
show_go_screen()
#waits 5 seconds so the user can see their score
time.sleep(5)
#kills the game
pygame.quit()
#THE END :)
