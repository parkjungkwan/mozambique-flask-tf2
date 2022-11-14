from ml.views import StokeController
from titanic.template import Plot
from util.common import Common

if __name__ == '__main__':
    api = StokeController()
    while True:
        menu = Common.menu(["종료", "문제제기", "데이터구하기", 
                            "타깃변수설정", "데이터처리", "시각화",
                            "모델링","학습","예측"])
        if menu == "0":
            print(" ### 종료 ### ")
            break
        elif menu == "1":
            print(" ### 시각화 ### ")
            plot = Plot("train.csv")
            plot.draw_survived()
            plot.draw_sex()
            plot.draw_pclass()
            plot.draw_embarked()
        elif menu == "2":
            print(" ### 데이터구하기 ### ")
            this = api.modeling('train.csv', 'test.csv')
            print(this.train.head())
            print(this.train.columns)
