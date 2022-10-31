import cv2
import numpy as np
import pandas as pd
from util.dataset import Dataset

class LennaModel(object):

    dataset = Dataset()

    def __init__(self):
        pass
    def __str__(self):
        return ""

    def preprocess(self):

        pass

    def new_model(self, fname) -> object:
        this = self.dataset
        this.context = './data/'
        img = cv2.imread(this.context + fname)
        return img

if __name__ == '__main__':
    pass