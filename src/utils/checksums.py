def calculate_checksum(file_path):
    import hashlib

    hash_md5 = hashlib.md5()
    with open(file_path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()

def log_checksums(directory, output_file):
    import os

    checksums = {}
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.pdf'):
                file_path = os.path.join(root, file)
                checksums[file] = calculate_checksum(file_path)

    with open(output_file, 'w') as f:
        for file_name, checksum in checksums.items():
            f.write(f"{file_name}: {checksum}\n")

if __name__ == "__main__":
    log_checksums('./input_pdfs', './fine_tune_ses_docguard/data_raw_checksums.txt')