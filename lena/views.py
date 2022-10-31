import cv2

from lena.models import LennaModel
from titanic.models import TitanicModel
from util.dataset import Dataset


class LennaController(object):
    model = LennaModel()
    def __init__(self):
        pass

    def __str__(self):
        return f""
    
    dataset = Dataset()

    def preprocess(self, fname) -> object: # 전처리
        img = self.model.new_model(fname)
        return img

    def modeling(self,fname) -> object:
        img = self.preprocess(fname)
        return img
    
    def learning(self): # 기계학습
        pass
    
    def submit(self): # 배포
        pass


if __name__=="__main__":
    pass
