import pytesseract
from PIL import ImageGrab
import sounddevice as sd
import soundfile as sf
import time

import soundfile as sf

import os

file_name = "snd_lancerlaugh.wav"
abs_path = os.path.abspath(file_name)

print(f"Current working directory: {os.getcwd()}")
print(f"Absolute path to file: {abs_path}")
print(f"File exists: {os.path.exists(file_name)}")
print(f"File size: {os.path.getsize(file_name) if os.path.exists(file_name) else 'N/A'} bytes")


print(sf.info("snd_lancerlaugh.wav"))


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"       
suppress_number = 0
screenshot = ImageGrab.grab()
print(screenshot.height)
screenshot = screenshot.crop((screenshot.width/2,0,screenshot.width,250))
screenshot.save("test.png")

text = pytesseract.image_to_string(screenshot)
print(text)
print("finished")

keyLevels = [20,40,90,95,110,150,160,190]


if not str(suppress_number) in text:
    for num in keyLevels:
        if str(num) in text:
            print("found number", num)
            suppress_number = num

time.sleep(2)


    