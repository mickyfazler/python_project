# Chrome dinosor game automation
import pyautogui # pip install pyautogui
from PIL import Image, ImageGrab # pip install pillow

# pyautogui.keyDown("F")      # It will tlype F
# pyautogui.keyDown("Fazle")    # It will not work..BEcause in keydown you only type one word
import time

def hit(key):
    pyautogui.keyDown(key)
    return          # That means returning nothing

def isCollide(data):
    # Draw the rectangle for birds
    for i in range(300, 415):               # x value or width
        for j in range(410, 563):           # y value   or height
            if data[i, j] < 100:
                hit("down")
                return              

    for i in range(300, 415):
        for j in range(563, 650):
            if data[i, j] < 100:
                hit("up")
                return
    return

if __name__ == "__main__":
    print("Hey.. Dino game about to start in 3 seconds")
    time.sleep(2)
    # hit('up') 

    while True:
        image = ImageGrab.grab().convert('L')       # Taking screen shots and convert it to grayscale for faster...and another thing is it's easy to work with grayscale image rather than RGB IMage
        data = image.load()
        isCollide(data)
            
        # print(asarray(image))         # from numpy import asarray
        # Just for drawing 
        '''
        # Draw the rectangle for cactus
        for i in range(275, 325):
            for j in range(563, 650):
                data[i, j] = 0
        
        # Draw the rectangle for birds
        for i in range(250, 300):
            for j in range(410, 563):
                data[i, j] = 171
        image.save("Fazle.jpg")
        image.show()
        break
      '''

