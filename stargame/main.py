#apple = star
#player = rocket

import pygame
import sys
import random

pygame.init() #starts up pygame
screen = pygame.display.set_mode((350, 600)) #creates a screen of width 350 and length 600
clock = pygame.time.Clock() #sets up an FPS(frames per second)

class Apple: 
    def __init__(self, image, position, speed):
        self.image = image 
        self.rect = self.image.get_rect(topleft = position)
        self.speed = speed
    def move(self):
        self.rect.y = self.rect.y + self.speed
#variables
speed = 3
score = 0

#constants
TILESIZE = 32





#floor
floor_image = pygame.image.load('stargame/assets/floor.png').convert_alpha()
floor_image = pygame.transform.scale(floor_image, (TILESIZE*15, TILESIZE*5))
floor_rect = floor_image.get_rect(bottomleft = (0, screen.get_height()))

# player
player_image = pygame.image.load('stargame/assets/player_static.png').convert_alpha() #convert alpha line optimizes the image in pygame
player_image = pygame.transform.scale(player_image, (TILESIZE, TILESIZE*(1.356467))) #paratheses is a tuple w the size of the player, in thise case tile size is a constant
player_rect = player_image.get_rect(center = (screen.get_width()/2, screen.get_height() - floor_image.get_height() - (player_image.get_height()/2))) #places the player at the center. To make center it does the height of the screen minus the height of the floor, minus half the height of the player

#apple
apple_image = pygame.image.load('stargame/assets/apple.png').convert_alpha()
apple_image = pygame.transform.scale(apple_image, (TILESIZE, TILESIZE))

apples = [
    Apple(apple_image, (100,0), 3),
    Apple(apple_image, (300,0), 3)
]

#fonts
font = pygame.font.Font('stargame/assets/PixeloidMono.ttf', int(TILESIZE/2))
#sound effects
pickup = pygame.mixer.Sound('stargame/assets/powerup.mp3')
pickup.set_volume(0.2) #set volume to a value between 0 and 1

#game loop
runnning = True

def update():
    global speed
    global score

    keys = pygame.key.get_pressed() #checks if keys r being pressed

    if keys[pygame.K_LEFT]:
        player_rect.x = player_rect.x - 8 #moves the x value of player_rect left by 8
    elif keys[pygame.K_RIGHT]:
        player_rect.x = player_rect.x + 8 #moves the x value of player_rect right by 8

    #apple movingx
    for apple in apples:
        apple.move() #calling the move method for each apple in apples
        if apple.rect.colliderect(floor_rect): #apple will go away if it hits the ground and a new one will appear
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50,300), -50), speed))
        elif apple.rect.colliderect(player_rect):
            apples.remove(apple)
            apples.append(Apple(apple_image, (random.randint(50,300), -50), speed))
            speed = speed + 0.1
            score = score + 1
            pickup.play()

def draw(): #gives screen a color/background
    screen.fill("darkblue")
    screen.blit(player_image, player_rect) #numnbers in parenthesis puts the player at a spot on the screen
    screen.blit(floor_image, floor_rect) #puts the floor on the screen, rect uses the x and y value of the floor_rect instead of a hard coded value

    for apple in apples:
        screen.blit(apple.image, apple.rect) #for each apple in apples list, it draws its unique image and position
    score_text = font.render(f'Score: {score}', True, "white") #inside the brackets u can put a variable
    screen.blit(score_text, (5,5))


while runnning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    #above 4 lines make it so the user has a way to close the screen
     
    update()

    draw()
    clock.tick(60) #sets up the FPS
    pygame.display.update() #keeps the screen on ur screen





