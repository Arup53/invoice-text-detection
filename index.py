from paddleocr import PaddleOCR, draw_ocr

ocr = PaddleOCR(use_angle_cls=True, lang='en')
img_path = './testimag.png'
result = ocr.ocr(img_path, cls=True)

for idx in range(len(result)):
    res = result[idx]
    for line in res:
        text, confidence = line[1]  # line[1] is (text, confidence)
        print(text)
