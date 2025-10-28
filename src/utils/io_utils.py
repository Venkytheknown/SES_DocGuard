def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def write_json(data, file_path):
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)

def read_csv(file_path):
    import pandas as pd
    return pd.read_csv(file_path)

def write_csv(data, file_path):
    import pandas as pd
    data.to_csv(file_path, index=False)

def checksum_file(file_path):
    import hashlib
    hasher = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()