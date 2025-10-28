def extract_text_from_image(image_path):
    import pytesseract
    from PIL import Image

    # Load the image from the specified path
    image = Image.open(image_path)

    # Use Tesseract to do OCR on the image
    text = pytesseract.image_to_string(image)

    return text

def process_pdf_with_ocr(pdf_path):
    import pdf2image

    # Convert PDF to images
    images = pdf2image.convert_from_path(pdf_path)

    # Extract text from each image
    extracted_text = []
    for image in images:
        text = extract_text_from_image(image)
        extracted_text.append(text)

    return "\n".join(extracted_text)

def ocr_pipeline(pdf_path):
    # Process the PDF and extract text using OCR
    text_content = process_pdf_with_ocr(pdf_path)
    return text_content

if __name__ == "__main__":
    # This file is intended to be imported as a module, not run directly
    pass