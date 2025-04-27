import re

def extract_invoice_data(extracted_text):
    """
    Extract the Bill To name and Total amount from invoice text.
    
    Args:
        extracted_text (list): List of strings containing extracted text from an invoice
        
    Returns:
        dict: A dictionary containing 'bill_to_name' and 'total_amount'
    """
    # Try to find the bill-to name by position in the list
    # In your example, "BILLTO" is at position 5, and "John Smith" is at position 9
    bill_to_name = None
    for i, item in enumerate(extracted_text):
        if item == "BILLTO" and i + 4 < len(extracted_text):
            bill_to_name = extracted_text[i + 4]
            break
    
    # Extract total amount from the joined text
    text = " ".join(extracted_text)
    total_pattern = r"TOTAL\s*\$?(\d+\.\d+)"
    total_match = re.search(total_pattern, text)
    total_amount = total_match.group(1) if total_match else None
    
    return {
        "bill_to_name": bill_to_name,
        "total_amount": total_amount
    }