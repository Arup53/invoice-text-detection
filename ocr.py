import requests
from PIL import Image
from paddleocr import PaddleOCR, draw_ocr
import numpy as np
from io import BytesIO



def perform_ocr(img_url):
    ocr = PaddleOCR(use_angle_cls=True, lang='en')

    # Download the image
    response = requests.get(img_url)
    img = Image.open(BytesIO(response.content))

    # Convert the image to a numpy array
    img = np.array(img)

    # Perform OCR
    result = ocr.ocr(img, cls=True)
    extracted_text = []

    # Extract the text and confidence
    for idx in range(len(result)):
        res = result[idx]
        for line in res:
            text, confidence = line[1]  # line[1] is (text, confidence)
            print(text)
            extracted_text.append(text)

    return extracted_text



