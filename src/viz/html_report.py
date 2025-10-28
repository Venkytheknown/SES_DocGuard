def generate_html_report(validation_results, output_path):
    html_content = """
    <html>
    <head>
        <title>Validation Report</title>
        <style>
            body { font-family: Arial, sans-serif; }
            table { width: 100%; border-collapse: collapse; }
            th, td { border: 1px solid #ddd; padding: 8px; }
            th { background-color: #f2f2f2; }
        </style>
    </head>
    <body>
        <h1>Validation Report</h1>
        <table>
            <tr>
                <th>Rule ID</th>
                <th>Description</th>
                <th>Severity</th>
                <th>Confidence</th>
                <th>Suggestion</th>
                <th>Evidence Snippet</th>
            </tr>
    """

    for result in validation_results:
        html_content += f"""
            <tr>
                <td>{result['rule_id']}</td>
                <td>{result['rule_description']}</td>
                <td>{result['severity']}</td>
                <td>{result['confidence']}</td>
                <td>{result['suggestion']}</td>
                <td>{result['evidence_snippet']}</td>
            </tr>
        """

    html_content += """
        </table>
    </body>
    </html>
    """

    with open(output_path, 'w') as file:
        file.write(html_content)

# Example usage
# generate_html_report(validation_results, 'output_report.html')