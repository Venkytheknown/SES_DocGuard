def parse_pdf(pdf_path):
    import PyPDF2

    text_content = ""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text_content += page.extract_text() + "\n"
    
    return text_content.strip()  # Clean up any leading/trailing whitespace

# Additional functions for OCR and noise filtering can be added here if needed.