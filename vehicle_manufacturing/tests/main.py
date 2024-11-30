from datasets import KaggleDatasetCollector as kdc

def load_dataset():
    kdc.raw_data(origin_dataset="arnavsmayan/vehicle-manufacturing-dataset")


if __name__ == '__main__':
    load_dataset()
