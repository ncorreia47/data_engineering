from datasets import KaggleDatasetCollector as kdc
import os
from pathlib import Path
import pandas as pd
import numpy as np
from colors import colors_ansi

def load_dataset():
    kdc.raw_data(origin_dataset="arnavsmayan/vehicle-manufacturing-dataset")

    df = pd.read_csv(os.path.join(Path.cwd(), 'samples/car_data.csv'))
    return df


def create_new_sample(sample_limit=10) -> pd.DataFrame():
    df = load_dataset()

    print(f'{colors_ansi('cyan')}{">" * 5} INITIALIZING SAMPLE CREATION...{colors_ansi('reset')}')
    # Create unique values list
    car_info = df[['Car ID', 'Brand', 'Model']].drop_duplicates()
    color_info = df[['Color']].drop_duplicates()
    location_info = df[['Location']].drop_duplicates()
    mileage_values = df[['Mileage']].drop_duplicates()
    price_values = df[['Price']].drop_duplicates()
    
    # Randomize data
    print(f'{colors_ansi('light_magenta')} RANDOMIZING DATA...{colors_ansi('reset')}')
    cars_samples = car_info.iloc[np.random.randint(0, high=len(car_info), size=sample_limit, dtype=int)]
    colors_samples = color_info.iloc[np.random.randint(0, high=len(color_info), size=sample_limit, dtype=int)]
    location_samples = location_info.iloc[np.random.randint(0, high=len(location_info), size=sample_limit, dtype=int)]
    mileage_values = mileage_values.iloc[np.random.randint(0, high=len(mileage_values), size=sample_limit, dtype=int)]
    price_values = price_values.iloc[np.random.randint(0, high=len(price_values), size=sample_limit, dtype=int)]
    print(f'{colors_ansi('light_magenta')} RANDOMIZATION COMPLETED!{colors_ansi('reset')}')

    # Create sample dataset
    print(f'{colors_ansi('light_magenta')} CREATING SAMPLE DATASET...{colors_ansi('reset')}')
    sample = pd.concat([cars_samples.reset_index(drop=True), 
                     colors_samples.reset_index(drop=True),
                     location_samples.reset_index(drop=True),
                     mileage_values.reset_index(drop=True),
                     price_values.reset_index(drop=True)], axis=1)
    print(f'{colors_ansi('light_magenta')} SAMPLE DATASET CREATED!{colors_ansi('reset')}')

    return pd.concat([df, sample])

        
if __name__ == '__main__':
    create_new_sample(5000)
