# filepath: SES-DocGuard/src/cli.py
import argparse
from src.ingest import ingest_pdfs

def main():
    parser = argparse.ArgumentParser(description='SES-DocGuard Command Line Interface')
    parser.add_argument('--input_dir', type=str, default='./input_pdfs', help='Directory containing input PDFs')
    parser.add_argument('--output_dir', type=str, default='./data/processed', help='Directory to save output JSONs')
    
    args = parser.parse_args()
    
    results = ingest_pdfs(input_dir=args.input_dir)
    
    print(f"Ingestion complete. Results saved to {args.output_dir}.")
    for pdf_file, result in results.items():
        print(f"Processed {pdf_file}: {result['validation']}")

if __name__ == "__main__":
    main()