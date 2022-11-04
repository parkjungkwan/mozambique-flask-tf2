from matplotlib import pyplot as plt
from mosaic.services import ImageToNumberArray, Hough, Haar, mosaic
from util.lambdas import MosaicLambda
import cv2 as cv
import numpy as np
from util.dataset import Dataset
import copy
class MenuController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = MosaicLambda('IMAGE_READ_FOR_CV', params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        img = MosaicLambda('GRAY_SCALE', arr)
        plt.imshow(MosaicLambda('IMAGE_FROM_ARRAY', img))
        plt.show()


    @staticmethod
    def menu_3(*params):
        print(params[0])
        ### 디스크에서 읽는 경우 ###
        # img = cv.imread('./data/roi.jpg', 0)
        # img = cv.imread(img, 0)
        ### 메모리에서 읽는 경우 ###
        img = ImageToNumberArray(params[1])
        print(f'img type : {type(img)}')
        # img = GaussianBlur(img, 1, 1) cv.Canny() 를 사용하지 않는 경우 필요
        # img = Canny(img, 50, 150) cv.Canny() 를 사용하지 않는 경우 필요
        edges = cv.Canny(np.array(img), 100, 200)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(edges, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_4(*params):
        print(params[0])
        img = ImageToNumberArray(params[1])
        edges = cv.Canny(img, 100, 200) # (image, threshold 1=100, threshold 2=200)
        dst = Hough(edges)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*param):
        print(param[0])
        cat = cv.imread(f"{Dataset().context}{param[1]}")
        mos = mosaic(cat, (150, 150, 450, 450), 10)
        cv.imwrite(f'{Dataset().context}cat-mosaic.png', mos)
        cv.imshow('CAT MOSAIC', mos)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_6(*param):
        print(param[0])
        girl = param[2]
        girl_original = MosaicLambda('IMAGE_READ_FOR_PLT', girl)
        girl_gray = MosaicLambda('GRAY_SCALE', girl_original)
        girl_canny = cv.Canny(np.array(girl_original), 50, 51) # 최소/최대 임계치
        girl_hough = Hough(girl_canny)
        girl_clone = copy.deepcopy(girl_original)
        haar = cv.CascadeClassifier(f"{Dataset().context}{param[1]}")
        rect = Haar(haar, girl_clone)
        girl_mosaic = mosaic(girl_original, rect, 10)
        plt.subplot(161), plt.imshow(girl_original, cmap='gray')
        plt.title('Original'), plt.xticks([]), plt.yticks([])
        plt.subplot(162), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray'), plt.xticks([]), plt.yticks([])
        plt.subplot(163), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge'), plt.xticks([]), plt.yticks([])
        plt.subplot(164), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough'), plt.xticks([]), plt.yticks([])
        plt.subplot(165), plt.imshow(girl_clone, cmap='gray')
        plt.title('HAAR'), plt.xticks([]), plt.yticks([])
        plt.subplot(166), plt.imshow(girl_mosaic, cmap='gray')
        plt.title('MOSAIC'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_7(*param):
        pass









