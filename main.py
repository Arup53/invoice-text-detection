from fastapi import FastAPI
from ocr import perform_ocr
from extraction import extract_invoice_data
app = FastAPI()

@app.get("/ocr")
async def ocr_endpoint(image_url: str):
    # Call the perform_ocr function with the image URL
    extracted_text = perform_ocr(image_url)
    structured_output= extract_invoice_data(extracted_text)

    return {"extracted_text": structured_output}