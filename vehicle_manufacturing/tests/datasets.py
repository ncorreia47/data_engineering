import kagglehub
import os
from pathlib import Path

# ANSI code colors
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
RESET = '\033[0m'

class KaggleDatasetCollector:


    def raw_data(origin_dataset) -> None:
        # Download latest version
        print(f'{GREEN}{">" * 5} DOWNLOADING...')
        try:
            path = kagglehub.dataset_download(origin_dataset)
        except Exception as error:
            print(f'{RED}FILE NOT FOUND!{RESET}')
            raise error
        
        print(f'{YELLOW}{">" * 5} PATH TO DATASET FILES: {RESET}{path}')
        print(f'{YELLOW}{">" * 5} MOVING FILES TO SAMPLE DIRECTORY...{RESET}')

        for file in os.listdir(path):
            fixed_file_name = (str(file).replace(' ', '_')).lower()
            os.rename(os.path.join(path, file), os.path.join(Path.cwd(), 'samples', fixed_file_name))

        print(f'{GREEN}{">" * 5} PROCESS FINISHED!')