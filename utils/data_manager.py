import json
import os

DATA_DIR = "data"

def load_data(filename):
    file_path = os.path.join(DATA_DIR, filename)
    if not os.path.exists(file_path):
        return {}
    try:
        with open(file_path, 'r') as f:
            content = f.read().strip()  
            if not content: 
                return {}
            return json.load(f)
    except json.JSONDecodeError:
        return {} 

def save_data(filename, data):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    file_path = os.path.join(DATA_DIR, filename)
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)