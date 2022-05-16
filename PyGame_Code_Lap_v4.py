# Python program to move the image
# with the mouse

# Import the library pygame
import pygame; import pyautogui
import cv2; import time
import numpy as np
from pygame.locals import *

def FilterVal(bg_img, filt, ker_size):
    count = filt % 2
    if (count == 0):
        filt += 1
        kercount = ker_size%2
        if kercount == 0:
            ker_size += 1
        bg_img = cv2.GaussianBlur(bg_img, (filt, filt), 0)
        bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        bg_img = cv2.Laplacian(src=bg_img, ddepth=cv2.CV_8U, ksize=ker_size)
    else:
        kercount = ker_size % 2
        if kercount == 0:
            ker_size += 1
        bg_img = cv2.GaussianBlur(bg_img, (filt, filt), 0)
        bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
        bg_img = cv2.Laplacian(src=bg_img, ddepth=cv2.CV_8U, ksize=ker_size)
    return bg_img

def do_nothing(x):
    pass

#######################################   Real Image loading  ###########################################
global bg_img
bg_img = cv2.imread("Obj1.png")
#############################Canny Edge Detection ########################################
# bg_img = cv2.Canny(bg_img,150,200)
#################################Laplacian Detection###################################
# bg_img = cv2.GaussianBlur(bg_img, (3, 3), 0) # to reduce the noise
# bg_img = cv2.cvtColor(bg_img, cv2.COLOR_BGR2GRAY)
# bg_img = cv2.Laplacian(src=bg_img, ddepth=cv2.CV_8U, ksize=5)
#########################################################################################
# cv2.imwrite("bg_img_con.png",bg_img)

accpt_but = pygame.image.load("D:\\LnT_python\\pythonProject\\buttons\\Accept_but.png"'').convert_alpha()
rjct_but = pygame.image.load("D:\\LnT_python\\pythonProject\\buttons\\Reject_but.png").convert_alpha()
nxt_but = pygame.image.load('D:\\LnT_python\\pythonProject\\buttons\\Next_but.png').convert_alpha()
prv_but = pygame.image.load('D:\\LnT_python\\pythonProject\\buttons\\Prev_but.png').convert_alpha()

class Button():
    def __init__(self, x, y,image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
    def draw(self):
        screen.blit(self.image, (self.rect.x, self.rect.y))
















cv2.namedWindow('controls')
cv2.resizeWindow("controls", 700, 100)
cv2.createTrackbar('filter', 'controls', 1, 50, do_nothing)
cv2.createTrackbar('kernel', 'controls', 1, 31, do_nothing)

while (1):
    # show the image window
    bg_img = cv2.imread("Obj2.png")
    filt = int(cv2.getTrackbarPos('filter', 'controls'))
    kern_size = int(cv2.getTrackbarPos('kernel', 'controls'))
    bg_img_con = FilterVal(bg_img, filt, kern_size)
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
global strt_time

while running:
    strt_time = []
    #print(pyautogui.position())
    events = pygame.event.get()
    #pyautogui.moveTo(444,297)
   # pyautogui.mouseDown(button='left')
   # pyautogui.moveTo(992,484, 1)
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
                strt_time.append(time.time())
                print("MOUSEWHEEL UP")
                action = "MOUSEWHEEL UP"
                fore_img = pygame.image.load(StencilImg)
                sten_width, sten_height = sten_width * 1.02, sten_height * 1.02
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)
                rect = fore_img.get_rect()
                rect.center = sten_width // 2, sten_height // 2
                if len(strt_time)<=1:
                    pass
                else:
                    if strt_time[-1]-strt_time[0] < 1:
                        print(strt_time[-1],strt_time[0])
                        print("difference: ", strt_time[-1]-strt_time[0] )
                        print("Passing drag func..")
                        continue
                    else:
                        pyautogui.moveTo(444, 297)
                        pyautogui.mouseDown(button='left')
                        pyautogui.moveTo(992,484, 1)
            if event.button == 5:
                print("MOUSEWHEEL DOWN")
                action = "MOUSEWHEEL DOWN"
                fore_img = pygame.image.load(StencilImg)
                sten_width, sten_height = sten_width * 0.98, sten_height * 0.98
                fore_img = pygame.transform.scale(fore_img, (sten_width, sten_height))
                fore_img.set_alpha(80)
                rect = fore_img.get_rect()
                rect.center = sten_width // 2, sten_height // 2
                time.sleep(1)
                pyautogui.moveTo(444, 297)
                pyautogui.mouseDown(button='left')
                pyautogui.moveTo(992,484, 1)
    screen.blit(bg_img, (0, 0))
    screen.blit(fore_img, rect)
    # pygame.draw.rect(screen, BLUE, rect, 1)
    pygame.display.update()

pygame.quit()
