# -*- coding: utf-8 -*-
import pyscreenshot as ImageGrab
from PIL import Image
import pytesseract
import ocr_space
import json
import pyautogui
import time

imgfile = "img/03.PNG"

def main():
    #concatenate_images()
    test_teclado()


def test_teclado():
    time.sleep(2)
    print('INICIO')
    pyautogui.typewrite(['1', 'q', 'e', 'r'], interval=2)
    print('FIM')


def tesseract_test():
    #ImageGrab.grab_to_file(imgfile)
    img = Image.open(imgfile)
    ratio = 2
    s = (img.size[0]*ratio,img.size[1]*ratio)
    print(s)
    img = img.resize(s, Image.ANTIALIAS)
    temp_file = 'temp.bmp'
    img.save(temp_file,'bmp')
    #img = Image.open(temp_file)
    text = pytesseract.image_to_string(img)
    f = open('temp.txt','w')
    f.write(text)
    f.close()

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


def concatenate_images():
    images = list(map(Image.open, ['img\\02.png', 'img\\03.png', 'img\\04.png']))
    widths, heights = zip(*(i.size for i in images))

    total_heigth = sum(heights)
    max_width = max(widths)

    new_im = Image.new('RGBA', (max_width, total_heigth))

    y_offset = 0
    for im in images:
        new_im.paste(im, (0, y_offset))
        y_offset += im.size[1]

    new_im.save('img\\test.png')


if __name__ == "__main__":
    main()
