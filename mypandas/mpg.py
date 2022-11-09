import pandas as pd

def my_menu(ls):
    print(f'type is {type(ls)}')
    for i, j in enumerate(ls):
        print(f"{i}. {j}")
    return input('메뉴선택: ')

MENUS = ["종료","mpg 앞부분 확인",
                    "mpg 뒷부분 확인",
                    "행,열 출력",
                    "데이터 속성 확인",
                    "요약 통계량 출력",
                    "문자 변수 요약 통계량 함께 출력"]
class Test:

    def __init__(self):
        self.mpg = pd.read_csv('./data/mpg.csv')

    def head(self):
        print(self.mpg.head(3))

    def tail(self):
        print(self.mpg.tail(3))

    def shape(self):
        print(self.mpg.shape)

    def info(self):
        print(self.mpg.info())

    def describe(self):
        print(self.mpg.describe())

    def describe_include(self):
        print(self.mpg.describe(include ='all'))


if __name__ == '__main__':
    t = Test()
    while True:
        menu = my_menu(MENUS)
        if menu == '0':
            print("종료")
            break
        elif menu == '1':
            print("mpg 앞부분 확인")
            t.head()
        elif menu == '2':
            print("mpg 뒷부분 확인")
            t.tail()
        elif menu == '3':
            print("행,열 출력")
            t.shape()
        elif menu == '4':
            print("데이터 속성 확인")
            t.info()
        elif menu == '5':
            print("요약 통계량 출력")
            t.describe()
        elif menu == '6':
            print("문자 변수 요약 통계량 함께 출력")
            t.describe_include()
        else:
            print("잘못된 번호입니다")