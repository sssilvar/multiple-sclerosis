#!/bin/env python3
import glob
from os.path import join

if __name__ == "__main__":
    # Set dataset folder
    dataset_folder = '/disk/Datasets/ADNI/FreeSurferSD'

    # Find files in folder
    files = glob.glob(join(dataset_folder, 'patient*_study1_T1W.nii.gz'))
    for f in files:
        print(f)

    print(f'Total files found: {len(files)}')