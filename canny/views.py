from matplotlib import pyplot as plt
from canny.services import ImageToNumberArray, ExecuteLambda, Hough, Haar
import cv2 as cv
import numpy as np

from util.dataset import Dataset


class MenuController(object):

    @staticmethod
    def menu_0(*params):
         print(params[0])

    @staticmethod
    def menu_1(*params):
        print(params[0])
        img = ExecuteLambda('IMAGE_READ_FOR_CV', params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        img = ExecuteLambda('GRAY_SCALE', arr)
        plt.imshow(ExecuteLambda('IMAGE_FROM_ARRAY', img))
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
        haar = cv.CascadeClassifier(f"{Dataset().context}{param[1]} ")
        girl = param[2]
        girl_original = ExecuteLambda('IMAGE_READ_FOR_PLT', girl)
        girl_gray = ExecuteLambda('GRAY_SCALE', girl_original)
        girl_canny = cv.Canny(np.array(girl_original), 10, 100)
        lines = cv.HoughLinesP(girl_canny, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        girl_hough = cv.cvtColor(girl_canny, cv.COLOR_GRAY2BGR)
        girl_haar = haar.detectMultiScale(girl_original, minSize=(150, 150))

        plt.subplot(151), plt.imshow(girl_original, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        Haar(girl_haar, girl_hough, girl_original, lines)

        plt.subplot(152), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(girl_original, cmap='gray')
        plt.title('HAAR Image'), plt.xticks([]), plt.yticks([])
        plt.show()




    @staticmethod
    def menu_6(*param):
        pass




