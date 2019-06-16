#!/bin/env python3
import glob
from os.path import join, isdir
from multiprocessing.pool import Pool

def recon_all(subject_id):
    pass

if __name__ == "__main__":
    # Set dataset folder
    dataset_folder = '/home/jullygh/Downloads/MS/extracted/*'
    pattern = join(dataset_folder, 'patient*_study1_T1Wreg.nii.gz')
    print(f'Finging pattern: {pattern}')

    # Output Folder
    out_folder = '/home/jullygh/Downloads/MS/processed_fs/'
    if not isdir(out_folder):
        os.mkdir(out_folder)

    # Find files in folder
    files = glob.glob(pattern, recursive=True)
    for f in files:
        print(f)

    print(f'Total files found: {len(files)}')
