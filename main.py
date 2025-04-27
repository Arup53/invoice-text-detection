from fastapi import FastAPI
from groqtest import invoice_extractor_groq
app = FastAPI()

@app.get("/ocr")
async def ocr_endpoint(image_url: str):
    # Call the invoice_extractor_groq function with the image URL
    extracted_text = invoice_extractor_groq(image_url)
    
    # Ensure the extracted_text is already a JSON object
    # If it's not a valid JSON object, we can parse it here (optional, depending on groq response)
    if isinstance(extracted_text, str):
        import json
        extracted_text = json.loads(extracted_text)
    
    return {"extracted_text": extracted_text}