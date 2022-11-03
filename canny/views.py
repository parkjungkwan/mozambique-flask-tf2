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
    def menu_5(*params):
        ds = Dataset()
        print(params[0])
        # 모델 불러오기
        haar = cv.CascadeClassifier(f"{ds.context}{params[1]}")
        girl = params[2]
        # girl = cv.cvtColor(image_read(girl), cv.COLOR_BGR2RGB)
        #
        girl = cv.imread(f'{ds.context}{girl}')
        face = haar.detectMultiScale(girl, minSize=(150,150))
        if len(face) == 0:
            print("얼굴인식 실패")
            quit()
        for(x,y,w,h) in face:
            print(f'얼굴의 좌표 : {x},{y},{w},{h}')
            red = (0, 0, 255)
            cv.rectangle(girl, (x,y), (x+w, y+h), red, thickness=20)
        girl = cv.resize(girl, (300, 300))
        cv.imwrite(f'{ds.context}girl-face.png', girl)
        cv.imshow('GIRL FACE', girl)
        cv.waitKey(0)
        cv.destroyAllWindows()




