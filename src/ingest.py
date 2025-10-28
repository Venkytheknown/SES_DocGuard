import os
import json
from src.pdf_ingest.pdf_parser import parse_pdf
from src.rule_engine.yaml_rules import apply_asd_ste_rules

def ingest_pdfs(input_dir='./input_pdfs'):
    pdf_files = [f for f in os.listdir(input_dir) if f.endswith('.pdf')]
    results = {}

    for pdf_file in pdf_files:
        pdf_path = os.path.join(input_dir, pdf_file)
        text_content = parse_pdf(pdf_path)
        validation_results = apply_asd_ste_rules(text_content)

        results[pdf_file] = {
            'text': text_content,
            'validation': validation_results
        }

        output_json_path = os.path.join(input_dir, f"{os.path.splitext(pdf_file)[0]}.json")
        with open(output_json_path, 'w') as json_file:
            json.dump(results[pdf_file], json_file, indent=4)

    return results

if __name__ == "__main__":
    ingest_pdfs()