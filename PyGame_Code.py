# Python program to move the image
# with the mouse

# Import the library pygame
import pygame
import cv2; import numpy as np
from pygame.locals import *

# Construct the GUI game

# Set dimensions of game GUI

# Take image as input

'''

UNCOMMENT THIS FOR USER-INTERACTIVE SCRIPT

bg_img_path = input("Enter Product Image Path: ")
bg_img = cv2.imread(bg_img_path)
stencil_path = input("Enter Stencil Image Path: ")
fore_img = cv2.imread(stencil_path)

'''
bg_img = cv2.imread("Obj1.png")
bg_img = cv2.Canny(bg_img,100,200)
cv2.imwrite("bg_img_con.png",bg_img)
#cv2.imshow("test", bg_img)
#cv2.waitKey(0)
fore_img = cv2.imread("Obj1_stencil.png")
#cv2.imshow("test",bg_img)
cv2.waitKey(0)
height , width = bg_img.shape
pygame.init()
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
#bg_img = pygame.image.load('Actual.png')
bg_img = pygame.image.load('bg_img_con.png')
bg_img = pygame.transform.scale(bg_img,(width,height))
bg_img.set_alpha(100)  #########################################

global sten_width, sten_height
img1 = cv2.resize(fore_img,(0,0),fx=0.3,fy=0.3)
sten_height, sten_width, __ = img1.shape
cv2.imwrite("Stencil_resize.png", img1)
fore_img = pygame.image.load("Stencil_resize.png")

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
    for event in events:
        # Close if the user quits the
        # game
        if event.type == QUIT:
            running = False

        # Making the image move
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        # elif event.button
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
        # elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
        #     if event.button == 4:
        #         print("MOUSEWHEEL UP")
        #         action = "MOUSEWHEEL UP"
        #         fore_img = pygame.image.load("Obj1_stencil.png")
        #         sten_width, sten_height = sten_width*1.1, sten_height*1.1
        #         fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
        #         fore_img.set_alpha(80)
        #     if event.button == 5:
        #         print("MOUSEWHEEL DOWN")
        #         action = "MOUSEWHEEL DOWN"
        #         fore_img = pygame.image.load("Obj1_stencil.png")
        #         sten_width, sten_height = sten_width * 0.9, sten_height * 0.9
        #         fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
        #         fore_img.set_alpha(80)
        #     text = f'button {event.button} {action} in the position {event.pos}'
        #     print(text)
        if event.type == pygame.QUIT:
            loop = 0
        elif event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            if event.type == pygame.MOUSEBUTTONDOWN:
                action, color = "pressed", (0, 255, 255)
            if event.type == pygame.MOUSEBUTTONUP:
                action, color = "released", (255, 64, 64)
            if event.button == 4:
                print("MOUSEWHEEL UP")
                action = "MOUSEWHEEL UP"
                fore_img = pygame.image.load("Obj1_stencil.png")
                sten_width, sten_height = sten_width * 1.02, sten_height * 1.02
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)
            if event.button == 5:
                print("MOUSEWHEEL DOWN")
                action = "MOUSEWHEEL DOWN"
                fore_img = pygame.image.load("Obj1_stencil.png")
                sten_width, sten_height = sten_width * 0.98, sten_height * 0.98
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)

    screen.blit(bg_img, (0, 0))
    screen.blit(fore_img, rect)
    #pygame.draw.rect(screen, BLUE, rect, 1)
    pygame.display.update()

pygame.quit()
