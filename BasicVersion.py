import time
from PIL import ImageGrab, ImageOps
import pyautogui
from numpy import *
from numpy import ndarray


class coordinates():
    replaybutton = (300,300)
    dino = (65,314)

def restartGame():
    pyautogui.click(coordinates.replaybutton)
def jump():
    pyautogui.keyDown('space')
    time.sleep(0.00001)
    pyautogui.keyUp('space')
def obstacleBox():
    box = (80,320,175,342)                 
    image = ImageGrab.grab(box)
    grayImage = ImageOps.grayscale(image)
    a = array(grayImage.getcolors())
    print(a.sum())
    return a.sum()

restartGame()
while True:
    obstacleBox()
    if (obstacleBox()!=2337):
        jump()
        time.sleep(0.0001)
        exit