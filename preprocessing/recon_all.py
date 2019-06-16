#!/bin/env python3
import glob
from os.path import join

if __name__ == "__main__":
    # Set dataset folder
    dataset_folder = '/home/jullygh/Downloads/MS/extracted'

    # Find files in folder
    files = glob.glob(join(dataset_folder, '*.nii.gz'))
    for f in files:
        print(f)

    print(f'Total files found: {len(files)}')
