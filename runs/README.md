# README.md for the runs directory

This directory contains the outputs from various runs of the SES-DocGuard project. Each run may include model training results, evaluation metrics, and generated reports. 

## Structure

- **Output Files**: Each run will generate output files such as JSON detection results, HTML reports, and logs.
- **Run Identifiers**: Each output will be organized by a unique run identifier to facilitate tracking and comparison of different runs.

## Usage

1. **Accessing Outputs**: After running the ingestion, training, or evaluation scripts, check this directory for the generated outputs.
2. **File Naming Convention**: Output files will follow a naming convention that includes the run identifier and the type of output (e.g., `run_001_detection.json`, `run_001_report.html`).
3. **Metrics**: Evaluation metrics will be logged in a structured format for easy analysis.

## Note

Ensure to regularly clean up old runs if storage becomes an issue, and consider archiving important outputs for future reference.