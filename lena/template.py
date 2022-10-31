import numpy as np
from PIL import Image
import requests
from io import BytesIO
import matplotlib.pyplot as plt

class numcv:
    def __init__(self):
        headers = {
            'User-Agent': 'My User Agent 1.0'
        }  # 위키피디아 이미지를 가져오기 위해 헤더를 생성
        res = requests.get("https://upload.wikimedia.org/wikipedia/ko/2/24/Lenna.png", headers=headers)  # 헤더를 적용해서 요청
        lena = Image.open(BytesIO(res.content))  # 얻어온 이미지를 PIL 형식으로 오픈
        self.lena = np.array(lena)  # PIL 이미지를 numpy 로 변환
        self.createDef()

    def createDef(self):
        self.ADAPTIVE_THRESH_MEAN_C = 0
        self.ADAPTIVE_THRESH_GAUSSIAN_C = 1
        self.THRESH_BINARY = 2
        self.THRESH_BINARY_INV = 3

    def imshow(self, img):
        img = Image.fromarray(img)  # numpy 배열을 PIL 이미지로 변환
        plt.imshow(img)
        plt.show()

    def grayscale(self, img):
        dst = img[:, :, 0] * 0.114 + img[:, :, 1] * 0.587 + img[:, :, 2] * 0.229  # GRAYSCALE 변환 공식
        return dst

    def filter2D(self, src, kernel, delta=0):
        # 가장자리 픽셀을 (커널의 길이 // 2) 만큼 늘리고 새로운 행렬에 저장
        halfX = kernel.shape[0] // 2
        halfY = kernel.shape[1] // 2
        cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

        # (커널의 길이 // 2) 만큼 가장자리에서 안쪽(여기서는 1만큼 안쪽)에 있는 픽셀들의 값을 입력 이미지의 값으로 바꾸어 가장자리에 0을 추가한 효과를 봄
        cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

        dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

        for y in np.arange(src.shape[1]):
            for x in np.arange(src.shape[0]):
                # 필터링 연산
                dst[x, y] = (kernel * cornerPixel[x: x + kernel.shape[0], y: y + kernel.shape[1]]).sum() + delta
        return dst

    def GaussianBlur(self, src, sigmax, sigmay):
        # 가로 커널과 세로 커널 행렬을 생성
        i = np.arange(-4 * sigmax, 4 * sigmax + 1)
        j = np.arange(-4 * sigmay, 4 * sigmay + 1)
        # 가우시안 계산
        mask = np.exp(-(i ** 2 / (2 * sigmax ** 2))) / (np.sqrt(2 * np.pi) * sigmax)
        maskT = np.exp(-(j ** 2 / (2 * sigmay ** 2))) / (np.sqrt(2 * np.pi) * sigmay)
        mask = mask[:, np.newaxis]
        maskT = maskT[:, np.newaxis].T

        dst = self.filter2D(self.filter2D(src, mask), maskT)  # 두번 필터링
        return dst  # float64로 dtype을 변경해서 반환

    def adaptiveThreshold(self, src, adaptiveMethod, thresholdType, blocksize, C):
        mask = np.zeros((blocksize, blocksize))
        if adaptiveMethod == self.ADAPTIVE_THRESH_MEAN_C:
            pass
        elif adaptiveMethod == self.ADAPTIVE_THRESH_GAUSSIAN_C:
            sigma = (blocksize - 1) / 8
            i = np.arange(-(blocksize // 2), (blocksize // 2) + 1)
            j = np.arange(-(blocksize // 2), (blocksize // 2) + 1)
            i, j = np.meshgrid(i, j)
            mask = np.exp(-((i ** 2 / (2 * sigma ** 2)) + (j ** 2 / (2 * sigma ** 2)))) / (2 * np.pi * sigma * sigma)
        else:
            return -1
        # 가장자리 픽셀을 (커널의 길이 // 2) 만큼 늘리고 새로운 행렬에 저장
        halfX = blocksize // 2
        halfY = blocksize // 2
        cornerPixel = np.zeros((src.shape[0] + halfX * 2, src.shape[1] + halfY * 2), dtype=np.uint8)

        # (커널의 길이 // 2) 만큼 가장자리에서 안쪽(여기서는 1만큼 안쪽)에 있는 픽셀들의 값을 입력 이미지의 값으로 바꾸어 가장자리에 0을 추가한 효과를 봄
        cornerPixel[halfX:cornerPixel.shape[0] - halfX, halfY:cornerPixel.shape[1] - halfY] = src

        dst = np.zeros((src.shape[0], src.shape[1]), dtype=np.float64)

        for y in np.arange(src.shape[1]):
            for x in np.arange(src.shape[0]):
                # 필터링 연산
                threshold = 0
                if adaptiveMethod == self.ADAPTIVE_THRESH_MEAN_C:
                    threshold = cornerPixel[x: x + mask.shape[0], y: y + mask.shape[1]].mean() - C

                elif adaptiveMethod == self.ADAPTIVE_THRESH_GAUSSIAN_C:
                    threshold = (mask * cornerPixel[x: x + mask.shape[0], y: y + mask.shape[1]]).sum() / mask.sum() - C

                if thresholdType == self.THRESH_BINARY:
                    if cornerPixel[x, y] > threshold:
                        dst[x, y] = 255
                    else:
                        dst[x, y] = 0
                elif thresholdType == self.THRESH_BINARY_INV:
                    if cornerPixel[x, y] > threshold:
                        dst[x, y] = 0
                    else:
                        dst[x, y] = 255
        return dst

    def Canny(self, src, lowThreshold, highThreshold):
        Kx = np.array([[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]])  # x축 소벨 행렬로 미분
        Ky = np.array([[1, 2, 1], [0, 0, 0], [-1, -2, -1]])  # y축 소벨 행렬로 미분
        Ix = self.filter2D(src, Kx)
        Iy = self.filter2D(src, Ky)
        G = np.hypot(Ix, Iy)  # 피타고라스 빗변 구하기
        img = G / G.max() * 255  # 엣지를 그레이스케일로 표현
        D = np.arctan2(Iy, Ix)  # 아크탄젠트 이용해서 그래디언트를 구함

        M, N = img.shape
        Z = np.zeros((M, N), dtype=np.int32)  # 이미지 크기만큼의 행렬을 생성
        angle = D * 180. / np.pi  # 라디안을 degree로 변환(정확하지 않음)
        angle[angle < 0] += 180  # 음수일 때 180을 더함

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                try:
                    q = 255
                    r = 255

                    # angle 0
                    if (0 <= angle[i, j] < 22.5) or (157.5 <= angle[i, j] <= 180):
                        q = img[i, j + 1]
                        r = img[i, j - 1]
                    # angle 45
                    elif (22.5 <= angle[i, j] < 67.5):
                        q = img[i + 1, j - 1]
                        r = img[i - 1, j + 1]
                    # angle 90
                    elif (67.5 <= angle[i, j] < 112.5):
                        q = img[i + 1, j]
                        r = img[i - 1, j]
                    # angle 135
                    elif (112.5 <= angle[i, j] < 157.5):
                        q = img[i - 1, j - 1]
                        r = img[i + 1, j + 1]

                    if (img[i, j] >= q) and (img[i, j] >= r):  # 주변 픽셀(q, r)보다 크면 img 행렬의 값을 그대로 사용
                        Z[i, j] = img[i, j]
                    else:  # 그렇지 않을 경우 0을 사용
                        Z[i, j] = 0

                except IndexError as e:  # 인덱싱 예외 발생 시 pass
                    pass

        M, N = img.shape
        res = np.zeros((M, N), dtype=np.int32)

        weak = np.int32(25)  # 약한 에지
        strong = np.int32(255)  # 강한 에지

        # 이중 임곗값 비교

        # 최대 임곗값보다 큰 원소의 인덱스를 저장
        strong_i, strong_j = np.where(img >= highThreshold)
        # 최소 임곗값보다 작은 원소의 인덱스를 저장
        zeros_i, zeros_j = np.where(img < lowThreshold)

        # 최소 임곗값과 최대 임곗값 사이에 있는 원소의 인덱스를 저장
        weak_i, weak_j = np.where((img <= highThreshold) & (img >= lowThreshold))

        # 각각 강한 에지와 약한 에지의 값으로 저장
        res[strong_i, strong_j] = strong
        res[weak_i, weak_j] = weak

        for i in range(1, M - 1):
            for j in range(1, N - 1):
                if (img[i, j] == weak):
                    try:
                        if ((img[i + 1, j - 1] == strong) or (img[i + 1, j] == strong) or (img[i + 1, j + 1] == strong)
                                or (img[i, j - 1] == strong) or (img[i, j + 1] == strong)
                                or (img[i - 1, j - 1] == strong) or (img[i - 1, j] == strong) or (
                                        img[i - 1, j + 1] == strong)):  # 강한 에지와 연결 되어있을 때
                            img[i, j] = strong  # 연결되어 있는 에지 또한 강한 에지가 됨
                        else:  # 연결되어 있지 않을 때
                            img[i, j] = 0  # 에지가 없는 0으로 설정
                    except IndexError as e:
                        pass
        return img

if __name__ == '__main__':
    cv = numcv()  # numcv를 cv 객체로 선언
    gray = cv.grayscale(cv.lena)
    gray = cv.GaussianBlur(gray, 1, 1)
    gray = cv.Canny(gray, 50, 150)
    cv.imshow(gray)