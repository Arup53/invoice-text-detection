from fastapi import FastAPI
from ocr import perform_ocr
app = FastAPI()

@app.get("/ocr")
async def ocr_endpoint(image_url: str):
    # Call the perform_ocr function with the image URL
    extracted_text = perform_ocr(image_url)
    return {"extracted_text": extracted_text}