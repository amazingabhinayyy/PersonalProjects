import pytesseract
from PIL import ImageGrab
import sounddevice as sd
import soundfile as sf
import time
import os
import difflib

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def play_sound(file_name):
    file_path = os.path.join(SCRIPT_DIR, file_name)
    print("Using sound file:", file_path)
    data, fs = sf.read(file_path, dtype='float32')
    sd.play(data, fs)
    sd.wait()

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"       
suppress_number = 0
while True:
    screenshot = ImageGrab.grab()
    screenshot = screenshot.crop((1421,115,1795,160))
    screenshot.save("wtf.png")
    text = pytesseract.image_to_string(screenshot)

    keyLevels = [21,51,61,91,111,141,161,191]
    keyLevelsStr = [str(x) for x in keyLevels]
    allNums = [str(x) for x in range(1,201)]

    match = difflib.get_close_matches(text.strip(),allNums,1,0.6)
    if match:
        print(match[0])
        text = match[0]
    else:
        print(text)

    if not str(suppress_number) in text:
        for num in keyLevels:
            if str(num) in text:
                print("found number", num)
                suppress_number = num
                play_sound("snd_lancerlaugh.wav")
    
    time.sleep(2)


    