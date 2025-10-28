#!/bin/bash

# Step 1: Set up environment variables
export INPUT_DIR="./input_pdfs"
export OUTPUT_DIR="./fine_tune_ses_docguard/data/processed"
export TOKENIZER_CONFIG="./configs/tokenizer_config.yaml"
export MODEL_CONFIG="./configs/model_config.yaml"
export TRAINING_CONFIG="./configs/training_config.yaml"

# Step 2: Create output directory if it doesn't exist
mkdir -p $OUTPUT_DIR

# Step 3: Run the ingestion process
echo "Ingesting PDFs from $INPUT_DIR..."
python src/ingest.py

# Step 4: Train the model
echo "Starting model training..."
python src/model/trainer.py --tokenizer_config $TOKENIZER_CONFIG --model_config $MODEL_CONFIG --training_config $TRAINING_CONFIG --output_dir $OUTPUT_DIR

# Step 5: Notify completion
echo "Training completed. Outputs are saved in $OUTPUT_DIR."