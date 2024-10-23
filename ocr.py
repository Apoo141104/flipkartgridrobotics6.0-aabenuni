import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'/opt/homebrew/bin/tesseract'
import cv2
from pillow_heif import register_heif_opener
from PIL import Image
import numpy as np

register_heif_opener()

# Read the HEIC file
heif_file = Image.open('datasetpqc/gits_dhokla/gits_dhokla_packof1/gits dhokla mix pack of 1 and its expiry date_9.jpg')

# Convert PIL Image to numpy array (OpenCV format)
img = cv2.cvtColor(np.array(heif_file), cv2.COLOR_RGB2BGR)

if img is None:
    print("Error: Unable to load the image. Please check the file path and format.")
else:
    cv2.imshow('', img)
    cv2.waitKey(10)
    cv2.destroyAllWindows()
    text = pytesseract.image_to_string(img)
    print(text)
