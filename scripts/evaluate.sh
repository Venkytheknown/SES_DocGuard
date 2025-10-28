#!/bin/bash

# Evaluate the model using the evaluation script
echo "Starting model evaluation..."

# Set the paths for the evaluation script and output directory
EVALUATION_SCRIPT="src/evaluator/metrics.py"
OUTPUT_DIR="data/processed/evaluation_results"

# Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Run the evaluation script and redirect output to a log file
python $EVALUATION_SCRIPT > $OUTPUT_DIR/evaluation_log.txt

echo "Model evaluation completed. Results saved to $OUTPUT_DIR/evaluation_log.txt"