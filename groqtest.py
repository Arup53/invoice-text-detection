from groq import Groq
from dotenv import load_dotenv
load_dotenv()
import os


# completion = client.chat.completions.create(
#     model="meta-llama/llama-4-scout-17b-16e-instruct",
#     messages=[
#         {
#             "role": "user",
#             "content": [
#                 {
#                     "type": "text",
#                     "text": "Answer the following:1. What is the name of the person or entity responsible for paying the bill? (Look for BILLTO or BILL TO or INVOICE TO similar keywords)2. What is the subtotal amount? (Look for the keyword Subtotal)3. What is the total amount? (Look for the keyword TOTAL) .List the answer in JSON format."
#                 },
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": "https://cdn.venngage.com/template/thumbnail/small/5b650276-1deb-4fa5-adee-a0b8b935cb37.webp"
#                     }
#                 }
#             ]
#         }
#     ],
#     temperature=1,
#     max_completion_tokens=1024,
#     top_p=1,
#     stream=False,
#     response_format={"type": "json_object"},
#     stop=None,
# )
# client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
# print(completion.choices[0].message.content)



client = Groq(api_key=os.environ.get("GROQ_API_KEY"))
def invoice_extractor_groq(image_url):
    
    completion = client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Answer the following:1. What is the name of the person or entity responsible for paying the bill? (Look for BILLTO or BILL TO or INVOICE TO similar keywords)2. What is the subtotal amount? (Look for the keyword Subtotal)3. What is the total amount? (Look for the keyword TOTAL) .List the answer in JSON format."
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": image_url  # Using the passed parameter
                        }
                    }
                ]
            }
        ],
        temperature=1,
        max_completion_tokens=1024,
        top_p=1,
        stream=False,
        response_format={"type": "json_object"},
        stop=None,
    )
    
    return completion.choices[0].message.content

# Example of calling the function with a specific image URL
# image_url = "https://cdn.venngage.com/template/thumbnail/small/5b650276-1deb-4fa5-adee-a0b8b935cb37.webp"
# result = invoice_extractor_groq(image_url)
# print(result)