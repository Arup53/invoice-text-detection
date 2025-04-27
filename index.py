import requests
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import numpy as np
from io import BytesIO

ocr = PaddleOCR(use_angle_cls=True, lang='en')

# Download the image
url = 'https://templates.invoicehome.com/invoice-template-us-neat-750px.png'
response = requests.get(url)
img = Image.open(BytesIO(response.content))

# You must convert it to a numpy array

img = np.array(img)

# img_path = './testimag.png'
result = ocr.ocr(img, cls=True)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        text, confidence = line[1]  # line[1] is (text, confidence)
        print(text)
