# Python program to move the image
# with the mouse

# Import the library pygame
import pygame
import cv2
import numpy as np
from pygame.locals import *

def do_nothing(x):
    pass

#######################################   Real Image loading  ###########################################
bg_img = cv2.imread("Obj2.png")
#############################Canny Edge Detection ########################################
# bg_img = cv2.Canny(bg_img,150,200)
#################################Laplacian Detection###################################
# bg_img = cv2.GaussianBlur(bg_img, (3, 3), 0) # to reduce the noise
# bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
# bg_img = cv2.Laplacian(src=bg_img, ddepth=cv2.CV_8U, ksize=5)
#########################################################################################
# cv2.imwrite("bg_img_con.png",bg_img)

cv2.namedWindow('controls')
cv2.resizeWindow("controls", 700, 100)
cv2.createTrackbar('upper_Lim', 'controls', 50, 200, do_nothing)
cv2.createTrackbar('lower_Lim', 'controls', 100, 300, do_nothing)

while (1):
    # show the image window
    upp = int(cv2.getTrackbarPos('upper_Lim', 'controls'))
    low = int(cv2.getTrackbarPos('lower_Lim', 'controls'))
    bg_img_con = cv2.Canny(bg_img, upp, low)
    cv2.imwrite("bg_img_con.png", bg_img_con)
    cv2.imshow('img', bg_img_con)
    # wait for the user to press escape and break the while loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        cv2.imwrite("bg_img_con.png",bg_img_con)
        break
# destroys all window
cv2.destroyAllWindows()
#######################################   Stencil loading  ##############################################
StencilImg = "Obj1_stencil.png"
fore_img = cv2.imread(StencilImg)

height, width = bg_img_con.shape
pygame.init()
BLUE = (0, 0, 255)

screen = pygame.display.set_mode((width, height))
# bg_img = pygame.image.load('Actual.png')
bg_img_con = pygame.image.load('bg_img_con.png')
bg_img = pygame.transform.scale(bg_img_con, (width, height))
bg_img.set_alpha(100)  #########################################

global sten_width, sten_height
img1 = cv2.resize(fore_img, (0, 0), fx=0.3, fy=0.3)
sten_height, sten_width, __ = img1.shape
cv2.imwrite("Stencil_resize.png", img1)
fore_img = pygame.image.load("Stencil_resize.png")

fore_img.set_alpha(100)
fore_img.convert()

# Draw width rectangle around the image
rect = fore_img.get_rect()
rect.center = width // 2, height // 2

def valchange():
    print("hi")

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

        elif event.type == MOUSEBUTTONUP:
            moving = False

        # Make your image move continuously
        elif event.type == pygame.MOUSEMOTION and moving:
            rect.move_ip(event.rel)

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
                fore_img = pygame.image.load(StencilImg)
                sten_width, sten_height = sten_width * 1.02, sten_height * 1.02
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)
                rect = fore_img.get_rect()
                rect.center = sten_width // 2, sten_height // 2
            if event.button == 5:
                print("MOUSEWHEEL DOWN")
                action = "MOUSEWHEEL DOWN"
                fore_img = pygame.image.load(StencilImg)
                sten_width, sten_height = sten_width * 0.98, sten_height * 0.98
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)
                rect = fore_img.get_rect()
                rect.center = sten_width // 2, sten_height // 2

    screen.blit(bg_img, (0, 0))
    screen.blit(fore_img, rect)
    # pygame.draw.rect(screen, BLUE, rect, 1)
    pygame.display.update()

pygame.quit()
