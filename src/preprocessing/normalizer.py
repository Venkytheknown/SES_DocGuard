def normalize_text(text):
    # Normalize whitespace
    normalized_text = ' '.join(text.split())
    
    # Convert to lowercase
    normalized_text = normalized_text.lower()
    
    # Additional normalization steps can be added here
    
    return normalized_text

def remove_special_characters(text):
    import re
    # Remove special characters using regex
    cleaned_text = re.sub(r'[^a-zA-Z0-9\s]', '', text)
    return cleaned_text

def normalize_pdf_content(pdf_content):
    # Normalize the text content extracted from the PDF
    normalized_content = normalize_text(pdf_content)
    cleaned_content = remove_special_characters(normalized_content)
    return cleaned_content

# Example usage
if __name__ == "__main__":
    sample_text = "This is a sample PDF content!  \nIt contains various   special characters & symbols."
    normalized = normalize_pdf_content(sample_text)
    print(normalized)