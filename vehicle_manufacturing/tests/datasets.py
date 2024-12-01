import kagglehub
import os
from pathlib import Path
from colors import colors_ansi


class KaggleDatasetCollector:


    def raw_data(origin_dataset) -> None:
        # Download latest version
        print(f'{colors_ansi('light_green')}{">" * 5} DOWNLOADING...')
        try:
            path = kagglehub.dataset_download(origin_dataset)
        except Exception as error:
            print(f'{colors_ansi('magenta')}FILE NOT FOUND!{colors_ansi('reset')}')
            raise error
        
        print(f'{colors_ansi('cyan')}{">" * 5} PATH TO DATASET FILES: {colors_ansi('reset')}{path}')
        print(f'{colors_ansi('light_yellow')}{">" * 5} MOVING FILES TO SAMPLE DIRECTORY...{colors_ansi('reset')}')

        for file in os.listdir(path):
            fixed_file_name = (str(file).replace(' ', '_')).lower()
            os.rename(os.path.join(path, file), os.path.join(Path.cwd(), 'samples', fixed_file_name))

        print(f'{colors_ansi('light_green')}{">" * 5} PROCESS FINISHED!{colors_ansi('reset')}')