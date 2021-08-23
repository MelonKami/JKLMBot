import pytesseract, requests, json
# cv2.cvtColor takes a numpy ndarray as an argument
import numpy as nm
# importing OpenCV
import cv2
from PIL import ImageGrab

# Getting started https://www.geeksforgeeks.org/python-using-pil-imagegrab-and-pytesseract/

while True:

    keyword = input('Hva vil du finne et ord for?: ')

    response = requests.get(f'https://api.datamuse.com/words?ml={keyword}&max=1000')

    json_str = json.loads(response.text)

    pytesseract.pytesseract.tesseract_cmd ='**Path to tesseract executable**'
    cap = ImageGrab.grab(bbox =(700, 300, 1400, 900))

    tesstr = pytesseract.image_to_string(
                cv2.cvtColor(nm.array(cap), cv2.COLOR_BGR2GRAY), 
                lang ='eng')

    #print(json_str)

    for word in json_str:
        #print(word)
        if keyword in word["word"]:
            print(word)

    # print(json_str)

