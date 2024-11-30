import kagglehub
import os
import shutil
from pathlib import Path

# ANSI code colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

def raw_data():
    # Download latest version
    print(f'{GREEN}{">" * 5} DOWNLOADING...')
    try:
        path = kagglehub.dataset_download("arnavsmayan/vehicle-manufacturing-dataset")
    except Exception as error:
        print(f'{RED}FILE NOT FOUND!{RESET}')
        raise error
    
    print(f'{YELLOW}{">" * 5} PATH TO DATASET FILES: {RESET}{path}')
    print(f'{YELLOW}{">" * 5} MOVING FILES TO SAMPLE DIRECTORY...{RESET}')

    for file in os.listdir(path):
        shutil.move(os.path.join(path, file), os.path.join(Path.cwd(), 'samples', file))

    print(f'{GREEN}{">" * 5} PROCESS FINISHED!')