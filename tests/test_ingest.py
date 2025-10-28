def test_ingest():
    import os
    import json
    from src.ingest import ingest_pdfs

    def mock_parse_pdf(pdf_path):
        return "Mocked text content from PDF."

    def mock_apply_asd_ste_rules(text_content):
        return [
            {
                "rule_id": "R1",
                "rule_description": "Mandatory field presence check.",
                "severity": "high",
                "confidence": 0.95,
                "suggestion": "Add the missing mandatory field.",
                "evidence_snippet": "Missing field evidence."
            }
        ]

    # Replace the actual functions with mocks
    original_parse_pdf = ingest_pdfs.__globals__['parse_pdf']
    original_apply_asd_ste_rules = ingest_pdfs.__globals__['apply_asd_ste_rules']
    ingest_pdfs.__globals__['parse_pdf'] = mock_parse_pdf
    ingest_pdfs.__globals__['apply_asd_ste_rules'] = mock_apply_asd_ste_rules

    # Create a temporary input directory and PDF file
    input_dir = './input_pdfs'
    os.makedirs(input_dir, exist_ok=True)
    test_pdf_path = os.path.join(input_dir, 'test_document.pdf')
    with open(test_pdf_path, 'w') as f:
        f.write("This is a test PDF document.")

    # Run the ingest function
    results = ingest_pdfs(input_dir)

    # Check the results
    expected_output = {
        'test_document.pdf': {
            'text': "Mocked text content from PDF.",
            'validation': [
                {
                    "rule_id": "R1",
                    "rule_description": "Mandatory field presence check.",
                    "severity": "high",
                    "confidence": 0.95,
                    "suggestion": "Add the missing mandatory field.",
                    "evidence_snippet": "Missing field evidence."
                }
            ]
        }
    }

    assert results == expected_output, f"Expected {expected_output}, but got {results}"

    # Clean up
    os.remove(test_pdf_path)
    os.rmdir(input_dir)

    # Restore original functions
    ingest_pdfs.__globals__['parse_pdf'] = original_parse_pdf
    ingest_pdfs.__globals__['apply_asd_ste_rules'] = original_apply_asd_ste_rules