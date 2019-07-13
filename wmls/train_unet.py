#!/bin/env python3
import os

import pandas as pd
import matplotlib.pyplot as plt

import torch
from torch import nn, optim
from torchvision import transforms
from torch.utils.data import DataLoader
import torch.nn.functional as F

from datasets.ms import MSISBIDataset
from unet.unet_model import UNet
from vnet import VNet

if __name__ == '__main__':
    # Parameters
    epochs = 20

    # Load dataset
    dataset_folder = os.path.normpath('/disk/Datasets/MS/MS2')
    dataset = MSISBIDataset(dataset_folder)

    # CNN architecture
    # model = UNet(n_channels=1, n_classes=1)
    model = VNet(elu=False,nll=False)
    optimizer = optim.Adam(model.parameters())
    # loss_function = nn.BCELoss()
    loss_function = F.nll_loss

    # Train
    train_set = DataLoader(dataset, batch_size=1)

    for epoch in range(epochs):
        model.train()
        for inputs, outputs in train_set:
            print('Inputs shape', inputs.shape, outputs.shape)
            optimizer.zero_grad()
            results = model(inputs)
            print('Results shape', results.shape)
            loss = loss_function(results, outputs)
            loss.backward()
            optimizer.step()

        print(f'Epoch: {epoch} | Loss: {loss}')

    plt.figure()
    plt.imshow(inputs[0][0].numpy())
    plt.title('MRI')

    plt.figure()
    plt.imshow(outputs[0][0].numpy())
    plt.title('Groundtruth')

    plt.figure()
    plt.imshow(results[0][0].detach().numpy())
    plt.title('Result')

    plt.show()
