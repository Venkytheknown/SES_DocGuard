def merge_results(validation_results):
    merged_results = {}

    for result in validation_results:
        pdf_name = result['source']
        if pdf_name not in merged_results:
            merged_results[pdf_name] = []

        merged_results[pdf_name].append({
            'rule_id': result['rule_id'],
            'rule_description': result['rule_description'],
            'severity': result['severity'],
            'confidence': result['confidence'],
            'suggestion': result['suggestion'],
            'evidence_snippet': result['evidence_snippet'],
            'offsets': result['offsets']
        })

    return merged_results

def save_merged_results(merged_results, output_dir='./data/processed'):
    for pdf_name, results in merged_results.items():
        output_json_path = os.path.join(output_dir, f"{pdf_name}_merged.json")
        with open(output_json_path, 'w') as json_file:
            json.dump(results, json_file, indent=4)

if __name__ == "__main__":
    # Placeholder for validation results input
    validation_results = []  # This should be populated with actual validation results
    merged_results = merge_results(validation_results)
    save_merged_results(merged_results)