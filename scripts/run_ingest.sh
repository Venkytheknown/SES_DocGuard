#!/bin/bash

# This script runs the PDF ingestion process for SES-DocGuard

# Navigate to the project directory
cd "$(dirname "$0")/.."

# Run the PDF ingestion script
python src/ingest.py

# Notify completion
echo "PDF ingestion completed."