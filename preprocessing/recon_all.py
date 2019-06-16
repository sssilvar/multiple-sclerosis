#!/bin/env python3
import glob
from os.path import join

if __name__ == "__main__":
    # Set dataset folder
    dataset_folder = '/home/jullygh/Downloads/MS/extracted/*'
    pattern = join(dataset_folder, 'patient*_study1_T1Wreg.nii.gz')
    print(f'Finging pattern: {pattern}')

    # Find files in folder
    files = glob.glob(pattern, recursive=True)
    for f in files:
        print(f)

    print(f'Total files found: {len(files)}')
