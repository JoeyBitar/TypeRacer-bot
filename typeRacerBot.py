from pynput.keyboard import Key, Controller
from pynput import keyboard
import pyscreenshot as ImageGrab
import pyautogui
import time
import pytesseract
import cv2

class Coordinates:
    def __init__(self) -> None:
        self.firstScreenShotX = 0
        self.firstScreenShotY = 0
        word = ""
    
    def setStartingX(self, x):
        self.firstScreenShotX = x

    def setStartingY(self, y):
        self.firstScreenShotY = y


def recordStartingCoordinates(xy):
    coordinates.setStartingX(xy.x)
    coordinates.setStartingY(xy.y)

def on_press(key):
    if key == Key.ctrl_l:
        recordStartingCoordinates(pyautogui.position())
        print(pyautogui.position())

    elif key == Key.alt_l:
        print(pyautogui.position())
        im = ImageGrab.grab(bbox=(coordinates.firstScreenShotX, coordinates.firstScreenShotY, pyautogui.position().x, pyautogui.position().y))
        im.save("coordinates.png")
        img = cv2.imread("coordinates.png")
        words = pytesseract.image_to_string(img)
        coordinates.word = words
    elif key == Key.esc:
        quit()
    elif key == Key.space:
        typeTheWord(coordinates.word)
    else:
        pass
    
def reset():
    coordinates.firstScreenShotX = 0
    coordinates.firstScreenShotY = 0
    coordinates.word = ""

def on_release(key):
    pass

def typeTheWord(word):
    word = word.replace("|", "I").replace("\n", " ").replace("[","T").strip()
    print(word)
    
    if word[0] == "{":
        word = word[1:]
    for i in range(0, len(word)):
        if word[i] == "." and (i != len(word)-1) and str.isupper(word[i+1]):
            word[i] = ","
        keyboardPresser.press(word[i])
        keyboardPresser.release(word[i])
        time.sleep(0.03)
    reset()


 
keyboardPresser = Controller()
coordinates = Coordinates()
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'



with keyboard.Listener(
    on_press=on_press,
    on_release=on_release) as listener:
    listener.join()












