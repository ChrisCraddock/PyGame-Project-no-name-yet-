import pygame
import math

pygame.init() #Initialize

#Create screen
screen = pygame.display.set_mode((1000, 800))

#Titile, Icon, Background
pygame.display.set_caption("Game Title Here")
""" 
TitleIcon = pygame.image.load()
pygame.set_icon(TitleIcon)
background = pygame.image.load()
"""

#Sound
"""Add sound here"""


#Player
playerIcon = pygame.image.load('player1.png')
playerX = 370
playerY = 480
playerX_change = 0
playerY_change = 0

def player(x,y):
    screen.blit(playerIcon, (x,y))

#Coordinates on screen
locationX_value = str(round(playerX,2))
locationY_value = str(round(playerY,2))
font = pygame.font.Font('freesansbold.ttf', 18) #Font style and size
textX = 10 #Text Location
textY = 10 #Text Location

def show_location(x,y):
    location = font.render("Location "+ str((locationX_value,locationY_value)) , True, (255,205,145)) #Render first.  Convert INT to STR, set as TRUE, Color of text
    screen.blit(location,(x,y))


#Launch Screen
running = True
while running:
    #RGB for screen
    screen.fill((0,0,0))
    #Background Image
    """ screen.blit(background,(0,0)) """
    #Enable game to be closed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -.1
                print("X: " + str(round(playerX,2)),"Y: " + str(round(playerY,2)))
            if event.key == pygame.K_RIGHT:
                playerX_change = +.1
                print("X: " + str(round(playerX,2)),"Y: " + str(round(playerY,2)))
            if event.key == pygame.K_UP:
                playerY_change = -.1
                print("X: " + str(round(playerX,2)),"Y: " + str(round(playerY,2)))
            if event.key == pygame.K_DOWN:
                playerY_change = +.1
                print("X: " + str(round(playerX,2)),"Y: " + str(round(playerY,2)))

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                playerX_change = 0 #If either key is released, stop moving
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                playerY_change = 0 #If either key is released, stop moving

    playerX += playerX_change#Update playerX variable value by the amount of the key pressed
    playerY += playerY_change#Update playerX variable value by the amount of the key pressed



#Update game to stay up
    player(playerX,playerY)
    show_location(textX,textY)
    pygame.display.update()