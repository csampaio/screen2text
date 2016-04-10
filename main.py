# -*- coding: utf-8 -*-
import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import ocr_space
import json
import pyautogui
import time

imgfile = "test.bmp"

def tesseract_test():
    #ImageGrab.grab_to_file(imgfile)
    img  = Image.open(imgfile)
    return pytesseract.image_to_string(img)

def ocr_space_test():
    test_file = ocr_space.ocr_space_file(filename=imgfile, language='eng')
    result = json.load(test_file)
    return result

def autogui_test():
    print("start")
    time.sleep(5)
    pyautogui.screenshot('img/screen.png')
    search_image('img/bandeira.png')
    search_image('img/scroller.png')


def search_image(image):
    location = pyautogui.locateOnScreen(image)
    if (location != None):
        print(location)
        x,y = pyautogui.center(location)
        pyautogui.moveTo(x,y,duration=2,tween=pyautogui.pytweening.easeInOutQuad)
    else:
        print(image + " não encontrado.")

if __name__ == "__main__":
    autogui_test()



