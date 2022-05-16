# Python program to move the image
# with the mouse

# Import the library pygame
import pygame
import cv2
from pygame.locals import *

# Take colors input
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)

# Construct the GUI game
pygame.init()

# Set dimensions of game GUI
width , height = 640, 350
screen = pygame.display.set_mode((width, height))
img = cv2.imread("undefined-Imgur-transformed.jpeg")
# Take image as input
img1 = cv2.resize(img,(0,0),fx=0.3,fy=0.3)
cv2.imwrite("img2.jpeg", img1)
bg_img = pygame.image.load('img2.jpeg')
bg_img = pygame.transform.scale(bg_img,(width,height))
bg_img.set_alpha(100)  #########################################
fore_img = pygame.image.load("img1.png")
fore_img.set_alpha(100)
fore_img.convert()


# Draw width rectangle around the image
rect = fore_img.get_rect()
rect.center = width// 2, height // 2

# Set running and moving values
running = True
moving = False

# Setting what happens when game
# is in running state
while running:
    events = pygame.event.get()
    #for event in pygame.event.get():
    for event in events:
        # Close if the user quits the
        # game
        if event.type == QUIT:
            running = False

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        #elif event.button
        # Set moving as False if you want
        # to move the image only with the
        # mouse click
        # Set moving as True if you want
        # to move the image without the
        # mouse click
        elif event.type == MOUSEBUTTONUP:
            moving = False

        # Make your image move continuously
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)


    # Set screen color and image on screen
    #screen.fill("logo.png")
    screen.blit(bg_img, (0,0))
    screen.blit(fore_img, rect)

    # Construct the border to the image
    pygame.draw.rect(screen, BLUE, rect, 1)

    # Update the GUI pygame
    pygame.display.update()

# Quit the GUI game
pygame.quit()
