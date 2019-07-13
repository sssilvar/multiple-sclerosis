# https://academictorrents.com/
import os
from os.path import join, splitext

import pandas as pd
import nibabel as nb
from PIL import Image
import scipy.io as sio

import torch
from torchvision import transforms
from torch.utils.data import Dataset


class MSLoizouDataset(Dataset):
    """
    Free Multiple sclerosis database.
    Info: http://www.medinfo.cs.ucy.ac.cy/
    """

    def __init__(self, root):
        self.data = pd.read_excel(join(root, 'PatientCodes-Names.xls')).dropna(axis='rows', how='all').reset_index()
        self.root = root

    def __getitem__(self, index):
        """
        :param index: Number of element (patient) to be returned
        :return: tuple: (image, target) where target is the lession mask
        """
        code = self.data['CODE'][index]
        subject_folder = join(self.root, code, '1')

        slides = [splitext(i)[0] for i in os.listdir(subject_folder) if i.endswith('.plq') and len(i.split('_')) == 2]
        print(slides)

        img = Image.open(join(self.root, code, '1', f'{slides[0]}.TIF'))
        target = sio.loadmat(join(self.root, code, '1', f'{slides[0]}.plq'))

        return img, target

    def __len__(self):
        return len(self.data)


class MSISBIDataset(Dataset):
    def __init__(self, root, train=True):
        self.root = root
        self.train = train
        self.data = None

        # Transforms
        self.to_tensor = transforms.ToTensor()
        self.pipeline = transforms.Compose([
            # transforms.ToTensor(),
            transforms.Normalize((0.5,), (0.5,))
        ])

        self.get_data_file()

    def __getitem__(self, index):
        # if self.train:
        #     sid = self.data['sid'][index]
        #     number = sid[-2:]
        #     subject_folder = join(self.root, 'training', sid)
        #     nii_img = join(subject_folder, 'preprocessed', f'training{number}_01_flair_pp.nii')
        #     nii_mask = join(subject_folder, 'masks', f'training{number}_01_mask1.nii')

        # print(nii_mask, nii_img)
        # Load images and extract values
        # img = torch.tensor([nb.load(nii_img).get_data()[:50, :50, :50]], dtype=torch.float)
        # mask = torch.tensor([nb.load(nii_mask).get_data()[:50, :50, :50]], dtype=torch.float)
        img = torch.rand(size=(1, 48, 64, 64))
        mask = torch.rand(size=(1, 48, 64, 64)) > 0.5

        return img, mask

    def __len__(self):
        return len(self.data)

    def get_data_file(self):
        if self.train:
            self.data = [i for i in range(5)]  # pd.read_csv(join(self.root, 'training', 'training.csv'))
        else:
            self.data = pd.read_csv(join(self.root, 'testdata_website', 'testing.csv'))
