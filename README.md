# SES-DocGuard

SES-DocGuard is a Python-based GenAI application developed for SafranES, designed to process technical publication PDFs and apply the ASD STE ruleset for error detection. This project aims to enhance the quality and compliance of technical documents such as CMMs, ESMs, AMMs, and Service Bulletins.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Installation

To set up the SES-DocGuard project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd SES-DocGuard
   ```

2. **Install Dependencies**:
   You can install the required packages using either `requirements.txt` or `environment.yml`:
   - Using pip:
     ```bash
     pip install -r requirements.txt
     ```
   - Using conda:
     ```bash
     conda env create -f environment.yml
     ```

3. **Set Up Google Colab**:
   If you are using Google Colab, open the `notebooks/SES_DocGuard_Colab.ipynb` file and follow the instructions provided in the notebook.

## Usage

1. **Input PDFs**: Place your PDF files in the `input_pdfs` directory.

2. **Run the Ingestion Process**:
   Execute the ingestion script to process the PDFs and apply the ASD STE rules:
   ```bash
   python src/ingest.py
   ```

3. **Train the Model**:
   To train the model, run the training script:
   ```bash
   bash scripts/train.sh
   ```

4. **Evaluate the Model**:
   After training, evaluate the model using:
   ```bash
   bash scripts/evaluate.sh
   ```

5. **Check Outputs**: Review the outputs in the `data/processed` directory and any generated reports.

## Project Structure

```
SES-DocGuard
├── README.md
├── LICENSE
├── pyproject.toml
├── requirements.txt
├── environment.yml
├── .gitignore
├── .github
│   └── workflows
│       └── ci.yml
├── configs
│   ├── tokenizer_config.yaml
│   ├── model_config.yaml
│   ├── training_config.yaml
│   └── rules
│       ├── asd_ste_ruleset_example.yaml
│       └── README.md
├── data
│   ├── raw
│   │   ├── manuals
│   │   │   ├── CMMs
│   │   │   ├── ESMs
│   │   │   ├── AMMs
│   │   │   └── ServiceBulletins
│   │   ├── annotated_samples
│   │   ├── glossary
│   │   │   └── controlled_vocab.csv
│   │   └── protected
│   └── processed
├── fine_tune_ses_docguard
│   ├── data
│   │   ├── raw
│   │   └── processed
│   ├── tokenizer
│   ├── models
│   │   ├── base
│   │   └── finetuned
│   ├── experiments
│   ├── logs
│   ├── notebooks
│   ├── deploy
│   └── data_raw_checksums.txt
├── input_pdfs
│   └── (place PDFs here)
├── notebooks
│   └── SES_DocGuard_Colab.ipynb
├── src
│   ├── __init__.py
│   ├── ingest.py
│   ├── cli.py
│   ├── pdf_ingest
│   │   ├── __init__.py
│   │   └── pdf_parser.py
│   ├── preprocessing
│   │   ├── __init__.py
│   │   ├── ocr.py
│   │   ├── noise_filters.py
│   │   └── normalizer.py
│   ├── tokenizer
│   │   ├── __init__.py
│   │   └── bpe_tokenizer.py
│   ├── model
│   │   ├── __init__.py
│   │   ├── transformer.py
│   │   └── trainer.py
│   ├── rule_engine
│   │   ├── __init__.py
│   │   ├── yaml_rules.py
│   │   └── model_checks.py
│   ├── merger
│   │   ├── __init__.py
│   │   └── results_merger.py
│   ├── evaluator
│   │   ├── __init__.py
│   │   └── metrics.py
│   ├── viz
│   │   ├── __init__.py
│   │   ├── html_report.py
│   │   └── attention_viz.py
│   └── utils
│       ├── __init__.py
│       ├── io_utils.py
│       ├── checksums.py
│       └── reproducibility.py
├── configs_examples
│   ├── tokenizer_config.yaml.example
│   ├── model_config.yaml.example
│   └── rules
│       └── asd_ste_rule_example.yaml
├── colab
│   ├── setup_colab.sh
│   └── SES_DocGuard_Colab.ipynb
├── scripts
│   ├── run_ingest.sh
│   ├── train.sh
│   └── evaluate.sh
├── tests
│   ├── __init__.py
│   ├── test_ingest.py
│   ├── test_tokenizer.py
│   ├── test_model.py
│   ├── test_evaluator.py
│   └── rules_tests
│       └── test_asd_ste_rule_stub.py
└── runs
    └── README.md
```

## Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.