import torch
from torch.utils.data import Dataset
import os


class TransformedImageDataset(Dataset):
    def __init__(self, images_path, labels_path):
        self.images_path = images_path
        self. labels_path = labels_path
        self.len = len(os.listdir(self.images_path))

    def __getitem__(self, item):
        single_image_path = self.images_path + f'/img{item}.pt'
        single_label_path = self.labels_path + f'/lbl{item}.pt'
        try:
            image_tensor = torch.load(single_image_path)
            label_tensor = torch.load(single_label_path)
        except FileNotFoundError:
            raise IndexError
        return [image_tensor, label_tensor]

    def __len__(self):
        return self.len