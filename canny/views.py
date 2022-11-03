from matplotlib import pyplot as plt
from PIL import Image
from canny.services import ImageToNumberArray, image_read
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
        img = image_read(params[1])
        print(f'cv2 버전 {cv.__version__}')  # cv2 버전 4.6.0
        print(f' Shape is {img.shape}')
        cv.imshow('Original', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    @staticmethod
    def menu_2(*params):
        print(params[0])
        arr = ImageToNumberArray(params[1])
        # 람다식 내부에서 GRAYSCALE 변환 공식 사용함
        img = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(arr)
        plt.imshow((lambda x: Image.fromarray(x))(img))
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
        edges = cv.Canny(img, 100, 200)
        lines = cv.HoughLinesP(edges, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        dst = cv.cvtColor(edges, cv.COLOR_GRAY2BGR)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(dst, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)
        plt.subplot(121), plt.imshow(img, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(122), plt.imshow(dst, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.show()

    @staticmethod
    def menu_5(*param):
        print(param[0])
        ds = Dataset()
        haar = cv.CascadeClassifier(f"{ds.context}{param[1]} ")
        girl = param[2]
        girl_original = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
        girl_gray = (lambda x: x[:, :, 0] * 0.114 + x[:, :, 1] * 0.587 + x[:, :, 2] * 0.229)(girl_original)
        girl_canny = cv.Canny(np.array(girl_original), 10, 100)
        lines = cv.HoughLinesP(girl_canny, 1, np.pi / 180., 120, minLineLength=50, maxLineGap=5)
        girl_hough = cv.cvtColor(girl_canny, cv.COLOR_GRAY2BGR)
        girl_haar = haar.detectMultiScale(girl_original, minSize=(150, 150))

        plt.subplot(151), plt.imshow(girl_original, cmap='gray')
        plt.title('Original Image'), plt.xticks([]), plt.yticks([])

        if len(girl_haar) == 0:
            print("얼굴인식 실패")
            quit()
        for (x, y, w, h,) in girl_haar:
            print(f'얼굴의 좌표 : {x},{y},{w},{h}')
            red = (255, 0, 0)
            cv.rectangle(girl_original, (x, y), (x + w, y + h), red, thickness=20)
        if lines is not None:
            for i in range(lines.shape[0]):
                pt1 = (lines[i][0][0], lines[i][0][1])
                pt2 = (lines[i][0][2], lines[i][0][3])
                cv.line(girl_hough, pt1, pt2, (255, 0, 0), 2, cv.LINE_AA)

        plt.subplot(152), plt.imshow(girl_gray, cmap='gray')
        plt.title('Gray Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(153), plt.imshow(girl_canny, cmap='gray')
        plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(154), plt.imshow(girl_hough, cmap='gray')
        plt.title('Hough Image'), plt.xticks([]), plt.yticks([])
        plt.subplot(155), plt.imshow(girl_original, cmap='gray')
        plt.title('HAAR Image'), plt.xticks([]), plt.yticks([])
        plt.show()




