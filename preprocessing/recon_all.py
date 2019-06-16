#!/bin/env python3
import os
import glob
from multiprocessing.pool import Pool
from os.path import join, isdir, basename


def recon_all(vol_file):
    sid = basename(vol_file).split('_')[0]
    t2_file = vol_file.replace('T1Wreg.nii.gz', 'T2Wreg.nii.gz')
    cmd = f'recon-all -i {vol_file} -T2 {t2_file} -s {sid} -sd {out_folder} -all'
    print(cmd)

if __name__ == "__main__":
    # Set dataset folder
    dataset_folder = '/home/jullygh/Downloads/MS/extracted/*'
    pattern = join(dataset_folder, 'patient*_study1_T1Wreg.nii.gz')
    print(f'Finging pattern: {pattern}')

    # Output Folder
    out_folder = '/home/jullygh/Downloads/MS/processed_fs/'

    # Find files in folder
    files = glob.glob(pattern, recursive=True)
    print(f'Total files found: {len(files)}')
    confirm = input('Start [y/n]:')
    
    if confirm == 'y':
        # Process subjects in parallel
        pool = Pool(20)
        pool.map(recon_all, files)
    else:
        print('No process started')
    print('Done')
