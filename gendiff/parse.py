import json

import yaml

from pathlib import Path

    
def parse(path_to_file):
    path = Path(path_to_file)
    suff = path.suffix.lower()

    with open(path_to_file) as file:
        if suff == '.yaml' or suff == '.yml':
            return yaml.safe_load(file)
        elif suff == '.json':
            return json.load(file)
        
    raise ValueError(f'Unsupported file format: {suff}')